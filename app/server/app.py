from fastapi import FastAPI
from app.server.routes.client_route import router as ClientRouter
from app.server.routes.user_route import router as UserRouter
from app.server.routes.dish_route import router as DishRouter
from app.server.routes.order_route import router as OrderRouter
from app.server.routes.credential_route import router as CredentialRouter

app = FastAPI()

app.include_router(ClientRouter, tags=["Client"], prefix="/client")
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(DishRouter, tags=["Dish"], prefix="/dish")
app.include_router(OrderRouter, tags=["Order"], prefix="/order")
app.include_router(CredentialRouter, tags=["credential"], prefix="/credential")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to maxi food back-end api!"}
