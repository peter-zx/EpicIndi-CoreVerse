from fastapi import APIRouter

router = APIRouter()


@router.get("/me")
async def get_current_user():
    """获取当前用户信息"""
    return {"message": "当前用户接口"}


@router.put("/me")
async def update_current_user():
    """更新当前用户信息"""
    return {"message": "更新用户接口"}


@router.get("/me/points")
async def get_my_points():
    """获取我的积分"""
    return {"message": "我的积分接口"}


@router.get("/me/invite-code")
async def get_my_invite_code():
    """获取我的邀请码"""
    return {"message": "我的邀请码接口"}


@router.get("/me/invited-users")
async def get_my_invited_users():
    """获取我邀请的用户列表"""
    return {"message": "我邀请的用户接口"}


@router.get("/{user_id}")
async def get_user_profile(user_id: int):
    """获取用户公开信息"""
    return {"message": f"用户{user_id}信息接口"}


@router.get("/leaderboard")
async def get_leaderboard():
    """用户积分排行榜"""
    return {"message": "排行榜接口"}
