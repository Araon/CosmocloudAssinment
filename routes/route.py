from fastapi import APIRouter, HTTPException
from config.database import async_students_collection
from models.students import Student
from schema.schema import StudentCreate, StudentUpdate
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def welcome():
    return {
        "GET /docs": "For swagger documentaion"
    }


@router.post("/students/")
async def create_student(student: StudentCreate):
    response = {}
    student_dict = student.dict()
    student_dict["address"] = student_dict["address"]
    result = await async_students_collection.insert_one(student_dict)
    inserted_id = str(result.inserted_id)
    response["id"] = inserted_id
    return response


@router.get("/students/", response_model=dict)
async def get_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = await async_students_collection.find(query).to_list(length=100)
    student_models = [await Student.from_mongo(student) for student in students]
    student_data = [{"name": student.name, "age": student.age} for student in student_models]
    return {"data": student_data}


@router.get("/students/{id}", response_model=dict)
async def get_student(id: str):
    student = await async_students_collection.find_one({"_id": ObjectId(id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student_obj = await Student.from_mongo(student)
    student_dict = student_obj.dict()
    student_dict.pop('id', None)
    return student_dict


@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: StudentUpdate):
    student_dict = student.dict(exclude_unset=True)
    if "address" in student_dict:
        student_dict["address"] = dict(student_dict["address"])
    result = await async_students_collection.update_one({"_id": ObjectId(id)}, {"$set": student_dict})
    if not result.matched_count:
        raise HTTPException(status_code=404, detail="Student not found")


@router.delete("/students/{id}")
async def delete_student(id: str):
    result = await async_students_collection.delete_one({"_id": ObjectId(id)})
    if not result.deleted_count:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}
