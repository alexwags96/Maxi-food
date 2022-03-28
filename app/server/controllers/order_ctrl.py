import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"



database = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS).maxifood

order_collection = database.get_collection("Orders_collection")

# helpers


def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "client_id": order["client_id"],
        "dish": order["dish"],
        "date": order["date"],
        "status": order["status"],
    }

# Retrieve all orders present in the database
async def retrieve_orders():
    orders = []
    async for order in order_collection.find():
        orders.append(order_helper(order))
    return orders


# Add a new order into to the database
async def add_order(order_data: dict) -> dict:
    order = await order_collection.insert_one(order_data)
    new_order = await order_collection.find_one({"_id": order.inserted_id})
    return order_helper(new_order)


# Retrieve a order with a matching ID
async def retrieve_order(id: str) -> dict:
    order = await order_collection.find_one({"_id": ObjectId(id)})
    if order:
        return order_helper(order)


# Update a order with a matching ID
async def update_order(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    order = await order_collection.find_one({"_id": ObjectId(id)})
    if order:
        updated_order = await order_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_order:
            return True
        return False


# Delete a order from the database
async def delete_order(id: str):
    order = await order_collection.find_one({"_id": ObjectId(id)})
    if order:
        await order_collection.delete_one({"_id": ObjectId(id)})
        return True