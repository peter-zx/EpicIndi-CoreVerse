from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register")
async def register():
    """用户注册（需要邀请码）"""
    # TODO: 实现注册逻辑
    return {"message": "注册接口"}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """用户登录"""
    # TODO: 实现登录逻辑
    return {"message": "登录接口"}


@router.post("/logout")
async def logout():
    """用户登出"""
    return {"message": "登出接口"}


@router.post("/refresh")
async def refresh_token():
    """刷新Token"""
    return {"message": "刷新Token接口"}


@router.post("/forgot-password")
async def forgot_password():
    """忘记密码"""
    return {"message": "忘记密码接口"}


@router.post("/reset-password")
async def reset_password():
    """重置密码"""
    return {"message": "重置密码接口"}
