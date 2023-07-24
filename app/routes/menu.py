from app.schemas import Menu,SuccessResponse
from fastapi import APIRouter
from app.databace import db

router = APIRouter()


@router.get("/api/v1/menus")
async def get_list_of_menus():
    """функция обращается к базе данных, забирает список меню и возвращает его пользователю в виде списка"""
    # return [1, 2, 3]  # просто заглушка
    return db.select_all_menus()   # реальная информация из меню


@router.post("/api/v1/menus", status_code=201)
async def add_menus(menu: Menu):
    """
    функция обрабатывает post запрос (принимает json вида {"title": str, "description": str}) и добавляет в таблицу menu
    новый элемент (menu_id, title, description)
    :param menu:
    :return:
    """
    db.insert_to_menu(menu.title, menu.description)
    print("I called  function add_menus")
    return menu


@router.get("/api/v1/menus/{target_menu_id}")
async def get_menu_item(target_menu_id: str):
    """
    функция возвращает title и discription menu по поданному в пути id меню
    :param target_menu_id: id запращиваемого меню
    :return: List[str]
    """
    target_menu_id = int(target_menu_id)
    print(target_menu_id)
    try:
        menu_id, title, description = db.select_from_menu(target_menu_id)
        return {"id": str(menu_id), "title": title, "description": description}
    except TypeError as e:
        return {"error": TypeError.__doc__}








@router.patch("/api/v1/menus/{target_menu_id}")
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


@router.delete("/api/v1/menus/{target_menu_id}", response_model=SuccessResponse)
async def delete_menu_id(target_menu_id: int):
    """
    Функция удаляет меню по ID(target_menu_id)
    :param target_menu_id:
    :return:
    """
    if db.delete_menu(target_menu_id):
        return SuccessResponse(message="deleted successfully")
    else:
        return SuccessResponse(message="Nothing deleted")


# @router.delete("/api/v1/menus_other/{target_menu_id}", status_code=204)
# async def delete_menu_id(target_menu_id: int):
#     """
#     Функция удаляет меню по ID(target_menu_id)
#     :param target_menu_id:
#     :return:
#     """
#     if target_menu_id:
#         pass
#














