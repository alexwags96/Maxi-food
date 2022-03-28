from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class CredentialSchema(BaseModel):
    user_id: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    token: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "azeazdcazcee",
                "email": "wg@gmu.vom",
                "password": "fsfs",
                "token": "delevered",
            }
        }


class UpdateCredentialModel(BaseModel):
    user_id: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    date: Optional[str]
    token: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "user_id": "azeazdcazcee",
                "email": "wg@gmu.vom",
                "password": "fsfs",
                "token": "delevered",
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