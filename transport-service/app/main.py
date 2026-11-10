from fastapi import FastAPI, HTTPException, status
from app import store
from app.schemas import BusinessTripCreate, BusinessTripRead, ErrorResponse
from typing import List

app = FastAPI(
    title="API Кадрового учета: Командировки",
    description="REST API для управления служебными командировками (по модели IDEF0)",
    version="1.0.0"
)

# 1. Получение списка
@app.get(
    "/api/v1/trips/",
    response_model=List[BusinessTripRead],
    summary="Получить список всех командировок",
    tags=["Командировки"]
)
def get_trips():
    return store.get_all()

# 2. Получение по ID
@app.get(
    "/api/v1/trips/{trip_id}",
    response_model=BusinessTripRead,
    responses={404: {"model": ErrorResponse, "description": "Не найдено"}},
    summary="Получить детали командировки",
    tags=["Командировки"]
)
def get_trip(trip_id: int):
    trip = store.get_by_id(trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Командировка не найдена")
    return trip

# 3. Создание
@app.post(
    "/api/v1/trips/",
    response_model=BusinessTripRead,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": ErrorResponse, "description": "Ошибка валидации"}},
    summary="Создать новую командировку",
    tags=["Командировки"]
)
def create_trip(payload: BusinessTripCreate):
    if payload.start_date > payload.end_date:
        raise HTTPException(status_code=400, detail="Дата начала не может быть позже даты окончания")
    return store.create(payload.model_dump())

# 4. Удаление
@app.delete(
    "/api/v1/trips/{trip_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse, "description": "Не найдено"}},
    summary="Удалить командировку",
    tags=["Командировки"]
)
def delete_trip(trip_id: int):
    if not store.delete(trip_id):
        raise HTTPException(status_code=404, detail="Командировка не найдена")
    return None