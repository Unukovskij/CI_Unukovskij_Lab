from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# Базовая модель командировки
class BusinessTripBase(BaseModel):
    employee_id: int = Field(..., description="ID сотрудника (М1 Отдел кадров)", example=101)
    destination: str = Field(..., description="Место назначения", example="г. Москва")
    start_date: date = Field(..., description="Дата начала", example="2026-04-01")
    end_date: date = Field(..., description="Дата окончания", example="2026-04-05")
    purpose: str = Field(..., description="Цель командировки (Основание)", example="Повышение квалификации")
    status: str = Field(default="draft", description="Статус (draft, approved, completed)")

# Модель для создания (без ID)
class BusinessTripCreate(BusinessTripBase):
    pass

# Модель для чтения (с ID)
class BusinessTripRead(BusinessTripBase):
    id: int
    created_at: date

# Модель ошибки
class ErrorResponse(BaseModel):
    detail: str