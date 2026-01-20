from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum, JSON
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class ContentType(enum.Enum):
    """内容类型"""
    VIDEO = "video"
    ARTICLE = "article"
    PODCAST = "podcast"


class ContentStatus(enum.Enum):
    """内容状态"""
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Content(Base):
    """内容表（视频、图文、播客）"""
    __tablename__ = "contents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, index=True)
    description = Column(Text, nullable=True)
    content_type = Column(SQLEnum(ContentType), nullable=False)
    
    # 内容详情
    body = Column(Text, nullable=True)                   # 图文内容/播客描述
    video_url = Column(String(500), nullable=True)       # 视频URL（OSS或B站嵌入）
    video_source = Column(String(50), nullable=True)     # 视频来源：oss/bilibili/youtube
    cover_image = Column(String(500), nullable=True)     # 封面图
    duration = Column(Integer, nullable=True)            # 时长（秒）
    
    # 分类和标签
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    tags = Column(JSON, default=list)
    
    # 访问控制
    is_free = Column(Boolean, default=True)
    required_points = Column(Integer, default=0)         # 解锁所需积分
    required_level = Column(Integer, default=0)          # 解锁所需等级
    
    # 统计
    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    share_count = Column(Integer, default=0)
    
    # 状态
    status = Column(SQLEnum(ContentStatus), default=ContentStatus.DRAFT)
    is_featured = Column(Boolean, default=False)         # 是否精选/热门
    is_pinned = Column(Boolean, default=False)           # 是否置顶
    
    # 作者
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime, nullable=True)
    
    # 关系
    category = relationship("Category", back_populates="contents")
    author = relationship("User")
    comments = relationship("Comment", back_populates="content")


class Category(Base):
    """分类表"""
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    slug = Column(String(50), unique=True, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String(500), nullable=True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    sort_order = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 关系
    parent = relationship("Category", remote_side=[id], backref="children")
    contents = relationship("Content", back_populates="category")
