import sys
import json
import os

TASKS_FILE = 'tasks.json'
DEFAULT_DATA = {'tasks': []}


def save_json(data, file_path=TASKS_FILE):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def load_json(file_path=TASKS_FILE):
    """Load JSON data from a file."""
    if not os.path.exists(file_path):
        save_json(DEFAULT_DATA)
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def add_task(task_name):
    """Add a new task."""
    data = load_json()
    task = {
        "task": task_name,
        "id": len(data['tasks']) + 1,
        "state": "todo"
    }
    data['tasks'].append(task)
    save_json(data)
    print(f"Task added successfully (ID: {task['id']})")


def delete_task(task_id):
    """Delete a task by ID."""
    data = load_json()
    task_id = int(task_id)
    for task in data['tasks']:
        if task['id'] == task_id:
            data['tasks'].remove(task)
            save_json(data)
            print(f"Task removed successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")


def list_tasks(state=None):
    """List all tasks."""
    data = load_json()
    if state:
        tasks = [task for task in data['tasks'] if task['state'] == state]
    else:
        tasks = data['tasks']

    if not tasks:
        print("No task found")
        return

    for task in tasks:
        print(f"{task['id']}: {task['task']} [{task['state']}]")


def mark_task(task_id, state):
    """Mark a task as in-progress, done, or todo."""
    data = load_json()
    task_id = int(task_id)
    for task in data['tasks']:
        if task['id'] == task_id:
            task['state'] = state
            save_json(data)
            print(f"Task {task_id} marked as {state}.")
            return

    print(f"Task with ID {task_id} not found.")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return

    command, *args = sys.argv[1:]

    match command:
        case "add":
            if args:
                add_task(args[0])
            else:
                print("Usage: task-cli add <task_name>")
        case "list":
            list_tasks(args[0] if args else None)
        case  "delete":
            delete_task(args[0])
        case "mark-in-progress":
            mark_task(args[0], "in-progress")
        case "mark-done":
            mark_task(args[0], "done")
        case "mark-todo":
            mark_task(args[0], "todo")
        case _:
            print(f"Unknown command: {command}")
