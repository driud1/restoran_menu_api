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
            var = (id_menu, )
            cursor.execute("""
            SELECT id_menu, title, description
	        FROM public.menu WHERE id_menu = %s; 
            """, var)

            result = cursor.fetchone()
            return result



def select_all_menus() -> list:
    """

    :return:
    """
    with pg.connect(**DB_PROPERTIES) as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM public.menu
                ORDER BY id_menu ASC
            """)

            return cursor.fetchall()


def delete_menu(id_menu: int):
    """
    функция принимает id_menu и удаляет его
    :return:
    """
    with pg.connect(**DB_PROPERTIES) as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                DELETE FROM public.menu
                WHERE id_menu = %s
                RETURNING *;

        """, (id_menu, ))
            return cursor.fetchall()


def insert_to_submenus(title: str, description: str, table: str):
    """
    функция создает новую запись в таблице подменю
    :param table:
    :param title:
    :param description:
    :return:
    """
    with pg.connect(**DB_PROPERTIES) as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                INSERT INTO public.submenu(
                title, description)
                VALUES (%s, %s, %s,);
            """, (title, description, table))
            connect.commit()



# когда мы импортируем файл в другой файл, мы по сути вставляем код из одного файла в другой
# Но переменная __name__ == '__main__' только для того файла который мы запустили. Для остальных (импортированных)
# файлов переменная __name__ равна их названию
if __name__ == '__main__':  # __name__ == '__main__'  если  мы запускаем тот файл где это записано(а не импортируем его
    # в другой и запускаем тот)
    # print(globals())
    # insert_to_menu("Fish", "Some fish")
    # print(select_from_menu(10))
    # print(select_all_menus())
    # spam = select_from_menu(1)
    # print(spam)
    print(delete_menu(1))
    print(delete_menu(2))





