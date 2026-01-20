from typing import Optional, Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.models.user import User, UserRole
from app.services.user import UserService
from app.schemas.user import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    auto_error=False
)


async def get_current_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    token: Annotated[Optional[str], Depends(oauth2_scheme)]
) -> Optional[User]:
    """
    获取当前用户（可选认证）
    如果没有token或token无效，返回None
    """
    if not token:
        return None
    
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        if token_data.sub is None:
            return None
            
    except JWTError:
        return None
    
    user_service = UserService(db)
    user = await user_service.get_by_id(token_data.sub)
    
    if not user or not user.is_active:
        return None
    
    return user


async def get_current_user_required(
    current_user: Annotated[Optional[User], Depends(get_current_user)]
) -> User:
    """
    获取当前用户（必须认证）
    如果未登录，抛出401异常
    """
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="未登录或登录已过期",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user_required)]
) -> User:
    """
    获取当前活跃用户
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="账号已被禁用"
        )
    return current_user


async def get_current_admin(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> User:
    """
    获取当前管理员用户
    """
    if current_user.role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要管理员权限"
        )
    return current_user


async def get_current_super_admin(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> User:
    """
    获取当前超级管理员
    """
    if current_user.role != UserRole.SUPER_ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要超级管理员权限"
        )
    return current_user


async def get_senior_or_admin(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> User:
    """
    获取高级用户或管理员（可批阅作业）
    """
    allowed_roles = [UserRole.SENIOR, UserRole.ADMIN, UserRole.SUPER_ADMIN]
    if current_user.role not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要高级用户或管理员权限"
        )
    return current_user


# 类型别名，方便使用
CurrentUser = Annotated[User, Depends(get_current_user_required)]
CurrentActiveUser = Annotated[User, Depends(get_current_active_user)]
CurrentAdmin = Annotated[User, Depends(get_current_admin)]
CurrentSuperAdmin = Annotated[User, Depends(get_current_super_admin)]
OptionalUser = Annotated[Optional[User], Depends(get_current_user)]
