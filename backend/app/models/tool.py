from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class ToolCategory(enum.Enum):
    """工具分类"""
    AI = "ai"
    VIDEO = "video"
    AUDIO = "audio"
    DATA = "data"
    DESIGN = "design"
    OTHER = "other"


class Tool(Base):
    """工具箱表"""
    __tablename__ = "tools"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, index=True)
    description = Column(Text, nullable=True)
    
    # 工具信息
    category = Column(SQLEnum(ToolCategory), default=ToolCategory.OTHER)
    icon = Column(String(500), nullable=True)
    cover_image = Column(String(500), nullable=True)
    version = Column(String(20), nullable=True)
    
    # 下载相关
    download_url = Column(String(500), nullable=True)    # OSS下载链接
    file_size = Column(Integer, nullable=True)           # 文件大小（字节）
    
    # 使用说明
    usage_guide = Column(Text, nullable=True)
    video_tutorial_url = Column(String(500), nullable=True)
    
    # 访问控制
    is_free = Column(Boolean, default=False)
    required_points = Column(Integer, default=0)
    required_level = Column(Integer, default=0)
    
    # 统计
    download_count = Column(Integer, default=0)
    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    
    # 状态
    is_active = Column(Boolean, default=True)
    is_featured = Column(Boolean, default=False)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
