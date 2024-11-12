# task_manager.py
# task structure

import json
import os

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            id=task_dict['id'],
            title=task_dict['title'],
            completed=task_dict['completed']
        )
# Implement Task Management Functions

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"[{task.id}] {task.title} - {status}")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        print(f"Task with ID {task_id} deleted.")

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Task '{task.title}' marked as completed.")
                return
        print(f"No task found with ID {task_id}")

#File Handling

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print("Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                tasks_list = json.load(file)
                self.tasks = [Task.from_dict(task) for task in tasks_list]
#Create a Command-Line Interface
def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter task title: ")
            task_manager.add_task(title)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                task_manager.mark_task_complete(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '5':
            task_manager.save_tasks()
        elif choice == '6':
            print("Exiting Task Manager...")
            task_manager.save_tasks()  # Auto-save on exit
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
