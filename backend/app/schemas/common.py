from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class ResponseBase(BaseModel):
    """基础响应"""
    code: int = 200
    message: str = "success"


class ResponseData(ResponseBase, Generic[T]):
    """带数据的响应"""
    data: Optional[T] = None


class ResponseList(ResponseBase, Generic[T]):
    """列表响应"""
    data: List[T] = []
    total: int = 0
    page: int = 1
    page_size: int = 20


class ErrorResponse(BaseModel):
    """错误响应"""
    code: int
    message: str
    detail: Optional[str] = None
