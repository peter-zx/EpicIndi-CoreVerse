from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum, Numeric
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class PointActionType(enum.Enum):
    """积分操作类型"""
    # 获得
    REGISTER = "register"               # 注册奖励
    DAILY_LOGIN = "daily_login"         # 每日登录
    POST = "post"                       # 发帖
    COMMENT = "comment"                 # 评论
    HOMEWORK_SUBMIT = "homework_submit" # 提交作业
    HOMEWORK_REVIEW = "homework_review" # 批阅作业
    INVITE = "invite"                   # 邀请用户
    RECHARGE = "recharge"               # 充值
    TASK_REWARD = "task_reward"         # 任务奖励
    ADMIN_GRANT = "admin_grant"         # 管理员发放
    
    # 消费
    UNLOCK_CONTENT = "unlock_content"   # 解锁内容
    UNLOCK_TOOL = "unlock_tool"         # 解锁工具
    PUBLISH_TASK = "publish_task"       # 发布任务
    TRANSFER = "transfer"               # 转账


class PointRecord(Base):
    """积分记录表"""
    __tablename__ = "point_records"
    
    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    action_type = Column(SQLEnum(PointActionType), nullable=False)
    points = Column(Integer, nullable=False)             # 正数获得，负数消费
    balance = Column(Integer, nullable=False)            # 操作后余额
    
    description = Column(String(200), nullable=True)
    reference_id = Column(Integer, nullable=True)        # 关联ID（如任务ID、内容ID等）
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 关系
    user = relationship("User", back_populates="point_records")


class PaymentStatus(enum.Enum):
    """支付状态"""
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    REFUNDED = "refunded"


class PaymentRecord(Base):
    """充值/支付记录表"""
    __tablename__ = "payment_records"
    
    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 订单信息
    order_no = Column(String(64), unique=True, index=True, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)      # 支付金额
    points = Column(Integer, nullable=False)             # 获得积分
    
    # 支付方式
    payment_method = Column(String(20), nullable=False)  # alipay/wechat
    trade_no = Column(String(64), nullable=True)         # 第三方交易号
    
    # 状态
    status = Column(SQLEnum(PaymentStatus), default=PaymentStatus.PENDING)
    
    # 时间戳
    created_at = Column(DateTime, default=datetime.utcnow)
    paid_at = Column(DateTime, nullable=True)
    
    # 关系
    user = relationship("User")
