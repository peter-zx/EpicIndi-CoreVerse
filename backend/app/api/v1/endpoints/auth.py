from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import create_access_token
from app.services.user import UserService
from app.schemas.user import (
    UserRegister, 
    UserInDB, 
    Token, 
    InviteCodeValidate,
    InviteCodeResponse,
    UserPublic
)
from app.schemas.common import ResponseData

router = APIRouter()


@router.post("/register", response_model=ResponseData[UserInDB])
async def register(
    user_data: UserRegister,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    用户注册（需要邀请码）
    
    - **username**: 用户名（3-50字符，字母数字下划线中文）
    - **email**: 邮箱
    - **password**: 密码（至少8位，包含字母和数字）
    - **invite_code**: 邀请码
    """
    user_service = UserService(db)
    
    user, message = await user_service.create_user(user_data)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )
    
    return ResponseData(
        code=200,
        message=message,
        data=UserInDB.model_validate(user)
    )


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    用户登录
    
    - **username**: 用户名或邮箱
    - **password**: 密码
    
    返回JWT Token
    """
    user_service = UserService(db)
    
    user = await user_service.authenticate(
        identifier=form_data.username,
        password=form_data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="账号已被禁用"
        )
    
    # 更新最后登录时间
    await user_service.update_last_login(user)
    
    # 生成Token
    access_token = create_access_token(subject=user.id)
    
    return Token(access_token=access_token)


@router.post("/validate-invite-code", response_model=InviteCodeResponse)
async def validate_invite_code(
    data: InviteCodeValidate,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    验证邀请码是否有效
    
    - **invite_code**: 邀请码
    """
    user_service = UserService(db)
    
    valid, message, inviter = await user_service.validate_invite_code(data.invite_code)
    
    inviter_public = None
    if inviter:
        inviter_public = UserPublic.model_validate(inviter)
    
    return InviteCodeResponse(
        valid=valid,
        message=message,
        inviter=inviter_public
    )


@router.post("/logout")
async def logout():
    """
    用户登出
    
    客户端需要删除本地存储的Token
    """
    return {"message": "登出成功，请在客户端删除Token"}


@router.post("/refresh", response_model=Token)
async def refresh_token():
    """
    刷新Token（预留接口）
    
    TODO: 实现Refresh Token机制
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="功能开发中"
    )


@router.post("/forgot-password")
async def forgot_password():
    """
    忘记密码（预留接口）
    
    TODO: 发送重置密码邮件
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="功能开发中"
    )


@router.post("/reset-password")
async def reset_password():
    """
    重置密码（预留接口）
    
    TODO: 通过邮件链接重置密码
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="功能开发中"
    )
