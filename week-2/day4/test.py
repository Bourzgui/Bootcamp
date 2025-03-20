import psycopg2
from psycopg2 import Error

def test_connection():
    try:
        connection = psycopg2.connect(
            dbname="restaurant_menu",
            user="postgres",
            password="0919",
            host="localhost",
            port="5432"  
        )
        
        cursor = connection.cursor()  

        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        
        print("Connection successful!")
        print(f"PostgreSQL database version: {db_version}") 
    
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'menu_items'
            );
        """)
        table_exists = cursor.fetchone()[0]
        
        if table_exists:
            print("Menu_Items table exists in the database")
            
            cursor.execute("SELECT * FROM Menu_Items LIMIT 5;")
            records = cursor.fetchall() # Récupérer tous les résultats
            print("\nFirst 5 records in Menu_Items:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")
        else:
            print("Menu_Items table does not exist yet")

    except Error as e:
        print("Error while connecting to PostgreSQL:")
        print(e)
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    print("database connection...")
    test_connection()