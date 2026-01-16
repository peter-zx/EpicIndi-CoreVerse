from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from app.core.database import Base


class Partner(Base):
    """合作方/赞助商表"""
    __tablename__ = "partners"
    
    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String(100), nullable=False)
    logo = Column(String(500), nullable=True)
    website = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    
    # 联系方式
    contact_name = Column(String(50), nullable=True)
    contact_email = Column(String(100), nullable=True)
    contact_phone = Column(String(20), nullable=True)
    
    # 展示设置
    is_active = Column(Boolean, default=True)
    is_sponsor = Column(Boolean, default=False)          # 是否为赞助商
    sort_order = Column(Integer, default=0)
    
    # 广告位
    banner_image = Column(String(500), nullable=True)
    banner_link = Column(String(500), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SiteConfig(Base):
    """网站配置表"""
    __tablename__ = "site_configs"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, index=True, nullable=False)
    value = Column(Text, nullable=True)
    description = Column(String(200), nullable=True)
    
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
