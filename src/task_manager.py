from dataclasses import dataclass, asdict
from typing import Dict
from task import Task
from utils import write_tasks, generate_id


@dataclass
class TaskManager:
    tasks: Dict[str,Task]
    
    def __post_init__(self) -> None:
        self.tasks = {task_id: Task(**task) for task_id, task in self.tasks.items()}

    def list_tasks(self) -> None:
        if len(self.tasks)!=0:
            print("Current Tasks:")
            for task_id, task in zip(self.tasks.keys(), self.tasks.values()):
                print(f"\nID: {task_id}")
                print(task)
        else:
            print("No tasks Found")            

    def add_task(self, name: str, description: str) -> None:
        if name!="" and description!="":
            task_id=generate_id()
            self.tasks[task_id]=Task(name, description)
            self._persist_tasks()
        else:
            raise ValueError("Please enter a valid name and description for the task")

    def delete_task(self, task_id: str) -> None:
        if task_id in self.tasks:
            self.tasks.pop(task_id)
            self._persist_tasks()
        else:
            raise KeyError("Task not found")
        
    def task_completed(self, task_id: str) -> None:
        if task_id in self.tasks:
            self.tasks[task_id].mark_as_completed()
            self._persist_tasks()
        else:
            raise KeyError("Task not found")

    def _persist_tasks(self) -> None:
        write_tasks(asdict(self))
