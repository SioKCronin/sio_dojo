import sqlite3

def create_connection(db_file):
    "Create database connection"

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "rumi.db"

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects(
                                       id integer PRIMARY KEY, 
                                       name text NOT NULL,
                                       begin_date text,
                                       end_date text
                                       );"""

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks(
                                 id integer PRIMARY KEY, 
                                 name text NOT NULL, 
                                 priority integer, 
                                 status_id integer NOT NULL, 
                                 project_id integer NOT NULL,
                                 begin_date text NOT NULL,
                                 end_date text NOT NULL );"""

    conn = create_connection(database)

    if conn is not None:
        #Create projects table
        create_table(conn, sql_create_projects_table)
        #Create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error")

if __name__ == '__main__':
    main()
