import fastapi
import uvicorn
from app.schemas.menu import Item
from app.routes import menu

app = fastapi.FastAPI(debug=True)  # создаем эксземпляр fastapi приложения  (он хранится, в файле app.main)

app.include_router(menu.router)


@app.get("/")  # возвращает информацию с сервера на клиент
async def root():
    return {"message": "Hello World"}


@app.post('/')
async def post_root(item: Item):

    return item


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=5467)
