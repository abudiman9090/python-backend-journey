class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def __str__(self):
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title}"