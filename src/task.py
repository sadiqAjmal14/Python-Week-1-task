from dataclasses import dataclass

@dataclass
class Task:
    name: str
    description: str
    completed: bool = False

    def __repr__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Status: {'Completed' if self.completed else 'Pending'}"
        )

    def mark_as_completed(self):
        self.completed = True
