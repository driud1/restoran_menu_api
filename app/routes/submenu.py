from fastapi import APIRouter
from app.schemas import SuccessResponse, Menu

router = APIRouter()


# /api/v1/menus/{{target_menu_id}}/submenus
@router.post("/api/v1/menus/{target_menu_id}/submenus")
async def add_submenus(target_menu_id: int, submenu: Menu):
    """
    Функция добавляет запись в таблице подменю
    :param submenu:
    :param target_menu_id:
    :param sub:
    :return:
    """
    db.insert_to_submenu(submenu.title, submenu.description, target_menu_id)
    # print(target_menu_id, type(target_menu_id))
    return SuccessResponse()



