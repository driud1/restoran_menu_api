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


if __name__ == '__main__':
    # print(globals())
    insert_to_menu("Fish", "Some fish")

