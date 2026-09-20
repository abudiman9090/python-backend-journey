class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def __str__(self):
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title}"

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    @classmethod
    def from_dict(cls,data):
        return cls(data["title"], data["done"])


class TodoManager:
    def __init__(self):
        self.tasks = []

    def add(self,title):
        self.tasks.append(Task(title))

    def list_all(self):
        return self.tasks

    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            return True
        return False

    def delete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False