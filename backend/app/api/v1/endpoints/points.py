from fastapi import APIRouter

router = APIRouter()


@router.get("/balance")
async def get_points_balance():
    """获取积分余额"""
    return {"message": "积分余额接口"}


@router.get("/records")
async def get_points_records():
    """获取积分明细"""
    return {"message": "积分明细接口"}


@router.get("/packages")
async def get_recharge_packages():
    """获取充值套餐"""
    return {"message": "充值套餐接口"}


@router.post("/recharge")
async def create_recharge_order():
    """创建充值订单"""
    return {"message": "创建充值订单接口"}


@router.post("/recharge/alipay/callback")
async def alipay_callback():
    """支付宝回调"""
    return {"message": "支付宝回调接口"}


@router.post("/recharge/wechat/callback")
async def wechat_callback():
    """微信支付回调"""
    return {"message": "微信支付回调接口"}


@router.get("/recharge/status/{order_no}")
async def get_order_status(order_no: str):
    """查询订单状态"""
    return {"message": f"订单{order_no}状态接口"}
