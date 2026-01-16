from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_tools():
    """获取工具列表"""
    return {"message": "工具列表接口"}


@router.get("/featured")
async def get_featured_tools():
    """获取热门工具"""
    return {"message": "热门工具接口"}


@router.get("/categories")
async def get_tool_categories():
    """获取工具分类"""
    return {"message": "工具分类接口"}


@router.get("/{tool_id}")
async def get_tool(tool_id: int):
    """获取工具详情"""
    return {"message": f"工具{tool_id}详情接口"}


@router.post("/{tool_id}/unlock")
async def unlock_tool(tool_id: int):
    """解锁工具"""
    return {"message": f"解锁工具{tool_id}接口"}


@router.get("/{tool_id}/download")
async def download_tool(tool_id: int):
    """下载工具"""
    return {"message": f"下载工具{tool_id}接口"}
