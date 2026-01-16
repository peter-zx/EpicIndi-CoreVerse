from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_homeworks():
    """获取作业列表"""
    return {"message": "作业列表接口"}


@router.get("/{homework_id}")
async def get_homework(homework_id: int):
    """获取作业详情"""
    return {"message": f"作业{homework_id}详情接口"}


@router.post("/{homework_id}/submit")
async def submit_homework(homework_id: int):
    """提交作业"""
    return {"message": f"提交作业{homework_id}接口"}


@router.get("/{homework_id}/submissions")
async def get_submissions(homework_id: int):
    """获取作业提交列表（管理员/高级用户）"""
    return {"message": f"作业{homework_id}提交列表接口"}


@router.get("/submissions/{submission_id}")
async def get_submission(submission_id: int):
    """获取提交详情"""
    return {"message": f"提交{submission_id}详情接口"}


@router.post("/submissions/{submission_id}/review")
async def review_submission(submission_id: int):
    """批阅作业"""
    return {"message": f"批阅提交{submission_id}接口"}


@router.get("/my/submissions")
async def get_my_submissions():
    """获取我的作业提交"""
    return {"message": "我的作业提交接口"}
