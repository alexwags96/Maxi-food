from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.controllers.client_ctrl import (
    add_client,
    delete_client,
    retrieve_client,
    retrieve_clients,
    update_client,
)
from app.server.models.client_model import (
    ErrorResponseModel,
    ResponseModel,
    ClientSchema,
    UpdateClientModel,
)

router = APIRouter()

@router.post("/", response_description="Client data added into the database")
async def add_client_data(client: ClientSchema = Body(...)):
    client = jsonable_encoder(client)
    new_client = await add_client(client)
    return ResponseModel(new_client, "Client added successfully.")

@router.get("/", response_description="Clients retrieved")
async def get_clients():
    clients = await retrieve_clients()
    if clients:
        return ResponseModel(clients, "Clients data retrieved successfully")
    return ResponseModel(clients, "Empty list returned")


@router.get("/{id}", response_description="Client data retrieved")
async def get_client_data(id):
    client = await retrieve_client(id)
    if client:
        return ResponseModel(client, "Client data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Client doesn't exist.")

@router.put("/{id}")
async def update_client_data(id: str, req: UpdateClientModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_client = await update_client(id, req)
    if updated_client:
        return ResponseModel(
            "Client with ID: {} name update is successful".format(id),
            "Client name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the client data.",
    )

@router.delete("/{id}", response_description="Client data deleted from the database")
async def delete_client_data(id: str):
    deleted_client = await delete_client(id)
    if deleted_client:
        return ResponseModel(
            "Client with ID: {} removed".format(id), "Client deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Client with id {0} doesn't exist".format(id)
    )