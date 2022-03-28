from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.controllers.credential_ctrl import (
    add_credential,
    delete_credential,
    retrieve_credential,
    retrieve_credentials,
    update_credential,
)
from app.server.models.credential_model import (
    ErrorResponseModel,
    ResponseModel,
    CredentialSchema,
    UpdateCredentialModel,
)

router = APIRouter()

@router.post("/", response_description="Credential data added into the database")
async def add_credential_data(credential: CredentialSchema = Body(...)):
    credential = jsonable_encoder(credential)
    new_credential = await add_credential(credential)
    return ResponseModel(new_credential, "Credential added successfully.")

@router.get("/", response_description="Credentials retrieved")
async def get_credentials():
    credentials = await retrieve_credentials()
    if credentials:
        return ResponseModel(credentials, "Credentials data retrieved successfully")
    return ResponseModel(credentials, "Empty list returned")


@router.get("/{id}", response_description="Credential data retrieved")
async def get_credential_data(id):
    credential = await retrieve_credential(id)
    if credential:
        return ResponseModel(credential, "Credential data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Credential doesn't exist.")

@router.put("/{id}")
async def update_credential_data(id: str, req: UpdateCredentialModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_credential = await update_credential(id, req)
    if updated_credential:
        return ResponseModel(
            "Credential with ID: {} name update is successful".format(id),
            "Credential name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the credential data.",
    )

@router.delete("/{id}", response_description="Credential data deleted from the database")
async def delete_credential_data(id: str):
    deleted_credential = await delete_credential(id)
    if deleted_credential:
        return ResponseModel(
            "Credential with ID: {} removed".format(id), "Credential deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Credential with id {0} doesn't exist".format(id)
    )