from fastapi import APIRouter

from redis_tools.tools import RedisTools
from .validate import Phone

router = APIRouter()
redis_tools = RedisTools()


@router.get("/all_phone/", tags=["Check data"])
async def all_key():
    """Получение всех телефонов."""

    return redis_tools.get_all_keys()


@router.get("/check_data/", tags=["Check data"])
async def check_data(phone: str = ""):
    """Получение адреса по телефону из cache."""

    phone = phone.strip()
    res = redis_tools.get_data(phone)
    if not res:
        return "The phone is missing"
    return res


@router.post("/write_data/", tags=["check_data"])
def write_data(data: Phone):
    """Обновление/Создание записей телефонов."""

    phone = redis_tools.get_data(data.phone)
    if not phone:
        redis_tools.set_data(data.phone, data.address)
        return "Data recorded"
    redis_tools.set_data(data.phone, data.address)
    return "Data updated"
