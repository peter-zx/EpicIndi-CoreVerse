from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum, JSON
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class HomeworkStatus(enum.Enum):
    """作业状态"""
    DRAFT = "draft"
    PUBLISHED = "published"
    CLOSED = "closed"


class SubmissionStatus(enum.Enum):
    """提交状态"""
    PENDING = "pending"       # 待批阅
    REVIEWING = "reviewing"   # 批阅中
    REVIEWED = "reviewed"     # 已批阅
    RETURNED = "returned"     # 已退回


class Homework(Base):
    """作业/练习表"""
    __tablename__ = "homeworks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    
    # 作业内容
    requirements = Column(Text, nullable=True)           # 作业要求
    reference_materials = Column(JSON, default=list)     # 参考资料链接
    
    # 关联内容
    related_content_id = Column(Integer, ForeignKey("contents.id"), nullable=True)
    
    # 奖励
    base_points = Column(Integer, default=30)            # 完成基础积分
    excellent_points = Column(Integer, default=50)       # 优秀作业额外积分
    
    # 截止时间
    deadline = Column(DateTime, nullable=True)
    
    # 状态
    status = Column(SQLEnum(HomeworkStatus), default=HomeworkStatus.PUBLISHED)
    
    # 统计
    submission_count = Column(Integer, default=0)
    
    # 发布者
    publisher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关系
    publisher = relationship("User")
    submissions = relationship("HomeworkSubmission", back_populates="homework")


class HomeworkSubmission(Base):
    """作业提交表"""
    __tablename__ = "homework_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # 关联
    homework_id = Column(Integer, ForeignKey("homeworks.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 提交内容
    content = Column(Text, nullable=False)
    attachments = Column(JSON, default=list)             # 附件URL列表
    
    # 状态
    status = Column(SQLEnum(SubmissionStatus), default=SubmissionStatus.PENDING)
    
    # 获得积分
    points_earned = Column(Integer, default=0)
    
    # 时间戳
    submitted_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关系
    homework = relationship("Homework", back_populates="submissions")
    student = relationship("User", back_populates="homeworks")
    reviews = relationship("HomeworkReview", back_populates="submission")


class HomeworkReview(Base):
    """作业批阅表"""
    __tablename__ = "homework_reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # 关联
    submission_id = Column(Integer, ForeignKey("homework_submissions.id"), nullable=False)
    reviewer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 批阅内容
    score = Column(Integer, nullable=True)               # 评分（0-100）
    comment = Column(Text, nullable=False)               # 评语
    is_excellent = Column(Boolean, default=False)        # 是否优秀
    
    # 时间戳
    reviewed_at = Column(DateTime, default=datetime.utcnow)
    
    # 关系
    submission = relationship("HomeworkSubmission", back_populates="reviews")
    reviewer = relationship("User", back_populates="reviews")
