from fastapi import APIRouter
from app.schemas import SuccessResponse, Menu
from app.databace import db

router = APIRouter()


# /api/v1/menus/{{target_menu_id}}/submenus
@router.post("/api/v1/menus/{target_menu_id}/submenus", status_code=201)
async def add_submenus(target_menu_id: int, submenu: Menu):
    """
    Функция добавляет запись в таблице подменю
    :param submenu:
    :param target_menu_id:
    :return:
    """
    db.insert_to_submenu(submenu.title, submenu.description, target_menu_id)
    # print(target_menu_id, type(target_menu_id))
    return submenu


@router.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
async def get_list_of_submenus():
    """функция обращается к базе данных, забирает список подменю и возвращает его пользователю в виде списка"""
    # return [1, 2, 3]  # просто заглушка
    return db.select_all_submenus()   # реальная информация из меню


@router.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}", response_model=SuccessResponse)
async def delete_submenu_id(target_menu_id: int):
    """
    Функция удаляет подменю по ID(target_menu_id)
    :param target_menu_id:
    :return:
    """
    if db.delete_menu(target_menu_id):
        return SuccessResponse(message="deleted successfully")
    else:
        return SuccessResponse(message="Nothing deleted")