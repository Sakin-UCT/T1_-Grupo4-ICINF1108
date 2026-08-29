from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str) -> list[Pet]:
    return pets_service.find_all_for_student(studentId)


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto):
    created = pets_service.create(studentId, body)

    return {
        "success": True,
        "message": "Mascota creada correctamente",
        "data": created,
        "error": None,
        "statusCode": 201
    }


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto):
    updated = pets_service.update(studentId, petId, body)

    return {
        "success": True,
        "Message": "Mascota actualizada correctamente",
        "data": updated,
        "error": None,
        "statusCode": 200
    }




@router.delete("/{petId}")
def delete(studentId: str, petId: str):
    deleted = pets_service.delete(studentId, petId)

    return {
        "success": True,
        "message": "Mascota eliminada correctamente",
        "data": deleted,
        "error": None,
        "statusCode": 200
    }
