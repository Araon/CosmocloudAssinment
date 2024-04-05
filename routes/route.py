from fastapi import APIRouter, HTTPException
from config.database import students_collection, async_students_collection
from models.students import Student
from schema.schema import StudentCreate, StudentUpdate
from bson import ObjectId

router = APIRouter()


@router.post("/students/", response_model=Student)
async def create_student(student: StudentCreate):
    student_dict = student.dict()
    student_dict["address"] = student_dict["address"]
    result = await async_students_collection.insert_one(student_dict)
    inserted_id = str(result.inserted_id)
    return {
        "id": inserted_id
    }
    # return Student.from_mongo({**student_dict, "_id": inserted_id})


@router.get("/students/", response_model=list[Student])
async def get_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = await async_students_collection.find(query).to_list(length=100)
    return [Student.from_mongo(student) for student in students]


@router.get("/students/{id}", response_model=Student)
async def get_student(id: str):
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return await Student.from_mongo(student)


@router.patch("/students/{id}", response_model=Student)
async def update_student(id: str, student: StudentUpdate):
    student_dict = student.dict(exclude_unset=True)
    if "address" in student_dict:
        student_dict["address"] = dict(student_dict["address"])
    result = await async_students_collection.update_one({"_id": ObjectId(id)}, {"$set": student_dict})
    if not result.matched_count:
        raise HTTPException(status_code=404, detail="Student not found")
    student = await async_students_collection.find_one({"_id": ObjectId(id)})
    return Student.from_mongo(student)


@router.delete("/students/{id}")
async def delete_student(id: str):
    result = await async_students_collection.delete_one({"_id": ObjectId(id)})
    if not result.deleted_count:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}
