from service import *
from conaction import create_table

create_table()

while True:
    n = int(input("===Menu=== \n 1) Create task \n 2) Get task by id \n 0) Exit \n choose one : "))
    match n:
        case 1:
            title = input("Enter task title: ")
            discription = input("Enter task discription: ")
            duration = input("Enter task duration (YYYY-MM-DD): ")
            create_task(title, discription, duration)
        case 2:
            task_id = int(input("Enter task id: "))
            get_task(task_id)
        case 0:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")