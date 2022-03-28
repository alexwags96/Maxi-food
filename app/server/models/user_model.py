from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(...)
    fuction: str = Field(...)
   

    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "fuction": "cooker",
            
            }
        }


class UpdateUserModel(BaseModel):
    firstName: Optional[str]
    lastName: Optional[EmailStr]
    fuction: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "firstName": "John ",
                "lastName": "Doe",
                "fuction": "cooker",
                
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}