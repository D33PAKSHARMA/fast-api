
from fastapi import APIRouter
from config.database import db
from models.pizzas import Pizza
from utils.getValue import *
from bson import ObjectId

router = APIRouter(prefix='/pizzas')

@router.get("/")
async def getAllPizzas():
    pizzas = list_values(db.newproducts.find())
    print(pizzas)
    return pizzas

@router.get("/{id}")
async def getPizzaById(id: str):
    pizza = get_single_value(db.newproducts.find_one({"_id": ObjectId(id)}))

    if not pizza:
        return {"success": False, "msg": "Product not found"}
    else: 
        return {"success": True, "msg": "Sucessfully retrieved" , "data": pizza}