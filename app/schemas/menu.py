from pydantic import BaseModel
from typing import Union

"""
файл содержит классы, описывающие типы приходящих к приложению данных
"""


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


# класс для валидации json
# данный класс называется схемой данный
class Menu(BaseModel):
    title: str
    description: str


# { 'code': 200
# "message': "Successful response"}
class SuccessResponse(BaseModel):
    code: int = 200
    message: str = "Successful response"


class Submenus(BaseModel):
    title: str
    description: str


if __name__ == '__main__':

    successful_response = SuccessResponse()
    print(successful_response)









