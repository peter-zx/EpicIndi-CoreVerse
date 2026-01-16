from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_tasks():
    """获取悬赏任务列表"""
    return {"message": "任务列表接口"}


@router.get("/open")
async def get_open_tasks():
    """获取待揭榜任务"""
    return {"message": "待揭榜任务接口"}


@router.post("/")
async def create_task():
    """发布悬赏任务"""
    return {"message": "发布任务接口"}


@router.get("/{task_id}")
async def get_task(task_id: int):
    """获取任务详情"""
    return {"message": f"任务{task_id}详情接口"}


@router.post("/{task_id}/apply")
async def apply_task(task_id: int):
    """申请接取任务"""
    return {"message": f"申请任务{task_id}接口"}


@router.post("/{task_id}/accept/{applicant_id}")
async def accept_applicant(task_id: int, applicant_id: int):
    """接受申请者"""
    return {"message": f"接受任务{task_id}申请者{applicant_id}接口"}


@router.post("/{task_id}/complete")
async def complete_task(task_id: int):
    """完成任务"""
    return {"message": f"完成任务{task_id}接口"}


@router.get("/my/published")
async def get_my_published_tasks():
    """我发布的任务"""
    return {"message": "我发布的任务接口"}


@router.get("/my/accepted")
async def get_my_accepted_tasks():
    """我接取的任务"""
    return {"message": "我接取的任务接口"}
