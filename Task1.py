class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print("Task Marked as completed")
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted.")
        else:
            print("Invalid task index")

    def list_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index + 1}. {task.title} - {status}")


def main():
    todo_list = ToDoList()

    while True:
        print("\t\t\t\t\tTo-Do List")
        print("\n1. Add Task\n2. Complete Task\n3. Delete Task\n4. List Tasks\n5. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                todo_list.add_task(title, description)
                print("Task added!")

            elif choice == "2":
                task_index = int(input("Enter task index to mark as completed: ")) - 1
                todo_list.complete_task(task_index)


            elif choice == "3":
                task_index = int(input("Enter task index to delete: ")) - 1
                todo_list.delete_task(task_index)

            elif choice == "4":
                todo_list.list_tasks()

            elif choice == "5":
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please choose again.")
        except:
            print("Invalid")


if __name__ == "__main__":
    main()
