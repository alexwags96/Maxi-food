import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"



database = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS).maxifood

client_collection = database.get_collection("Clients_collection")

# helpers


def client_helper(client) -> dict:
    return {
        "id": str(client["_id"]),
        "firstName": client["firstName"],
        "lastName": client["lastName"],
        "address": client["address"],
    }

# Retrieve all clients present in the database
async def retrieve_clients():
    clients = []
    async for client in client_collection.find():
        clients.append(client_helper(client))
    return clients


# Add a new client into to the database
async def add_client(client_data: dict) -> dict:
    client = await client_collection.insert_one(client_data)
    new_client = await client_collection.find_one({"_id": client.inserted_id})
    return client_helper(new_client)


# Retrieve a client with a matching ID
async def retrieve_client(id: str) -> dict:
    client = await client_collection.find_one({"_id": ObjectId(id)})
    if client:
        return client_helper(client)


# Update a client with a matching ID
async def update_client(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    client = await client_collection.find_one({"_id": ObjectId(id)})
    if client:
        updated_client = await client_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_client:
            return True
        return False


# Delete a client from the database
async def delete_client(id: str):
    client = await client_collection.find_one({"_id": ObjectId(id)})
    if client:
        await client_collection.delete_one({"_id": ObjectId(id)})
        return True