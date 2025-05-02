import sys
import json
import os


def load_json(filepath='tasks.json'):
    """Load JSON data from a file."""
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({"tasks": []}, f)
    with open(filepath, 'r') as f:
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
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Task added successfully (ID: {task['id']})")


def delete_task(task_id):
    """Delete a task by ID."""
    data = load_json()
    task_id = int(task_id)
    for task in data['tasks']:
        if task['id'] == task_id:
            data['tasks'].remove(task)
            with open('tasks.json', 'w') as f:
                json.dump(data, f, indent=4)
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

    for task in tasks:
        print(f"{task['id']}: {task['task']} [{task['state']}]")


def mark_task(task_id, state):
    """Mark a task as in-progress, done, or todo."""
    data = load_json()
    task_id = int(task_id)
    for task in data['tasks']:
        if task['id'] == task_id:
            task['state'] = state
            with open('tasks.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("success")
            return
    print(f"Task with ID {task_id} not found.")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return
    
    command, *args = sys.argv[1:]
    if command == "add":
        add_task(args[0])
    elif command == "list":
        list_tasks(args[0] if args else None)
    elif command == "delete":
        delete_task(args[0])
    elif command == "mark-in-progress":
        mark_task(args[0], "in-progress")
    elif command == "mark-done":
        mark_task(args[0], "done")
    elif command == "mark-todo":
        mark_task(args[0], "todo")
