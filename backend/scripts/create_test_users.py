"""
创建额外的测试用户

用法:
    python scripts/create_test_users.py
"""
import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import AsyncSessionLocal
from app.core.security import get_password_hash
from app.models.user import User, UserRole
from app.services.user import UserService, generate_invite_code


async def create_test_users():
    """创建测试用户"""
    async with AsyncSessionLocal() as session:
        user_service = UserService(session)
        
        # 获取管理员邀请码
        admin = await user_service.get_by_username("admin")
        if not admin:
            print("❌ 请先运行 init_db.py 创建管理员")
            return
        
        print(f"使用管理员邀请码: {admin.invite_code}")
        print()
        
        # 测试用户列表
        test_users = [
            {
                "username": "testuser1",
                "email": "test1@example.com",
                "password": "test123456",
                "nickname": "测试用户1",
                "bio": "我是测试用户1",
            },
            {
                "username": "testuser2",
                "email": "test2@example.com",
                "password": "test123456",
                "nickname": "测试用户2",
                "bio": "我是测试用户2",
            },
            {
                "username": "senior1",
                "email": "senior1@example.com",
                "password": "test123456",
                "nickname": "高级用户",
                "bio": "我是高级用户，可以批阅作业",
                "role": UserRole.SENIOR,
            },
        ]
        
        for user_data in test_users:
            # 检查用户是否已存在
            existing = await user_service.get_by_username(user_data["username"])
            if existing:
                print(f"⚠️  用户 {user_data['username']} 已存在，跳过")
                continue
            
            # 创建用户
            user = User(
                username=user_data["username"],
                email=user_data["email"],
                hashed_password=get_password_hash(user_data["password"]),
                nickname=user_data.get("nickname", user_data["username"]),
                bio=user_data.get("bio"),
                role=user_data.get("role", UserRole.USER),
                level=user_data.get("level", 1),
                points=100,
                total_points_earned=100,
                invite_code=generate_invite_code(),
                invite_quota=5,
                invited_by_id=admin.id,
                is_active=True,
            )
            
            session.add(user)
            await session.flush()
            
            print(f"✅ 创建用户: {user.username}")
            print(f"   邮箱: {user.email}")
            print(f"   密码: {user_data['password']}")
            print(f"   邀请码: {user.invite_code}")
            print()
        
        await session.commit()
        print("✅ 测试用户创建完成")


if __name__ == "__main__":
    asyncio.run(create_test_users())
