import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        """Ajoute l'élément dans la base de données."""
        try:
            with psycopg2.connect(
                dbname="restaurant_menu",
                user="postgres",
                password="0919",
                host="localhost",
                port="5432"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING item_id",
                        (self.name, self.price)
                    )
                    conn.commit()
        except psycopg2.Error as e:
            print(f"Erreur lors de l'ajout de l'élément : {e}")

    def delete(self):
        """Supprime l'élément de la base de données."""
        try:
            with psycopg2.connect(
                dbname="restaurant_menu",
                user="postgres",
                password="0919",
                host="localhost",
                port="5432"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "DELETE FROM Menu_Items WHERE item_name = %s",
                        (self.name,)
                    )
                    conn.commit()
        except psycopg2.Error as e:
            print(f"Erreur lors de la suppression de l'élément : {e}")

    def update(self, new_name, new_price):
        """Met à jour le nom et le prix de l'élément."""
        try:
            with psycopg2.connect(
                dbname="restaurant_menu",
                user="postgres",
                password="0919",
                host="localhost",
                port="5432"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                        (new_name, new_price, self.name)
                    )
                    conn.commit()
                    # Met à jour les attributs de l'instance
                    self.name = new_name
                    self.price = new_price
        except psycopg2.Error as e:
            print(f"Erreur lors de la mise à jour de l'élément : {e}")

    def __repr__(self):
        return f"MenuItem(name={self.name}, price={self.price})"
