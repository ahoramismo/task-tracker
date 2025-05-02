import sys
from task_manager import TaskManager
from task_state import TaskState


def main():
    """Main CLI entry point for task management commands."""
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return

    command, *args = sys.argv[1:]
    tm = TaskManager()

    match command:
        case "add":
            tm.add(args[0])
        case "list":
            tm.list(args[0] if args else None)
        case "delete":
            tm.delete(args[0])
        case "mark-in-progress":
            tm.mark(args[0], TaskState.IN_PROGRESS)
        case "mark-done":
            tm.mark(args[0], TaskState.DONE)
        case "mark-todo":
            tm.mark(args[0], TaskState.TODO)
        case _:
            print(f"Unknown command: {command}")
