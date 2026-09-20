import json

FILENAME = "tasks.json"

def save(tasks):
    data = [t.to_dict() for t in tasks]
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=2)

def load():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
        from todo import Task
        return [Task.from_dict(d) for d in data]
    except FileNotFoundError:
        return []