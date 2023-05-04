from fastapi import APIRouter 

order_router = APIRouter(
    prefix='/auth'
) 

@order_router.get('/')
async def hello():
    return {"message":"hello world"}