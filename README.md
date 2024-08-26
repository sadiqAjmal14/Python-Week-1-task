# Task Manager CLI Application

## Overview

This is a simple Command Line Interface (CLI) application that helps you manage tasks efficiently. You can add, list, delete, and mark tasks as completed. The tasks are persisted across sessions, making it easy to keep track of your to-do list.

## Features

- **Add a Task:** Add new tasks with a name and description.
- **List Tasks:** Display all current tasks with their details.
- **Delete a Task:** Remove tasks by their unique ID.
- **Mark Task as Completed:** Update the status of a task to "Completed."
- **Persist Data:** Tasks are saved and loaded automatically, ensuring data is not lost between sessions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sadiqAjmal14/Python-Week-1-task.git
2. Navigate to the src folder:
   ```bash
   cd Python-Week-1-task/src
3. Ensure that Python 3.10+ is installed:
   ```bash
   python --version

## Usage
- Run the main application:
  ```bash
  python main.py
- Follow the on-screen menu to interact with the Task Manager:
  1.  Add a new task
  2.  Delete an existing task
  3.   Mark a task as completed
  4.   List all tasks
  5.   Exit the application

## Files

- **`main.py`:** The main entry point of the application, handles user input and manages the task operations.
- **`task.py`:** Defines the `Task` class, which represents an individual task.
- **`task_manager.py`:** Manages the collection of tasks in `TaskManager` class, providing methods to add, delete, list, and mark tasks as completed.
- **`utils.py`:** Contains utility functions such as printing the menu, reading tasks from a file, writing tasks to a file, and generating unique task IDs.
- **`tasks.json`:** Contains a dictionary of tasks with their unique ids
