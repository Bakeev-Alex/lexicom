from pydantic import BaseModel


class Phone(BaseModel):
    """Валидация данных post запрсоа."""

    phone: str
    address: str
