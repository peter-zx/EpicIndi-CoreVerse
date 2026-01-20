from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from typing import Optional

from app.core.database import get_db
from app.models.homework import Homework, HomeworkSubmission, HomeworkReview, HomeworkStatus, SubmissionStatus
from app.api.deps import CurrentUser, CurrentAdmin
from datetime import datetime

router = APIRouter()


# === 管理员作业管理 ===
@router.get("/admin/homeworks")
async def admin_get_homeworks(
    skip: int = 0,
    limit: int = 20,
    status: Optional[HomeworkStatus] = None,
    category_id: Optional[int] = None,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员获取作业列表"""
    query = select(Homework)
    
    if status:
        query = query.where(Homework.status == status)
    if category_id:
        query = query.where(Homework.category_id == category_id)
    
    # 获取总数
    count_query = select(func.count()).select_from(Homework)
    if status:
        count_query = count_query.where(Homework.status == status)
    if category_id:
        count_query = count_query.where(Homework.category_id == category_id)
    
    total_result = await db.execute(count_query)
    total = total_result.scalar()
    
    # 获取列表
    query = query.order_by(Homework.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    homeworks = result.scalars().all()
    
    return {"items": homeworks, "total": total}


@router.post("/admin/homeworks")
async def admin_create_homework(
    title: str,
    description: str,
    requirements: Optional[str] = None,
    category_id: Optional[int] = None,
    base_points: int = 30,
    deadline: Optional[datetime] = None,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员创建作业"""
    new_homework = Homework(
        title=title,
        description=description,
        requirements=requirements,
        category_id=category_id,
        base_points=base_points,
        deadline=deadline,
        publisher_id=current_admin.id,
        status=HomeworkStatus.PUBLISHED
    )
    
    db.add(new_homework)
    await db.commit()
    await db.refresh(new_homework)
    
    return {"message": "作业创建成功", "data": new_homework}


@router.put("/admin/homeworks/{homework_id}")
async def admin_update_homework(
    homework_id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    requirements: Optional[str] = None,
    status: Optional[HomeworkStatus] = None,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员更新作业"""
    result = await db.execute(select(Homework).where(Homework.id == homework_id))
    homework = result.scalar_one_or_none()
    
    if not homework:
        raise HTTPException(status_code=404, detail="作业不存在")
    
    if title:
        homework.title = title
    if description:
        homework.description = description
    if requirements:
        homework.requirements = requirements
    if status:
        homework.status = status
    
    await db.commit()
    await db.refresh(homework)
    
    return {"message": "更新成功", "data": homework}


@router.delete("/admin/homeworks/{homework_id}")
async def admin_delete_homework(
    homework_id: int,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员删除作业"""
    result = await db.execute(select(Homework).where(Homework.id == homework_id))
    homework = result.scalar_one_or_none()
    
    if not homework:
        raise HTTPException(status_code=404, detail="作业不存在")
    
    await db.delete(homework)
    await db.commit()
    
    return {"message": "删除成功"}


@router.get("/admin/submissions")
async def admin_get_submissions(
    skip: int = 0,
    limit: int = 20,
    homework_id: Optional[int] = None,
    status: Optional[SubmissionStatus] = None,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员获取作业提交列表"""
    query = select(HomeworkSubmission)
    
    if homework_id:
        query = query.where(HomeworkSubmission.homework_id == homework_id)
    if status:
        query = query.where(HomeworkSubmission.status == status)
    
    query = query.order_by(HomeworkSubmission.submitted_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    submissions = result.scalars().all()
    
    return {"items": submissions}


@router.post("/admin/submissions/{submission_id}/review")
async def admin_review_submission(
    submission_id: int,
    score: int,
    comment: str,
    is_excellent: bool = False,
    current_admin: CurrentAdmin = None,
    db: AsyncSession = Depends(get_db)
):
    """管理员批阅作业"""
    result = await db.execute(
        select(HomeworkSubmission).where(HomeworkSubmission.id == submission_id)
    )
    submission = result.scalar_one_or_none()
    
    if not submission:
        raise HTTPException(status_code=404, detail="提交不存在")
    
    # 创建批阅记录
    review = HomeworkReview(
        submission_id=submission_id,
        reviewer_id=current_admin.id,
        score=score,
        comment=comment,
        is_excellent=is_excellent
    )
    
    db.add(review)
    
    # 更新提交状态
    submission.status = SubmissionStatus.REVIEWED
    
    # 获取作业信息计算积分
    homework_result = await db.execute(
        select(Homework).where(Homework.id == submission.homework_id)
    )
    homework = homework_result.scalar_one()
    
    # 计算获得积分
    points = homework.base_points
    if is_excellent:
        points += homework.excellent_points
    
    submission.points_earned = points
    
    await db.commit()
    
    return {"message": "批阅成功", "points_earned": points}


# === 公开作业接口 ===
@router.get("/")
async def get_homeworks(
    skip: int = 0,
    limit: int = 20,
    category_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    """获取作业列表"""
    query = select(Homework).where(Homework.status == HomeworkStatus.PUBLISHED)
    
    if category_id:
        query = query.where(Homework.category_id == category_id)
    
    query = query.order_by(Homework.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    homeworks = result.scalars().all()
    
    return {"items": homeworks}


@router.get("/{homework_id}")
async def get_homework(homework_id: int, db: AsyncSession = Depends(get_db)):
    """获取作业详情"""
    result = await db.execute(select(Homework).where(Homework.id == homework_id))
    homework = result.scalar_one_or_none()
    
    if not homework:
        raise HTTPException(status_code=404, detail="作业不存在")
    
    return homework


@router.post("/{homework_id}/submit")
async def submit_homework(
    homework_id: int,
    content: str,
    current_user: CurrentUser = None,
    db: AsyncSession = Depends(get_db)
):
    """提交作业"""
    # 检查作业是否存在
    homework_result = await db.execute(select(Homework).where(Homework.id == homework_id))
    homework = homework_result.scalar_one_or_none()
    
    if not homework:
        raise HTTPException(status_code=404, detail="作业不存在")
    
    # 检查是否已提交
    existing_result = await db.execute(
        select(HomeworkSubmission).where(
            HomeworkSubmission.homework_id == homework_id,
            HomeworkSubmission.student_id == current_user.id
        )
    )
    existing = existing_result.scalar_one_or_none()
    
    if existing:
        raise HTTPException(status_code=400, detail="已提交过该作业")
    
    # 创建提交
    submission = HomeworkSubmission(
        homework_id=homework_id,
        student_id=current_user.id,
        content=content,
        status=SubmissionStatus.PENDING
    )
    
    db.add(submission)
    homework.submission_count += 1
    await db.commit()
    
    return {"message": "提交成功"}


@router.get("/my/submissions")
async def get_my_submissions(
    current_user: CurrentUser = None,
    db: AsyncSession = Depends(get_db)
):
    """获取我的作业提交"""
    result = await db.execute(
        select(HomeworkSubmission)
        .where(HomeworkSubmission.student_id == current_user.id)
        .order_by(HomeworkSubmission.submitted_at.desc())
    )
    submissions = result.scalars().all()
    
    return {"items": submissions}
