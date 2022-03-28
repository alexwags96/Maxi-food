from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ClientSchema(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(...)
    address: str = Field(...)
   

    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "address": "5 street St Marth ",
               
            }
        }


class UpdateClientModel(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    address: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "address": "5 street St Marth ",
                
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