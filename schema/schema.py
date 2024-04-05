from pydantic import BaseModel


class Address(BaseModel):
    city: str
    country: str


class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address


class StudentUpdate(BaseModel):
    name: str = None
    age: int = None
    address: Address = None
