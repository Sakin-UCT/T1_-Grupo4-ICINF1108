from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("/{student_id}/pets")
def list_pets(student_id: str) -> dict:
    pets = pets_service.list_by_student(student_id)
    return {
        "success": True,
        "message": "MASCOTAS_OBTENIDAS_EXITOSAMENTE",
        "data": pets,
        "error": None,
        "statusCode": 200
    }


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto) -> Pet:
    return pets_service.create(studentId, body)


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto) -> Pet:
    return pets_service.update(studentId, petId, body)


@router.delete("/{petId}")
def delete(studentId: str, petId: str) -> Pet:
    return pets_service.delete(studentId, petId)

