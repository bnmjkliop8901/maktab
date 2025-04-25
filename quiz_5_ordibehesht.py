class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.completed = False

    def execute(self):
        print(f"executing : {self.name}")
        self.mark_completed()

    def mark_completed(self):
        self.completed = True
        print(f"{self.name} completed.")


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run_all(self):
        self.tasks.sort(key=lambda x: x.priority)
        for task in self.tasks:
            if not task.completed:
                task.execute()

    def show_pending(self):
        pending = [task.name for task in self.tasks if not task.completed]
        for task in pending:
            print(f"{task}")
