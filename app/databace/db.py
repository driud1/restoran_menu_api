import psycopg2 as pg

DB_PROPERTIES = {
    "database": "menu",
    "user": "postgres",
    "password": "02342Met",
    "host": "127.0.0.1",
    "port": "5432"
}


def insert_to_menu(title: str, description: str):
    """
    функция создает новую запись в таблице меню
    :param title:
    :param description:
    :return:
    """
    print(globals())
    with pg.connect(**DB_PROPERTIES) as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                INSERT INTO public.menu(
                title, description)
                VALUES (%s, %s);
            """, (title, description))
            connect.commit()


def select_from_menu(id_menu: int) -> tuple[str]:
    """
    функция принимает id_menu и возвращает id title и description
    :param id_menu:
    :return: tuple(id, title, description)
    """
    with pg.connect(**DB_PROPERTIES) as connect:
        with connect.cursor() as cursor:
            var = (id_menu,)
            cursor.execute("""
            SELECT id_menu, title, description
	        FROM public.menu WHERE id_menu = %s; 
            """, var)

            result = cursor.fetchone()
            return result



if __name__ == '__main__':  # __name__ == '__main__'  если  мы запускаем тот файл где это записано(а не импортируем его
    # в другой и запускаем тот)
    # print(globals())
    # insert_to_menu("Fish", "Some fish")
    print(select_from_menu(10))






