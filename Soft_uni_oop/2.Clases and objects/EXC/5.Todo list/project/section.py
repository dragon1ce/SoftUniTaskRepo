from typing import List
from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self,task_name: str):
        for tasks in self.tasks:
            if tasks.name == task_name:
                tasks.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for t in self.tasks:
            if t.completed == True:
                self.tasks.remove(t)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        return_msg= [f"Section {self.name}:"]
        for t in self.tasks:
            return_msg.append(t.details())
        return '\n'.join(return_msg)



