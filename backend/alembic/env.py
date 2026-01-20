import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
sys.path.append(str(Path(__file__).parent.parent))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 导入配置和模型
from app.core.config import settings
from app.core.database import Base

# 导入所有模型，确保被Alembic识别
from app.models.user import User, UserLevel
from app.models.content import Content, Category
from app.models.forum import Post, ForumCategory, Comment
from app.models.tool import Tool
from app.models.homework import Homework, HomeworkSubmission, HomeworkReview
from app.models.points import PointRecord, PaymentRecord
from app.models.task import Task, TaskApplicationRecord
from app.models.partner import Partner, SiteConfig

# Alembic配置对象
config = context.config

# 设置数据库URL
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL.replace("+asyncpg", ""))

# 解析日志配置
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 目标元数据
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """离线模式运行迁移"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """在线模式运行迁移"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
