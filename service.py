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


def update_task(task_id, title, discription, duration):
    conn = contion_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            UPDATE tasks
            SET title = %s,
                discription = %s,
                duration = %s
            WHERE task_id = %s
        """, (title, discription, duration, task_id))

        if cur.rowcount == 0:
            print("Task not found.")
        else:
            conn.commit()
            print("Task updated successfully.")

    except Exception as error:
        conn.rollback()
        print(f"Error updating task: {error}")

    finally:
        cur.close()
        conn.close()


def delete_task(task_id):
    conn = contion_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            UPDATE tasks
            SET is_active = FALSE
            WHERE task_id = %s
        """, (task_id,))

        conn.commit()
        print("Task deleted successfully.")

    except Exception as error:
        conn.rollback()
        print(f"Error deleting task: {error}")

    finally:
        cur.close()
        conn.close()
