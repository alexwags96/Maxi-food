import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"



database = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS).maxifood

dish_collection = database.get_collection("Dishs_collection")

# helpers


def dish_helper(dish) -> dict:
    return {
        "id": str(dish["_id"]),
        "name": dish["name"],
        "description": dish["description"],
        "image": dish["image"],
        "composition": dish["composition"],
        "origin": dish["origin"],
    }

# Retrieve all dishs present in the database
async def retrieve_dishs():
    dishs = []
    async for dish in dish_collection.find():
        dishs.append(dish_helper(dish))
    return dishs


# Add a new dish into to the database
async def add_dish(dish_data: dict) -> dict:
    dish = await dish_collection.insert_one(dish_data)
    new_dish = await dish_collection.find_one({"_id": dish.inserted_id})
    return dish_helper(new_dish)


# Retrieve a dish with a matching ID
async def retrieve_dish(id: str) -> dict:
    dish = await dish_collection.find_one({"_id": ObjectId(id)})
    if dish:
        return dish_helper(dish)


# Update a dish with a matching ID
async def update_dish(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    dish = await dish_collection.find_one({"_id": ObjectId(id)})
    if dish:
        updated_dish = await dish_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_dish:
            return True
        return False


# Delete a dish from the database
async def delete_dish(id: str):
    dish = await dish_collection.find_one({"_id": ObjectId(id)})
    if dish:
        await dish_collection.delete_one({"_id": ObjectId(id)})
        return True