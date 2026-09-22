import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

pasw = os.getenv("PASSWORD_DB")

def contion_db():
    try:
        conn = psycopg2.connect(
        port = 5432,
        host = "localhost",
        user = "postgres",
        database = "ps_db",
        password = pasw
    )
    except Exception as error:
        print(f"Conation error:{error}")
    return conn

   


def create_table():
    conn = contion_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            task_id serial PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            discription TEXT,
            duration date  NOT NULL,
            status boolean DEFAULT false,
            creted_at  timestamp DEFAULT NOW(),
            is_active boolean DEFAULT true
            );
        """)
        conn.commit()
        cur.close()
        print("Table created successfully.")
    except Exception as error:
        print(f"Error creating table: {error}")

