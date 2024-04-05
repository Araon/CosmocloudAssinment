from pydantic import BaseModel
from bson import ObjectId
from typing import Dict


class Address(BaseModel):
    city: str
    country: str

    class Config:
        arbitrary_types_allowed = True


class StudentCreate(BaseModel):
    name: str
    age: int
    address: Dict[str, str]


class Student(BaseModel):
    id: str
    name: str
    age: int
    address: Address

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    async def from_mongo(cls, student_dict):
        student_dict["_id"] = str(student_dict["_id"])
        student_dict["address"] = Address(**student_dict["address"])
        return cls(**student_dict)
