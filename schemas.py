from pydantic import BaseModel 
from typing import Optional

class SignupModel(BaseModel):
    id :Optional[int]
    username:str
    email: str
    password:str
    is_staff : Optional[bool]
    is_active :Optional[bool]
    
    
    class Config:
        orm_mode=True 
        schema_extra={
            'example':{
                "username":"johndoe",
                "email":"email@gmail.com",
                "password":"password",
                "is_staff":True,
                "is_active":True,
                
            }
        }
        
# class Settings(BaseModel):
#     authjwt_secret_key:str=