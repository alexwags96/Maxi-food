from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.controllers.dish_ctrl import (
    add_dish,
    delete_dish,
    retrieve_dish,
    retrieve_dishs,
    update_dish,
)
from app.server.models.dish_model import (
    ErrorResponseModel,
    ResponseModel,
    DishSchema,
    UpdateDishModel,
)

router = APIRouter()

@router.post("/", response_description="Dish data added into the database")
async def add_dish_data(dish: DishSchema = Body(...)):
    dish = jsonable_encoder(dish)
    new_dish = await add_dish(dish)
    return ResponseModel(new_dish, "Dish added successfully.")

@router.get("/", response_description="Dishs retrieved")
async def get_dishs():
    dishs = await retrieve_dishs()
    if dishs:
        return ResponseModel(dishs, "Dishs data retrieved successfully")
    return ResponseModel(dishs, "Empty list returned")


@router.get("/{id}", response_description="Dish data retrieved")
async def get_dish_data(id):
    dish = await retrieve_dish(id)
    if dish:
        return ResponseModel(dish, "Dish data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Dish doesn't exist.")

@router.put("/{id}")
async def update_dish_data(id: str, req: UpdateDishModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_dish = await update_dish(id, req)
    if updated_dish:
        return ResponseModel(
            "Dish with ID: {} name update is successful".format(id),
            "Dish name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the dish data.",
    )

@router.delete("/{id}", response_description="Dish data deleted from the database")
async def delete_dish_data(id: str):
    deleted_dish = await delete_dish(id)
    if deleted_dish:
        return ResponseModel(
            "Dish with ID: {} removed".format(id), "Dish deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Dish with id {0} doesn't exist".format(id)
    )