from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, field_validator
import re


# ============ Token相关 ============
class Token(BaseModel):
    """Token响应"""
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Token载荷"""
    sub: Optional[int] = None
    exp: Optional[datetime] = None


# ============ 用户注册 ============
class UserRegister(BaseModel):
    """用户注册请求"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)
    invite_code: str = Field(..., min_length=6, max_length=20)
    
    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not re.match(r"^[a-zA-Z0-9_\u4e00-\u9fa5]+$", v):
            raise ValueError("用户名只能包含字母、数字、下划线和中文")
        return v
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("密码必须包含至少一个数字")
        if not any(c.isalpha() for c in v):
            raise ValueError("密码必须包含至少一个字母")
        return v


# ============ 用户登录 ============
class UserLogin(BaseModel):
    """用户登录请求"""
    username: str  # 可以是用户名或邮箱
    password: str


# ============ 用户信息 ============
class UserBase(BaseModel):
    """用户基础信息"""
    username: str
    email: EmailStr
    nickname: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None


class UserCreate(UserBase):
    """创建用户（内部使用）"""
    password: str
    invite_code: str


class UserUpdate(BaseModel):
    """更新用户信息"""
    nickname: Optional[str] = Field(None, max_length=50)
    avatar: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=500)
    phone: Optional[str] = Field(None, max_length=20)


class UserAdminUpdate(BaseModel):
    """管理员更新用户信息"""
    nickname: Optional[str] = Field(None, max_length=50)
    avatar: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=500)
    phone: Optional[str] = Field(None, max_length=20)
    role: Optional[str] = None  # 'USER', 'SENIOR', 'ADMIN', 'SUPER_ADMIN'
    level: Optional[int] = Field(None, ge=1, le=8)
    experience: Optional[int] = Field(None, ge=0)
    points: Optional[int] = Field(None, ge=0)
    invite_quota: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None


class UserInDB(UserBase):
    """数据库中的用户"""
    id: int
    role: str
    level: int
    experience: int
    points: int
    total_points_earned: int
    invite_code: str
    invite_quota: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    last_login_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserPublic(BaseModel):
    """公开的用户信息"""
    id: int
    username: str
    nickname: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    level: int
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserProfile(UserInDB):
    """用户完整信息（本人可见）"""
    invited_count: int = 0
    
    class Config:
        from_attributes = True


# ============ 邀请码相关 ============
class InviteCodeInfo(BaseModel):
    """邀请码信息"""
    code: str
    remaining_quota: int
    invited_users: List[UserPublic] = []


class InviteCodeValidate(BaseModel):
    """验证邀请码请求"""
    invite_code: str


class InviteCodeResponse(BaseModel):
    """验证邀请码响应"""
    valid: bool
    message: str
    inviter: Optional[UserPublic] = None
