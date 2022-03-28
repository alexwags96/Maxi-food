from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.controllers.order_ctrl import (
    add_order,
    delete_order,
    retrieve_order,
    retrieve_orders,
    update_order,
)
from app.server.models.order_model import (
    ErrorResponseModel,
    ResponseModel,
    OrderSchema,
    UpdateOrderModel,
)

router = APIRouter()

@router.post("/", response_description="Order data added into the database")
async def add_order_data(order: OrderSchema = Body(...)):
    order = jsonable_encoder(order)
    new_order = await add_order(order)
    return ResponseModel(new_order, "Order added successfully.")

@router.get("/", response_description="Orders retrieved")
async def get_orders():
    orders = await retrieve_orders()
    if orders:
        return ResponseModel(orders, "Orders data retrieved successfully")
    return ResponseModel(orders, "Empty list returned")


@router.get("/{id}", response_description="Order data retrieved")
async def get_order_data(id):
    order = await retrieve_order(id)
    if order:
        return ResponseModel(order, "Order data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Order doesn't exist.")

@router.put("/{id}")
async def update_order_data(id: str, req: UpdateOrderModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_order = await update_order(id, req)
    if updated_order:
        return ResponseModel(
            "Order with ID: {} name update is successful".format(id),
            "Order name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the order data.",
    )

@router.delete("/{id}", response_description="Order data deleted from the database")
async def delete_order_data(id: str):
    deleted_order = await delete_order(id)
    if deleted_order:
        return ResponseModel(
            "Order with ID: {} removed".format(id), "Order deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Order with id {0} doesn't exist".format(id)
    )