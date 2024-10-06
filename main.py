from fastapi import FastAPI
from routes.pizza_routes import router as pizza_routes
from routes.auth_routes import router as auth_routes

app = FastAPI()

app.include_router(pizza_routes)
app.include_router(auth_routes)