from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class UserRole(enum.Enum):
    """用户角色"""
    USER = "user"                    # 普通用户
    SENIOR = "senior"                # 高级用户（可批阅作业）
    ADMIN = "admin"                  # 管理员
    SUPER_ADMIN = "super_admin"      # 超级管理员


class User(Base):
    """用户表"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), unique=True, index=True, nullable=True)
    hashed_password = Column(String(255), nullable=False)
    
    # 用户信息
    nickname = Column(String(50), nullable=True)
    avatar = Column(String(500), nullable=True)
    bio = Column(Text, nullable=True)
    
    # 角色和等级
    role = Column(SQLEnum(UserRole), default=UserRole.USER)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    
    # 积分
    points = Column(Integer, default=0)
    total_points_earned = Column(Integer, default=0)
    
    # 邀请相关
    invite_code = Column(String(20), unique=True, index=True)
    invited_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    invite_quota = Column(Integer, default=5)
    
    # 状态
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login_at = Column(DateTime, nullable=True)
    
    # 关系
    invited_by = relationship("User", remote_side=[id], backref="invited_users")
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    homeworks = relationship("HomeworkSubmission", back_populates="student")
    reviews = relationship("HomeworkReview", back_populates="reviewer")
    point_records = relationship("PointRecord", back_populates="user")


class UserLevel(Base):
    """用户等级配置表"""
    __tablename__ = "user_levels"
    
    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, unique=True, nullable=False)
    name = Column(String(50), nullable=False)           # 等级名称
    min_experience = Column(Integer, nullable=False)     # 所需经验值
    icon = Column(String(500), nullable=True)            # 等级图标
    
    # 特权
    can_post = Column(Boolean, default=True)
    can_comment = Column(Boolean, default=True)
    can_publish_task = Column(Boolean, default=False)    # 可发布任务
    can_review_homework = Column(Boolean, default=False) # 可批阅作业
    daily_download_limit = Column(Integer, default=5)    # 每日下载限制
    
    created_at = Column(DateTime, default=datetime.utcnow)
