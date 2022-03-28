from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class OrderSchema(BaseModel):
    client_id: str = Field(...)
    dish: str = Field(...)
    date: str = Field(...)
    status: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "client_id": "azeazdcazcee",
                "dish": "riz au poisson",
                "date": "10/02/2022",
                "status": "delevered",
            }
        }


class UpdateOrderModel(BaseModel):
    client_id: Optional[str]
    dish: Optional[str]
    date: Optional[str]
    status: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "client_id": "azeazdcazcee",
                "dish": "riz au poisson",
                "date": "10/02/2022",
                "status": "delevered",
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