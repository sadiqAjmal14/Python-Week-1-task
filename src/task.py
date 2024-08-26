from dataclasses import dataclass

@dataclass(repr=False)
class Task:
    name: str
    description: str
    completed: bool = False

    def __repr__(self)->str:
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Status: {'Completed' if self.completed else 'Pending'}"
        )
    
    def mark_as_completed(self) -> None:
        if not self.completed:
            self.completed = True
        else:
            raise ValueError("Task is already completed")

