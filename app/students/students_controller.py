from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.pets.pets_service import pets_service
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("")
def find_all() -> dict:
    students = students_service.find_all()
    return {
        "success": True,
        "message": "ESTUDIANTES_LISTADOS_EXITOSAMENTE",
        "data": students,
        "error": None,
        "statusCode": 200
    }


@router.get("/{student_id}")
def find_by_id(student_id: str) -> dict:
    student = students_service.find_by_id(student_id)
    return {
        "success": True,
        "message": "ESTUDIANTE_ENCONTRADO_EXITOSAMENTE",
        "data": student,
        "error": None,
        "statusCode": 200
    }


from fastapi import APIRouter

from app.pets.pets_service import pets_service
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.post("", status_code=201)
def create(body: CreateStudentDto):

    nuevo_estudiante = students_service.create(body)

    return {
        "success": True,
        "message": "ESTUDIANTE_CREADO_CORRECTAMENTE",
        "data": nuevo_estudiante,
        "error": None,
        "statusCode": 201
    }

@router.patch("/{student_id}")
def update(student_id: str, body: UpdateStudentDto) -> dict:
    updated_student = students_service.update(student_id, body)
    return {
        "success": True,
        "message": "ESTUDIANTE_ACTUALIZADO_EXITOSAMENTE",
        "data": updated_student,
        "error": None,
        "statusCode": 200
    }


@router.delete("/{student_id}")
def delete(student_id: str):
    deleted = students_service.delete(student_id)
    pets_service.delete_all_for_student(student_id)

    return {
        "success": True,
        "message": "Estudiante eliminado correctamente",
        "data": deleted,
        "error": None,
        "statusCode": 200
    }
