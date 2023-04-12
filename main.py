import fastapi
import uvicorn
from utils.data_types import Item, Menu


app = fastapi.FastAPI(debug=True)

menu_list = []


@app.get("/test")  # возвращает информацию с сервера на клиент
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/posttest")
async def test():
    pass


@app.get("/api/v1/menus")
async def get_list_of_menus():
    """функция обращается к базе данных, забирает список меню и возвращает его пользователю в виде списка"""
    return [menu_list]



@app.post("/api/v1/menus", status_code=201)
async def add_menus(menu: Menu):
    """
    функция обрабатывает post запрос (принимает json вида {"title": str, "description": str}) и добавляет в таблицу menu
    новый элемент (menu_id, title, description)
    :param menu:
    :return:
    """
    print(menu.title, menu.title, menu)
    return menu



@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/api/v1/menus/{target_menu_id}")
async def get_menu_item(target_menu_id: int):
    """
    функция возвращает title и discription menu по поданному в пути id меню
    :param target_menu_id: id запращиваемого меню
    :return: List[str]
    """
    return target_menu_id


@app.patch("/api/v1/menus/{target_menu_id}", )
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


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=5467)


