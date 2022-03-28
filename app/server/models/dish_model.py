from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class DishSchema(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    image: str = Field(...)
    composition: str = Field(...)
    origin: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "thiep",
                "description": "riz au poisson",
                "image": "lien",
                "composition": "riz poisson legume",
                "origin": "Senegal",
            }
        }


class UpdateDishModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    image: Optional[str]
    composition: Optional[str]
    origin: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                 "name": "thiep",
                "description": "riz au poisson",
                "image": "lien",
                "composition": "riz poisson legume",
                "origin": "Senegal",
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