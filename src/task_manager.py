from task_state import TaskState
from constants import TASKS_FILE
from storage import load_json, save_json


class TaskManager:
    def __init__(self, filepath=TASKS_FILE):
        """Initialize the TaskManager with data loaded from the file."""
        self.filepath = filepath
        self.data = load_json(self.filepath)

    def _save(self):
        """Save the current task data to the file."""
        save_json(self.data, self.filepath)

    def _get_next_id(self):
        """Get the next available unique task ID."""
        if not self.data['tasks']:
            return 1
        return max(task['id'] for task in self.data['tasks']) + 1


    def add(self, task_name):
        """Add a new task with the given name."""
        task = {
            "id": self._get_next_id(),
            "task": task_name,
            "state": TaskState.TODO
        }
        self.data['tasks'].append(task)
        self._save()
        print(f"Task added successfully (ID: {task['id']})")

    def delete(self, task_id):
        """Delete a task by its ID."""
        task_id = int(task_id)
        for task in self.data['tasks']:
            if task['id'] == task_id:
                self.data['tasks'].remove(task)
                self._save()
                print(f"Task removed successfully (ID: {task_id})")
                return
        print(f"Task with ID {task_id} not found.")

    def list(self, state=None):
        """List all tasks, optionally filtered by state."""
        tasks = self.data['tasks']
        if state:
            tasks = [task for task in tasks if task['state'] == state]
        if not tasks:
            print("No task found")
            return
        for task in tasks:
            print(f"{task['id']}: {task['task']} [{task['state']}]")

    def mark(self, task_id, state):
        """Mark a task as a given state (must be one of TaskState values)."""
        task_id = int(task_id)

        if state not in TaskState.__members__.values():
            print(
                f"Invalid state: {state}. Must be one of {[s.value for s in TaskState]}")
            return
        for task in self.data['tasks']:
            if task['id'] == task_id:
                task['state'] = state
                self._save()
                print("Task updated successfully.")
                return
        print(f"Task with ID {task_id} not found.")
