from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class PostStatus(enum.Enum):
    """帖子状态"""
    PENDING = "pending"      # 待审核
    PUBLISHED = "published"  # 已发布
    REJECTED = "rejected"    # 已拒绝
    ARCHIVED = "archived"    # 已归档


class Post(Base):
    """论坛帖子表"""
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    
    # 分类
    category_id = Column(Integer, ForeignKey("forum_categories.id"), nullable=True)
    
    # 作者
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 统计
    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    
    # 状态
    status = Column(SQLEnum(PostStatus), default=PostStatus.PUBLISHED)
    is_pinned = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关系
    author = relationship("User", back_populates="posts")
    category = relationship("ForumCategory", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class ForumCategory(Base):
    """论坛分类表"""
    __tablename__ = "forum_categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    slug = Column(String(50), unique=True, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String(500), nullable=True)
    sort_order = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 关系
    posts = relationship("Post", back_populates="category")


class Comment(Base):
    """评论表（通用）"""
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    
    # 关联
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=True)
    content_id = Column(Integer, ForeignKey("contents.id"), nullable=True)
    parent_id = Column(Integer, ForeignKey("comments.id"), nullable=True)
    
    # 统计
    like_count = Column(Integer, default=0)
    
    # 状态
    is_hidden = Column(Boolean, default=False)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关系
    author = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
    content = relationship("Content", back_populates="comments")
    parent = relationship("Comment", remote_side=[id], backref="replies")
