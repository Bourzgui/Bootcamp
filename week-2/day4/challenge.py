import requests
import sqlite3
import random

def setup_database():
    
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()
   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            capital TEXT,
            flag TEXT,
            subregion TEXT,
            population INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
 
def get_random_countries():
    url = 'https://restcountries.com/v3.1/all'
    
    try:
        
        response = requests.get(url)
        response.raise_for_status()   
        countries = response.json()
        
        random_countries = random.sample(countries, 10)
        
        conn = sqlite3.connect('countries.db')
        cursor = conn.cursor()
        
        for country in random_countries:
            name = country.get('name', {}).get('common', 'Unknown')
            
            capital = country.get('capital', ['Unknown'])[0] if country.get('capital') else 'Unknown'
            flag = country.get('flag', 'Unknown')
            subregion = country.get('subregion', 'Unknown')
            population = country.get('population', 0)
   
            cursor.execute('''
                INSERT INTO countries (name, capital, flag, subregion, population)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, capital, flag, subregion, population))
 
        conn.commit()
        conn.close()
        
        print("Successfully added 10 random countries to the database!")
 
        conn = sqlite3.connect('countries.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM countries")
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Capital: {row[2]}, Population: {row[5]}")
        conn.close()
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
 
if __name__ == "__main__":
    setup_database()
    get_random_countries()
