from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.pets.pets_controller import router as pets_router
from app.students.students_controller import router as students_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI CRUD Students & Pets",
        description="API de un CRUD en memoria para la entidad Student y sus mascotas (Pet)",
        version="1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(HTTPException)
    def exception_http(request: Request, error: HTTPException):
        return JSONResponse(
            status_code=error.status_code,
            content={
                "success": False,
                "message": "ERROR_PROCESAR_SOLICUTUD",
                "data": None,
                "error": error.detail,
                "statusCode": error.status_code,
            },
        )

    @app.exception_handler(RequestValidationError)
    def exception_validacion(request: Request, error: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "DATOS_INVALIDOS_EN_LA_SOLICITUD",
                "data": None,
                "error": error.errors(),
                "statusCode": 422,
            },
        )

    app.include_router(students_router)
    app.include_router(pets_router)

    return app


app = create_app()