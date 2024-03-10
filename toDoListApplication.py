class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False

    def complete(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date):
        task = Task(name, due_date)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.name} (due {task.due_date})")
            if task.completed:
                print("\tCompleted!")
            else:
                print("\tNot completed yet.")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number-1].complete()
        else:
            print("Invalid task number.")

if __name__ == "__main__":
    my_list = ToDoList()
    my_list.add_task("Complete codesoft project", "Tuesday")
    my_list.add_task("Finish project report", "Friday")
    my_list.view_tasks()
    my_list.complete_task(1)
    my_list.view_tasks()