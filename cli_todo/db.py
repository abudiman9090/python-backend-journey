import os
import psycopg2

DB_CONFIG = {
    "dbname": "todos",
    "user": "postgres",
    "password": os.environ.get("PGPASSWORD", ""),   # replace with your real password
    "host": "localhost",
    "port": "5432",
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def list_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, done FROM tasks ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_task(title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    print("Tasks in database:")
    for row in list_tasks():
        print(row)

    add_task("Read a book")
    print("\nAfter adding 'Read a book':")
    for row in list_tasks():
        print(row)