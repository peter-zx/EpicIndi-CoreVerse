import secrets
import string
from datetime import datetime
from typing import Optional, List

from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.models.user import User, UserRole
from app.schemas.user import UserRegister, UserUpdate


def generate_invite_code(length: int = 8) -> str:
    """生成邀请码"""
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


class UserService:
    """用户服务"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        """通过ID获取用户"""
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_username(self, username: str) -> Optional[User]:
        """通过用户名获取用户"""
        result = await self.db.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[User]:
        """通过邮箱获取用户"""
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_by_username_or_email(self, identifier: str) -> Optional[User]:
        """通过用户名或邮箱获取用户"""
        result = await self.db.execute(
            select(User).where(
                or_(User.username == identifier, User.email == identifier)
            )
        )
        return result.scalar_one_or_none()
    
    async def get_by_invite_code(self, invite_code: str) -> Optional[User]:
        """通过邀请码获取用户"""
        result = await self.db.execute(
            select(User).where(User.invite_code == invite_code)
        )
        return result.scalar_one_or_none()
    
    async def validate_invite_code(self, invite_code: str) -> tuple[bool, str, Optional[User]]:
        """
        验证邀请码
        返回: (是否有效, 消息, 邀请人)
        """
        inviter = await self.get_by_invite_code(invite_code)
        
        if not inviter:
            return False, "邀请码不存在", None
        
        if not inviter.is_active:
            return False, "邀请人账号已被禁用", None
        
        if inviter.invite_quota <= 0:
            return False, "该邀请码已达到使用上限", None
        
        return True, "邀请码有效", inviter
    
    async def create_user(self, user_data: UserRegister) -> tuple[Optional[User], str]:
        """
        创建用户
        返回: (用户对象, 消息)
        """
        # 检查用户名是否已存在
        existing_user = await self.get_by_username(user_data.username)
        if existing_user:
            return None, "用户名已被使用"
        
        # 检查邮箱是否已存在
        existing_email = await self.get_by_email(user_data.email)
        if existing_email:
            return None, "邮箱已被注册"
        
        # 验证邀请码（如果启用邀请制）
        inviter = None
        if settings.INVITE_CODE_REQUIRED:
            valid, msg, inviter = await self.validate_invite_code(user_data.invite_code)
            if not valid:
                return None, msg
        
        # 生成唯一邀请码
        while True:
            new_invite_code = generate_invite_code()
            existing = await self.get_by_invite_code(new_invite_code)
            if not existing:
                break
        
        # 创建用户
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=get_password_hash(user_data.password),
            nickname=user_data.username,
            invite_code=new_invite_code,
            invited_by_id=inviter.id if inviter else None,
            invite_quota=settings.DEFAULT_INVITE_QUOTA,
            points=settings.POINTS_FOR_REGISTER,
            total_points_earned=settings.POINTS_FOR_REGISTER,
            role=UserRole.USER,
        )
        
        self.db.add(new_user)
        
        # 减少邀请人的邀请配额
        if inviter:
            inviter.invite_quota -= 1
        
        await self.db.flush()
        await self.db.refresh(new_user)
        
        return new_user, "注册成功"
    
    async def authenticate(self, identifier: str, password: str) -> Optional[User]:
        """
        验证用户登录
        """
        user = await self.get_by_username_or_email(identifier)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    async def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """更新用户信息"""
        user = await self.get_by_id(user_id)
        if not user:
            return None
        
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        user.updated_at = datetime.utcnow()
        await self.db.flush()
        await self.db.refresh(user)
        
        return user
    
    async def update_last_login(self, user: User) -> None:
        """更新最后登录时间"""
        user.last_login_at = datetime.utcnow()
        await self.db.flush()
    
    async def get_invited_users(self, user_id: int) -> List[User]:
        """获取用户邀请的人"""
        result = await self.db.execute(
            select(User).where(User.invited_by_id == user_id)
        )
        return list(result.scalars().all())
    
    async def add_points(self, user_id: int, points: int, reason: str = "") -> Optional[User]:
        """增加积分"""
        user = await self.get_by_id(user_id)
        if not user:
            return None
        
        user.points += points
        if points > 0:
            user.total_points_earned += points
        
        await self.db.flush()
        return user
    
    async def deduct_points(self, user_id: int, points: int) -> tuple[bool, str]:
        """扣除积分"""
        user = await self.get_by_id(user_id)
        if not user:
            return False, "用户不存在"
        
        if user.points < points:
            return False, "积分不足"
        
        user.points -= points
        await self.db.flush()
        return True, "扣除成功"
