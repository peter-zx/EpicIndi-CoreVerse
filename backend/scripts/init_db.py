"""
数据库初始化脚本

用法:
    python scripts/init_db.py

功能:
    1. 创建所有数据库表
    2. 初始化等级配置
    3. 创建超级管理员账号
"""
import asyncio
import sys
import os
from pathlib import Path

# 设置 UTF-8 编码
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# 添加项目根目录到 Python 路径
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy import select
from app.core.database import Base, engine, AsyncSessionLocal
from app.core.security import get_password_hash
from app.models.user import User, UserLevel, UserRole
from app.models.content import Category
from app.models.forum import ForumCategory
from app.models.homework import HomeworkCategory
from app.services.user import generate_invite_code


async def create_tables():
    """创建所有表"""
    print("🔧 创建数据库表...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表创建成功")


async def init_user_levels():
    """初始化用户等级配置"""
    print("🔧 初始化用户等级...")
    
    async with AsyncSessionLocal() as session:
        # 检查是否已存在等级配置
        result = await session.execute(select(UserLevel))
        if result.scalar_one_or_none():
            print("⚠️  等级配置已存在，跳过")
            return
        
        levels = [
            UserLevel(
                level=1, name="见习散修", min_experience=0,
                can_post=True, can_comment=True, daily_download_limit=3
            ),
            UserLevel(
                level=2, name="炼气散修", min_experience=100,
                can_post=True, can_comment=True, daily_download_limit=5
            ),
            UserLevel(
                level=3, name="筑基散修", min_experience=500,
                can_post=True, can_comment=True, daily_download_limit=10
            ),
            UserLevel(
                level=4, name="金丹散修", min_experience=1500,
                can_post=True, can_comment=True, can_publish_task=True, daily_download_limit=20
            ),
            UserLevel(
                level=5, name="元婴散修", min_experience=3000,
                can_post=True, can_comment=True, can_publish_task=True, daily_download_limit=30
            ),
            UserLevel(
                level=6, name="化神散修", min_experience=5000,
                can_post=True, can_comment=True, can_publish_task=True,
                can_review_homework=True, daily_download_limit=50
            ),
            UserLevel(
                level=7, name="渡劫散修", min_experience=10000,
                can_post=True, can_comment=True, can_publish_task=True,
                can_review_homework=True, daily_download_limit=100
            ),
            UserLevel(
                level=8, name="大乘散修", min_experience=20000,
                can_post=True, can_comment=True, can_publish_task=True,
                can_review_homework=True, daily_download_limit=999
            ),
        ]
        
        session.add_all(levels)
        await session.commit()
        print(f"✅ 创建了 {len(levels)} 个等级配置")


async def init_categories():
    """初始化内容分类"""
    print("🔧 初始化内容分类...")
    
    async with AsyncSessionLocal() as session:
        # 检查是否已存在分类
        result = await session.execute(select(Category))
        if result.scalar_one_or_none():
            print("⚠️  内容分类已存在，跳过")
        else:
            categories = [
                Category(name="联盟导演LOL", slug="lol-director", sort_order=1),
                Category(name="AI绘画", slug="ai-art", sort_order=2),
                Category(name="机器学习", slug="ml", sort_order=3),
                Category(name="Python", slug="python", sort_order=4),
                Category(name="工具开发", slug="tools", sort_order=5),
                Category(name="设计", slug="design", sort_order=6),
                Category(name="其他", slug="other", sort_order=99),
            ]
            session.add_all(categories)
            await session.commit()
            print(f"✅ 创建了 {len(categories)} 个内容分类")
        
        # 论坛分类
        result = await session.execute(select(ForumCategory))
        if result.scalar_one_or_none():
            print("⚠️  论坛分类已存在，跳过")
        else:
            forum_categories = [
                ForumCategory(name="技术讨论", slug="tech", sort_order=1),
                ForumCategory(name="问答求助", slug="qa", sort_order=2),
                ForumCategory(name="作品分享", slug="showcase", sort_order=3),
                ForumCategory(name="资源分享", slug="resources", sort_order=4),
                ForumCategory(name="闲聊灌水", slug="chat", sort_order=5),
            ]
            session.add_all(forum_categories)
            await session.commit()
            print(f"✅ 创建了 {len(forum_categories)} 个论坛分类")
        
        # 作业分类
        result = await session.execute(select(HomeworkCategory))
        if result.scalar_one_or_none():
            print("⚠️  作业分类已存在，跳过")
        else:
            homework_categories = [
                HomeworkCategory(name="联盟导演LOL", slug="lol-director", sort_order=1),
                HomeworkCategory(name="AI绘画", slug="ai-art", sort_order=2),
                HomeworkCategory(name="视频剪辑", slug="video-editing", sort_order=3),
                HomeworkCategory(name="编程实战", slug="coding", sort_order=4),
                HomeworkCategory(name="设计练习", slug="design", sort_order=5),
                HomeworkCategory(name="其他", slug="other", sort_order=99),
            ]
            session.add_all(homework_categories)
            await session.commit()
            print(f"✅ 创建了 {len(homework_categories)} 个作业分类")


async def create_super_admin():
    """创建超级管理员账号"""
    print("🔧 创建超级管理员账号...")
    
    async with AsyncSessionLocal() as session:
        # 检查是否已存在管理员
        result = await session.execute(
            select(User).where(User.role == UserRole.SUPER_ADMIN)
        )
        if result.scalar_one_or_none():
            print("⚠️  超级管理员已存在，跳过")
            return
        
        # 创建超级管理员
        admin = User(
            username="admin",
            email="admin@epicindi.com",
            hashed_password=get_password_hash("admin123456"),
            nickname="站长_竹相左边",
            bio="AIGC散修创始人，只分享验证可行的前沿技术",
            role=UserRole.SUPER_ADMIN,
            level=8,
            experience=99999,
            points=99999,
            total_points_earned=99999,
            invite_code=generate_invite_code(),
            invite_quota=999,
            is_active=True,
            is_verified=True,
        )
        
        session.add(admin)
        await session.commit()
        await session.refresh(admin)
        
        print("✅ 超级管理员创建成功")
        print(f"   用户名: {admin.username}")
        print(f"   邮箱: {admin.email}")
        print(f"   密码: admin123456")
        print(f"   邀请码: {admin.invite_code}")
        print(f"\n⚠️  请立即修改默认密码！")


async def create_initial_invite_codes():
    """创建初始邀请码用户（用于冷启动）"""
    print("🔧 创建初始邀请码用户...")
    
    async with AsyncSessionLocal() as session:
        # 检查是否已存在初始邀请码用户
        result = await session.execute(
            select(User).where(User.username == "invite_code_pool")
        )
        if result.scalar_one_or_none():
            print("⚠️  初始邀请码池已存在，跳过")
            return
        
        # 创建10个预设邀请码
        initial_codes = []
        invite_codes_list = []
        
        for i in range(10):
            code = generate_invite_code()
            invite_codes_list.append(code)
            initial_codes.append(
                User(
                    username=f"invite_code_{i+1}",
                    email=f"invite_{i+1}@system.internal",
                    hashed_password=get_password_hash("system_generated"),
                    nickname=f"邀请码{i+1}",
                    bio="系统预设邀请码，用于冷启动",
                    role=UserRole.USER,
                    level=1,
                    experience=0,
                    points=0,
                    total_points_earned=0,
                    invite_code=code,
                    invite_quota=50,  # 每个邀请码可以邀请50人
                    is_active=False,  # 设置为不活跃，避免被登录
                    is_verified=False,
                )
            )
        
        session.add_all(initial_codes)
        await session.commit()
        
        print("✅ 初始邀请码创建成功")
        print(f"   共创建 {len(initial_codes)} 个邀请码，每个可邀请 50 人")
        print("\n" + "=" * 60)
        print("📋 初始邀请码列表（请妥善保管）:")
        print("=" * 60)
        for i, code in enumerate(invite_codes_list, 1):
            print(f"   {i:2d}. {code}")
        print("=" * 60)
        print("\n💡 提示: 这些邀请码可以分发给早期用户进行注册")


async def main():
    """主函数"""
    print("=" * 60)
    print("AIGC散修学习平台 - 数据库初始化")
    print("=" * 60)
    print()
    
    try:
        await create_tables()
        await init_user_levels()
        await init_categories()
        await create_super_admin()
        await create_initial_invite_codes()
        
        print()
        print("=" * 60)
        print("✅ 数据库初始化完成！")
        print("=" * 60)
        print()
        print("下一步:")
        print("1. 复制 backend/.env.example 到 backend/.env")
        print("2. 修改 .env 中的数据库配置")
        print("3. 启动后端: cd backend && uvicorn app.main:app --reload")
        print("4. 使用上面的邀请码进行用户注册测试")
        print()
        
    except Exception as e:
        print(f"\n❌ 初始化失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
