from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models.content import ContentType, ContentStatus


class ContentBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    slug: Optional[str] = None
    description: Optional[str] = None
    content_type: ContentType
    body: Optional[str] = None
    video_url: Optional[str] = None
    video_source: Optional[str] = None
    cover_image: Optional[str] = None
    duration: Optional[int] = None
    category_id: Optional[int] = None
    tags: List[str] = Field(default_factory=list)
    is_free: bool = True
    required_points: int = 0
    required_level: int = 0
    status: ContentStatus = ContentStatus.DRAFT
    is_featured: bool = False
    is_pinned: bool = False


class ContentCreate(ContentBase):
    pass


class ContentUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    slug: Optional[str] = None
    description: Optional[str] = None
    body: Optional[str] = None
    video_url: Optional[str] = None
    video_source: Optional[str] = None
    cover_image: Optional[str] = None
    duration: Optional[int] = None
    category_id: Optional[int] = None
    tags: Optional[List[str]] = None
    is_free: Optional[bool] = None
    required_points: Optional[int] = None
    required_level: Optional[int] = None
    status: Optional[ContentStatus] = None
    is_featured: Optional[bool] = None
    is_pinned: Optional[bool] = None


class ContentResponse(ContentBase):
    id: int
    author_id: int
    view_count: int
    like_count: int
    comment_count: int
    share_count: int
    created_at: datetime
    updated_at: datetime
    published_at: Optional[datetime]

    class Config:
        from_attributes = True


class ContentListResponse(BaseModel):
    items: List[ContentResponse]
    total: int
    skip: int
    limit: int


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    slug: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None
    icon: Optional[str] = None
    parent_id: Optional[int] = None
    sort_order: int = 0


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    slug: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    icon: Optional[str] = None
    parent_id: Optional[int] = None
    sort_order: Optional[int] = None


class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
