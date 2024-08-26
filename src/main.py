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
            choice = int(input("Choose an option: "))
            clear_screen()
            
            if choice == 1:
                name = input("Task name: ")
                description = input("Task description: ")
                task_manager.add_task(name, description)
                print("Task added successfully.\n")
        
            elif choice == 2:
                task_manager.list_tasks()
                task_id = input("Enter task ID to delete: ")
                task_manager.delete_task(task_id)
                print("Task deleted successfully.\n")
        
            elif choice == 3:
                task_manager.list_tasks()
                task_id = input("Enter task ID to mark as completed: ")
                task_manager.task_completed(task_id)
                print("Task marked as completed.\n")
        
            elif choice == 4:
                task_manager.list_tasks()
        
            elif choice == 5:
                clear_screen()
                print("Exiting Task Manager.")
                break
        
            else:
                clear_screen()
                print("Invalid input, please choose a valid option.\n")
                
        except ValueError:
            print("Error: Invalid input")
            
        except (IndexError , KeyError):
            print("Error: Task not found")
            
        finally:
            input("\nPress Enter to continue...")
    

if __name__=="__main__":
    main()
        


