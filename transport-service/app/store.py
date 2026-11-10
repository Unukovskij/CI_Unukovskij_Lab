from typing import Dict, List
from app.schemas import BusinessTripRead
from datetime import date

# Имитация базы данных (М3 Информационная система)
_trips: Dict[int, BusinessTripRead] = {}
_next_id = 1

def get_all() -> List[BusinessTripRead]:
    return list(_trips.values())

def get_by_id(trip_id: int) -> BusinessTripRead | None:
    return _trips.get(trip_id)

def create(trip_data: dict) -> BusinessTripRead:
    global _next_id
    new_trip = BusinessTripRead(
        id=_next_id,
        created_at=date.today(),
        **trip_data
    )
    _trips[_next_id] = new_trip
    _next_id += 1
    return new_trip

def delete(trip_id: int) -> bool:
    if trip_id in _trips:
        del _trips[trip_id]
        return True
    return False

# Наполним тестовыми данными
create({
    "employee_id": 101, "destination": "г. Санкт-Петербург",
    "start_date": date(2026, 5, 10), "end_date": date(2026, 5, 12),
    "purpose": "Семинар", "status": "approved"
})