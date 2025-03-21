from fastapi import FastAPI, HTTPException
import psycopg2
from pydantic import BaseModel

app = FastAPI()

# requêtes
class MenuItem(BaseModel):
    name: str
    price: float

def get_db_connection():
    return psycopg2.connect(
        dbname="restaurant_menu",
        user="postgres",
        password="0919",
        host="localhost",
        port="5432"
    )

@app.get("/menu", response_model=list[MenuItem])
def get_menu():
    """Récupère tous les éléments du menu."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT item_name, item_price FROM Menu_Items")
    items = [MenuItem(name=row[0], price=row[1]) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return items

@app.get("/menu/{name}", response_model=MenuItem)
def get_menu_item(name: str):
    """Récupère un élément du menu par son nom."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (name,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return MenuItem(name=row[0], price=row[1])
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/menu")
def add_menu_item(item: MenuItem):
    """Ajoute un nouvel élément au menu."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)", (item.name, item.price))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Item added successfully"}

@app.put("/menu/{name}")
def update_menu_item(name: str, item: MenuItem):
    """Met à jour un élément du menu."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s", (item.name, item.price, name))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Item updated successfully"}

@app.delete("/menu/{name}")
def delete_menu_item(name: str):
    """Supprime un élément du menu."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
