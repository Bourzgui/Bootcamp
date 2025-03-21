import psycopg2
from menu_item import MenuItem  # Assure-toi que le fichier menu_item.py existe et contient la classe MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        try:
            conn = psycopg2.connect(
                dbname="restaurant_menu",
                user="postgres",
                password="0919",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute(
                "SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s",
                (name,)
            )
            result = cur.fetchone()
            cur.close()
            conn.close()

            if result:
                return MenuItem(result[0], result[1])
            return None

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return None

    @classmethod
    def all_items(cls):
        try:
            conn = psycopg2.connect(
                dbname="restaurant_menu",
                user="postgres",
                password="0919",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("SELECT item_name, item_price FROM Menu_Items")
            results = cur.fetchall()
            cur.close()
            conn.close()

            return [MenuItem(name, price) for name, price in results]

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return []
