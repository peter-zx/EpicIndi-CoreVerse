from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_

from app.core.database import get_db
from app.api.deps import CurrentActiveUser, OptionalUser, CurrentAdmin
from app.services.user import UserService
from app.models.user import User, UserRole
from app.schemas.user import (
    UserInDB,
    UserPublic,
    UserProfile,
    UserUpdate,
    InviteCodeInfo,
    UserAdminUpdate
)
from app.schemas.common import ResponseData, ResponseList

router = APIRouter()


# === 管理员用户管理接口 ===
@router.get("/admin/users", response_model=ResponseList[UserProfile])
async def admin_get_users(
    db: Annotated[AsyncSession, Depends(get_db)],
    current_admin: CurrentAdmin = None,
    skip: int = 0,
    limit: int = 20,
    search: Optional[str] = None,
    role: Optional[UserRole] = None,
    is_active: Optional[bool] = None
):
    """管理员获取用户列表"""
    query = select(User)
    
    if search:
        query = query.where(
            or_(
                User.username.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                User.nickname.ilike(f"%{search}%")
            )
        )
    
    if role:
        query = query.where(User.role == role)
    
    if is_active is not None:
        query = query.where(User.is_active == is_active)
    
    # 获取总数
    count_query = select(func.count()).select_from(User)
    if search:
        count_query = count_query.where(
            or_(
                User.username.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                User.nickname.ilike(f"%{search}%")
            )
        )
    if role:
        count_query = count_query.where(User.role == role)
    if is_active is not None:
        count_query = count_query.where(User.is_active == is_active)
    
    total_result = await db.execute(count_query)
    total = total_result.scalar()
    
    # 获取用户列表
    query = query.order_by(User.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    users = result.scalars().all()
    
    users_profile = [UserProfile.model_validate(u) for u in users]
    
    return ResponseList(
        data=users_profile,
        total=total
    )


@router.get("/admin/users/{user_id}", response_model=ResponseData[UserProfile])
async def admin_get_user(
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
    current_admin: CurrentAdmin = None
):
    """管理员获取用户详情"""
    user_service = UserService(db)
    user = await user_service.get_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return ResponseData(data=UserProfile.model_validate(user))


@router.put("/admin/users/{user_id}", response_model=ResponseData[UserProfile])
async def admin_update_user(
    user_id: int,
    user_data: UserAdminUpdate,
    db: Annotated[AsyncSession, Depends(get_db)],
    current_admin: CurrentAdmin = None
):
    """管理员更新用户信息"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    # 更新字段
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    
    await db.commit()
    await db.refresh(user)
    
    return ResponseData(
        message="更新成功",
        data=UserProfile.model_validate(user)
    )


@router.post("/admin/users/{user_id}/ban")
async def admin_ban_user(
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
    current_admin: CurrentAdmin = None
):
    """管理员封禁用户"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    user.is_active = False
    await db.commit()
    
    return ResponseData(message="用户已封禁")


@router.post("/admin/users/{user_id}/unban")
async def admin_unban_user(
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
    current_admin: CurrentAdmin = None
):
    """管理员解封用户"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    user.is_active = True
    await db.commit()
    
    return ResponseData(message="用户已解封")


@router.post("/admin/users/{user_id}/points")
async def admin_adjust_points(
    user_id: int,
    points: int,
    reason: str,
    db: Annotated[AsyncSession, Depends(get_db)],
    current_admin: CurrentAdmin = None
):
    """管理员调整用户积分"""
    user_service = UserService(db)
    user = await user_service.add_points(user_id, points)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return ResponseData(
        message=f"积分调整成功：{points:+d}",
        data={"points": user.points, "total_earned": user.total_points_earned}
    )


# === 普通用户接口 ===
@router.get("/me", response_model=ResponseData[UserProfile])
async def get_current_user_info(
    current_user: CurrentActiveUser,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    获取当前用户信息
    """
    user_service = UserService(db)
    invited_users = await user_service.get_invited_users(current_user.id)
    
    user_data = UserProfile.model_validate(current_user)
    user_data.invited_count = len(invited_users)
    
    return ResponseData(data=user_data)


@router.put("/me", response_model=ResponseData[UserInDB])
async def update_current_user(
    user_data: UserUpdate,
    current_user: CurrentActiveUser,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    更新当前用户信息
    
    - **nickname**: 昵称（最多50字符）
    - **avatar**: 头像URL
    - **bio**: 个人简介（最多500字符）
    - **phone**: 手机号
    """
    user_service = UserService(db)
    
    updated_user = await user_service.update_user(current_user.id, user_data)
    
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return ResponseData(
        message="更新成功",
        data=UserInDB.model_validate(updated_user)
    )


@router.get("/me/points")
async def get_my_points(current_user: CurrentActiveUser):
    """
    获取我的积分信息
    """
    return ResponseData(data={
        "points": current_user.points,
        "total_earned": current_user.total_points_earned,
        "level": current_user.level,
        "experience": current_user.experience
    })


@router.get("/me/invite-code", response_model=ResponseData[InviteCodeInfo])
async def get_my_invite_code(
    current_user: CurrentActiveUser,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    获取我的邀请码信息
    """
    user_service = UserService(db)
    invited_users = await user_service.get_invited_users(current_user.id)
    
    invited_public = [UserPublic.model_validate(u) for u in invited_users]
    
    return ResponseData(data=InviteCodeInfo(
        code=current_user.invite_code,
        remaining_quota=current_user.invite_quota,
        invited_users=invited_public
    ))


@router.get("/me/invited-users", response_model=ResponseList[UserPublic])
async def get_my_invited_users(
    current_user: CurrentActiveUser,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    获取我邀请的用户列表
    """
    user_service = UserService(db)
    invited_users = await user_service.get_invited_users(current_user.id)
    
    users_public = [UserPublic.model_validate(u) for u in invited_users]
    
    return ResponseList(
        data=users_public,
        total=len(users_public)
    )


@router.get("/leaderboard", response_model=ResponseList[UserPublic])
async def get_leaderboard(
    db: Annotated[AsyncSession, Depends(get_db)],
    limit: int = 10
):
    """
    获取用户积分排行榜
    
    - **limit**: 返回数量（默认10，最多50）
    """
    from sqlalchemy import select
    from app.models.user import User
    
    limit = min(limit, 50)
    
    result = await db.execute(
        select(User)
        .where(User.is_active == True)
        .order_by(User.points.desc())
        .limit(limit)
    )
    users = result.scalars().all()
    
    users_public = [UserPublic.model_validate(u) for u in users]
    
    return ResponseList(
        data=users_public,
        total=len(users_public)
    )


@router.get("/{user_id}", response_model=ResponseData[UserPublic])
async def get_user_profile(
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    获取用户公开信息
    """
    user_service = UserService(db)
    user = await user_service.get_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return ResponseData(data=UserPublic.model_validate(user))
