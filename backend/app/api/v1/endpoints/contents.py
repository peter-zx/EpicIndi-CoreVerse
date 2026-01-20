from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from typing import Optional

from app.core.database import get_db
from app.models.content import Content, ContentType, ContentStatus, Category
from app.schemas.content import ContentCreate, ContentUpdate, ContentResponse, ContentListResponse
from app.api.deps import CurrentAdmin

router = APIRouter()


# === 管理员内容管理 ===
@router.get("/admin/contents", response_model=ContentListResponse)
async def admin_get_contents(
    skip: int = 0,
    limit: int = 20,
    content_type: Optional[ContentType] = None,
    status: Optional[ContentStatus] = None,
    category_id: Optional[int] = None,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员获取内容列表"""
    query = select(Content)
    
    if content_type:
        query = query.where(Content.content_type == content_type)
    if status:
        query = query.where(Content.status == status)
    if category_id:
        query = query.where(Content.category_id == category_id)
    
    # 获取总数
    count_query = select(func.count()).select_from(Content)
    if content_type:
        count_query = count_query.where(Content.content_type == content_type)
    if status:
        count_query = count_query.where(Content.status == status)
    if category_id:
        count_query = count_query.where(Content.category_id == category_id)
    
    total_result = await db.execute(count_query)
    total = total_result.scalar()
    
    # 获取列表
    query = query.order_by(Content.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    contents = result.scalars().all()
    
    return {
        "items": contents,
        "total": total,
        "skip": skip,
        "limit": limit
    }


@router.post("/admin/contents", response_model=ContentResponse)
async def admin_create_content(
    content_data: ContentCreate,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员创建内容"""
    new_content = Content(
        **content_data.dict(),
        author_id=current_admin.id
    )
    db.add(new_content)
    await db.commit()
    await db.refresh(new_content)
    return new_content


@router.put("/admin/contents/{content_id}", response_model=ContentResponse)
async def admin_update_content(
    content_id: int,
    content_data: ContentUpdate,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员更新内容"""
    result = await db.execute(select(Content).where(Content.id == content_id))
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(status_code=404, detail="内容不存在")
    
    for key, value in content_data.dict(exclude_unset=True).items():
        setattr(content, key, value)
    
    await db.commit()
    await db.refresh(content)
    return content


@router.delete("/admin/contents/{content_id}")
async def admin_delete_content(
    content_id: int,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员删除内容"""
    result = await db.execute(select(Content).where(Content.id == content_id))
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(status_code=404, detail="内容不存在")
    
    await db.delete(content)
    await db.commit()
    return {"message": "删除成功"}


# === 公开内容接口 ===
@router.get("/videos")
async def get_videos(
    skip: int = 0,
    limit: int = 20,
    category_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    """获取视频列表"""
    query = select(Content).where(
        Content.content_type == ContentType.VIDEO,
        Content.status == ContentStatus.PUBLISHED
    )
    
    if category_id:
        query = query.where(Content.category_id == category_id)
    
    query = query.order_by(Content.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    videos = result.scalars().all()
    
    return {"items": videos, "total": len(videos)}


@router.get("/videos/{video_id}")
async def get_video(video_id: int, db: AsyncSession = Depends(get_db)):
    """获取视频详情"""
    result = await db.execute(
        select(Content).where(
            Content.id == video_id,
            Content.content_type == ContentType.VIDEO
        )
    )
    video = result.scalar_one_or_none()
    
    if not video:
        raise HTTPException(status_code=404, detail="视频不存在")
    
    # 增加浏览次数
    video.view_count += 1
    await db.commit()
    
    return video


@router.get("/articles")
async def get_articles(
    skip: int = 0,
    limit: int = 20,
    category_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    """获取图文列表"""
    query = select(Content).where(
        Content.content_type == ContentType.ARTICLE,
        Content.status == ContentStatus.PUBLISHED
    )
    
    if category_id:
        query = query.where(Content.category_id == category_id)
    
    query = query.order_by(Content.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    articles = result.scalars().all()
    
    return {"items": articles, "total": len(articles)}


@router.get("/articles/{article_id}")
async def get_article(article_id: int, db: AsyncSession = Depends(get_db)):
    """获取图文详情"""
    result = await db.execute(
        select(Content).where(
            Content.id == article_id,
            Content.content_type == ContentType.ARTICLE
        )
    )
    article = result.scalar_one_or_none()
    
    if not article:
        raise HTTPException(status_code=404, detail="文章不存在")
    
    article.view_count += 1
    await db.commit()
    
    return article


@router.get("/podcasts")
async def get_podcasts(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db)
):
    """获取播客列表"""
    query = select(Content).where(
        Content.content_type == ContentType.PODCAST,
        Content.status == ContentStatus.PUBLISHED
    ).order_by(Content.created_at.desc()).offset(skip).limit(limit)
    
    result = await db.execute(query)
    podcasts = result.scalars().all()
    
    return {"items": podcasts, "total": len(podcasts)}


@router.get("/podcasts/{podcast_id}")
async def get_podcast(podcast_id: int, db: AsyncSession = Depends(get_db)):
    """获取播客详情"""
    result = await db.execute(
        select(Content).where(
            Content.id == podcast_id,
            Content.content_type == ContentType.PODCAST
        )
    )
    podcast = result.scalar_one_or_none()
    
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")
    
    podcast.view_count += 1
    await db.commit()
    
    return podcast


@router.get("/categories")
async def get_categories(db: AsyncSession = Depends(get_db)):
    """获取内容分类"""
    result = await db.execute(
        select(Category).order_by(Category.sort_order)
    )
    categories = result.scalars().all()
    return {"items": categories}


@router.post("/{content_id}/like")
async def like_content(content_id: int, db: AsyncSession = Depends(get_db)):
    """点赞内容"""
    result = await db.execute(select(Content).where(Content.id == content_id))
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(status_code=404, detail="内容不存在")
    
    content.like_count += 1
    await db.commit()
    
    return {"message": "点赞成功", "like_count": content.like_count}
