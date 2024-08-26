import json
import os
import uuid
from json import JSONDecodeError
from typing import Dict
from task import Task

def write_tasks(tasks: Dict[str, Dict[str, Task]]) -> None:
    try:
        with open("tasks.json", 'w') as file:
            json.dump(tasks["tasks"], file, indent=4)
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_tasks()->Dict[str,Task]:
   try:
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                return json.load(file)
        else:
            raise FileNotFoundError("Error task file not found")
   except JSONDecodeError:
       return {}
   except FileNotFoundError:
       return {}

def print_menu()->None:
    print("1. Add Task\n2. Delete Task\n3. Mark as Completed\n4. List Tasks\n5. Exit")

def generate_id()->str:
    small_id = str(uuid.uuid4().hex)
    return small_id