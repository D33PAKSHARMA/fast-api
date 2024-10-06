from pydantic import BaseModel
from bson import ObjectId


class Image(BaseModel):
    url: str

class Pizza(BaseModel):
    name: str
    price: int
    size: str
    image: Image

    class Config:
        # Allow Pydantic to convert MongoDB ObjectId to str
        json_encoders = {ObjectId: str}