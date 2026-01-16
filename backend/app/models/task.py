from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum, JSON
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class TaskStatus(enum.Enum):
    """任务状态"""
    OPEN = "open"           # 开放中
    IN_PROGRESS = "in_progress"  # 进行中
    COMPLETED = "completed"  # 已完成
    CANCELLED = "cancelled"  # 已取消


class TaskApplication(enum.Enum):
    """申请状态"""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


class Task(Base):
    """悬赏任务表"""
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=True)
    
    # 发布者
    publisher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 奖励
    reward_points = Column(Integer, nullable=False)      # 悬赏积分
    
    # 时间限制
    deadline = Column(DateTime, nullable=True)
    
    # 状态
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.OPEN)
    
    # 接受者
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    # 关系
    publisher = relationship("User", foreign_keys=[publisher_id])
    assignee = relationship("User", foreign_keys=[assignee_id])
    applications = relationship("TaskApplicationRecord", back_populates="task")


class TaskApplicationRecord(Base):
    """任务申请记录"""
    __tablename__ = "task_applications"
    
    id = Column(Integer, primary_key=True, index=True)
    
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    applicant_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    message = Column(Text, nullable=True)
    status = Column(SQLEnum(TaskApplication), default=TaskApplication.PENDING)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 关系
    task = relationship("Task", back_populates="applications")
    applicant = relationship("User")
