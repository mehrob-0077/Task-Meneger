from conaction import contion_db

def  get_task(task_id):
    conn = contion_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
        data = cur.fetchone()
        for task in data:
            print(f"""
        Your task
task_id: {data[0]}
task_title: {data[1]}
task_discription: {data[2]}
task_duration: {data[3]}
task_status: {data[4]}
        """)
            
    except Exception as error:
        print(f"Error getting task: {error}")

    finally:
        conn.commit()
        cur.close()
        conn.close()


def  create_task(title, discription, duration):
    conn = contion_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO tasks (title, discription, duration) VALUES (%s, %s, %s)", (title, discription, duration))
        print("Task created successfully.")
    except Exception as error:
        print(f"Error creating task: {error}")

    finally:
        conn.commit()
        cur.close()
        conn.close()