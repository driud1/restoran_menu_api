# from app.schemas.menu import Menu
from app.schemas import Menu
from app.main import app
from fastapi import APIRouter


router = APIRouter()


@router.get("/api/v1/menus")
async def get_list_of_menus():
    """функция обращается к базе данных, забирает список меню и возвращает его пользователю в виде списка"""
    return [1, 2, 3]


@router.post("/api/v1/menus", status_code=201)
async def add_menus(menu: Menu):
    """
    функция обрабатывает post запрос (принимает json вида {"title": str, "description": str}) и добавляет в таблицу menu
    новый элемент (menu_id, title, description)
    :param menu:
    :return:
    """
    print(menu.title, menu.title, menu)
    return menu


@router.get("/api/v1/menus/{target_menu_id}")
async def get_menu_item(target_menu_id: int):
    """
    функция возвращает title и discription menu по поданному в пути id меню
    :param target_menu_id: id запращиваемого меню
    :return: List[str]
    """
    return target_menu_id


@router.patch("/api/v1/menus/{target_menu_id}", )
async def patc_menu_id(target_menu_id: int):
    """
    Функция обновляет запись в таблице меню по ID (target_menu_id) и возвращает обновленный элемент меню
    :param target_menu_id:
    :return:
    """
    if target_menu_id is str:
        return {"None": "None"}
    return {
        "title": "Kvas",
        "description": "Cold russian drink"
    }



