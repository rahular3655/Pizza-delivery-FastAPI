from fastapi import FastAPI 
from typing import Union
from pydantic import BaseModel
from auth_router import * 
from order_router import * 

app =FastAPI()

app.include_router(auth_router)
app.include_router(order_router) 