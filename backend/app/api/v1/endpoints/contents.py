from fastapi import APIRouter

router = APIRouter()


# === 视频 ===
@router.get("/videos")
async def get_videos():
    """获取视频列表"""
    return {"message": "视频列表接口"}


@router.get("/videos/{video_id}")
async def get_video(video_id: int):
    """获取视频详情"""
    return {"message": f"视频{video_id}详情接口"}


@router.get("/videos/featured")
async def get_featured_videos():
    """获取热门/精选视频"""
    return {"message": "热门视频接口"}


# === 图文 ===
@router.get("/articles")
async def get_articles():
    """获取图文列表"""
    return {"message": "图文列表接口"}


@router.get("/articles/{article_id}")
async def get_article(article_id: int):
    """获取图文详情"""
    return {"message": f"图文{article_id}详情接口"}


# === 播客 ===
@router.get("/podcasts")
async def get_podcasts():
    """获取播客列表"""
    return {"message": "播客列表接口"}


@router.get("/podcasts/{podcast_id}")
async def get_podcast(podcast_id: int):
    """获取播客详情"""
    return {"message": f"播客{podcast_id}详情接口"}


# === 通用 ===
@router.get("/categories")
async def get_categories():
    """获取内容分类"""
    return {"message": "分类列表接口"}


@router.post("/{content_id}/unlock")
async def unlock_content(content_id: int):
    """解锁付费内容"""
    return {"message": f"解锁内容{content_id}接口"}


@router.post("/{content_id}/like")
async def like_content(content_id: int):
    """点赞内容"""
    return {"message": f"点赞内容{content_id}接口"}
