from fastapi import APIRouter

router = APIRouter()


@router.get("/categories")
async def get_forum_categories():
    """获取论坛分类"""
    return {"message": "论坛分类接口"}


@router.get("/posts")
async def get_posts():
    """获取帖子列表"""
    return {"message": "帖子列表接口"}


@router.post("/posts")
async def create_post():
    """发布帖子"""
    return {"message": "发布帖子接口"}


@router.get("/posts/{post_id}")
async def get_post(post_id: int):
    """获取帖子详情"""
    return {"message": f"帖子{post_id}详情接口"}


@router.put("/posts/{post_id}")
async def update_post(post_id: int):
    """更新帖子"""
    return {"message": f"更新帖子{post_id}接口"}


@router.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    """删除帖子"""
    return {"message": f"删除帖子{post_id}接口"}


@router.get("/posts/{post_id}/comments")
async def get_post_comments(post_id: int):
    """获取帖子评论"""
    return {"message": f"帖子{post_id}评论接口"}


@router.post("/posts/{post_id}/comments")
async def create_comment(post_id: int):
    """发表评论"""
    return {"message": f"帖子{post_id}发表评论接口"}


@router.post("/posts/{post_id}/like")
async def like_post(post_id: int):
    """点赞帖子"""
    return {"message": f"点赞帖子{post_id}接口"}
