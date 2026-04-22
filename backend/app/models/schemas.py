from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class User(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    username: str
    email: EmailStr
    password: Optional[str] = None
    role: str = "user"
    team: Optional[PyObjectId] = None
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Player(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    category: str
    basePrice: int
    status: str = "unsold"
    team: Optional[PyObjectId] = None
    sellingPrice: int = 0
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Team(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    owner: Optional[PyObjectId] = None
    budget: int
    players: List[PyObjectId] = []
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Auction(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    players: List[PyObjectId] = []
    currentPlayer: Optional[PyObjectId] = None
    status: str = "upcoming"
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
