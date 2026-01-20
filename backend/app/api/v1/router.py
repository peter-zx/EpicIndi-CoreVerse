from fastapi import APIRouter

from app.api.v1.endpoints import auth, users, contents, forum, tools, homework, tasks, points, admin

api_router = APIRouter()

# 认证相关
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])

# 用户相关
api_router.include_router(users.router, prefix="/users", tags=["用户"])

# 内容相关（视频、图文、播客）
api_router.include_router(contents.router, prefix="/contents", tags=["内容"])

# 论坛相关
api_router.include_router(forum.router, prefix="/forum", tags=["论坛"])

# 工具箱
api_router.include_router(tools.router, prefix="/tools", tags=["工具箱"])

# 作业系统
api_router.include_router(homework.router, prefix="/homework", tags=["作业系统"])

# 悬赏任务
api_router.include_router(tasks.router, prefix="/tasks", tags=["悬赏任务"])

# 积分系统
api_router.include_router(points.router, prefix="/points", tags=["积分系统"])

# 管理后台
api_router.include_router(admin.router, prefix="/admin", tags=["管理后台"])
