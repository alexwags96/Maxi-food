import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"



database = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS).maxifood

credential_collection = database.get_collection("Credentials_collection")

# helpers


def credential_helper(credential) -> dict:
    return {
        "id": str(credential["_id"]),
        "user_id": credential["user_id"],
        "email": credential["email"],
        "password": credential["password"],
        "token": credential["token"],
    }

# Retrieve all credentials present in the database
async def retrieve_credentials():
    credentials = []
    async for credential in credential_collection.find():
        credentials.append(credential_helper(credential))
    return credentials


# Add a new credential into to the database
async def add_credential(credential_data: dict) -> dict:
    credential = await credential_collection.insert_one(credential_data)
    new_credential = await credential_collection.find_one({"_id": credential.inserted_id})
    return credential_helper(new_credential)


# Retrieve a credential with a matching ID
async def retrieve_credential(id: str) -> dict:
    credential = await credential_collection.find_one({"_id": ObjectId(id)})
    if credential:
        return credential_helper(credential)


# Update a credential with a matching ID
async def update_credential(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    credential = await credential_collection.find_one({"_id": ObjectId(id)})
    if credential:
        updated_credential = await credential_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_credential:
            return True
        return False


# Delete a credential from the database
async def delete_credential(id: str):
    credential = await credential_collection.find_one({"_id": ObjectId(id)})
    if credential:
        await credential_collection.delete_one({"_id": ObjectId(id)})
        return True