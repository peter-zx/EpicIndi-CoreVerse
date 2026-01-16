from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # 项目基础配置
    PROJECT_NAME: str = "AIGC散修学习平台"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    
    # 安全配置
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7天
    ALGORITHM: str = "HS256"
    
    # 数据库配置
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "epicindi_coreverse"
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    # Redis配置
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    
    # 阿里云OSS配置
    OSS_ACCESS_KEY_ID: Optional[str] = None
    OSS_ACCESS_KEY_SECRET: Optional[str] = None
    OSS_BUCKET_NAME: Optional[str] = None
    OSS_ENDPOINT: Optional[str] = None
    
    # 支付配置
    ALIPAY_APP_ID: Optional[str] = None
    ALIPAY_PRIVATE_KEY: Optional[str] = None
    ALIPAY_PUBLIC_KEY: Optional[str] = None
    
    # 邀请码配置
    INVITE_CODE_REQUIRED: bool = True
    DEFAULT_INVITE_QUOTA: int = 5
    
    # 积分配置
    POINTS_FOR_REGISTER: int = 100
    POINTS_FOR_DAILY_LOGIN: int = 10
    POINTS_FOR_POST: int = 20
    POINTS_FOR_COMMENT: int = 5
    POINTS_FOR_HOMEWORK_SUBMIT: int = 30
    POINTS_FOR_HOMEWORK_REVIEW: int = 50
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
