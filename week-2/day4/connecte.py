import psycopg2

# 1. Connect to the database

DB_NAME = "hollywood"
USER = "postgres" 
PASSWORD = "postgres" 
HOST = "localhost"
PORT = "5432" # or 5433

# 3. Write an SQL query
def create_table(table_name: str): 
    """create new table with id, num"""

    query = f'''
    create table {table_name}(
        id serial primary key,
        num integer not null
    );
    '''
    cursor.execute(query) # execute the query
    connection.commit() # make changes in the database

def insert_into_table(table_name: str, num_value: int):

    query = f'''
    insert into {table_name}(num)
    values
    ({num_value})
    '''
    cursor.execute(query) # execute the query
    connection.commit() # make changes in the database

def select_all(table_name: str):

    query = f'''
    select * from {table_name};
    '''

    cursor.execute(query)
    output = cursor.fetchall()
    return output



if __name__ == '__main__':

    try:
        connection = psycopg2.connect(
            dbname = DB_NAME,
            user = USER,
            password = PASSWORD,
            host = HOST,
            port = PORT
        )
    except Exception as e:
        print(f"Error: {e}")

    # 2. Create a cursor object
    cursor = connection.cursor()

    table_name = 'new_table3'

    create_table(table_name)

    insert_into_table(table_name, 12312)
    insert_into_table(table_name, 88888)

    print(select_all(table_name))

    # 4. Close database connection

    connection.close()