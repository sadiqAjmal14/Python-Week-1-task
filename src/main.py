import os
from task_manager import TaskManager
from utils import print_menu, read_tasks

def clear_screen():
    os.system('cls')

def main():
    task_manager = TaskManager(read_tasks())
    while True:
        try:
            clear_screen()
            print_menu()
            choice = input("Choose an option: ").strip()
            clear_screen()
            
            if choice == "1":
                try:
                    name = input("Task name: ").strip()
                    description = input("Task description: ").strip()
                    task_manager.add_task(name, description)
                    print("Task added successfully.\n")
                except ValueError as ve:
                    print(f"Error adding task: {ve}")
        
            elif choice == "2":
                try:
                    task_manager.list_tasks()
                    task_id = input("Enter task ID to delete: ").strip()
                    task_manager.delete_task(task_id)
                    print("Task deleted successfully.\n")
                except KeyError as ke:
                    print(f"Error deleting task: {ke}")
        
            elif choice == "3":
                try:
                    task_manager.list_tasks()
                    task_id = input("Enter task ID to mark as completed: ").strip()
                    task_manager.task_completed(task_id)
                    print("Task marked as completed.\n")
                except KeyError as ke:
                    print(f"Error marking task as completed: {ke}")
                except ValueError as ve:
                    print(f"Error: {ve}")
        
            elif choice == "4":
                task_manager.list_tasks()
        
            elif choice == "5":
                clear_screen()
                print("Exiting Task Manager.")
                break
        
            else:
                clear_screen()
                print("Invalid input, please choose a valid option.\n")
                
        except Exception as err:
            print(f"An unexpected error occurred: {err}")  # Keep the general exception handling
        
        finally:
            input("\nPress Enter to continue...")

    

if __name__=="__main__":
    main()
        


