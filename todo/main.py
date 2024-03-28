from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import uvicorn

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str

students=[1,2,3,4,5,]
print(students[0])
students: Dict[int, Student] = {}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@app.post("/students")
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400, detail="Student already exists")
    students[student.id] = student
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student has been deleted successfully"}



def start():
    uvicorn.run("todo.main:app",host="127.0.0.1", port=8080, reload=True)