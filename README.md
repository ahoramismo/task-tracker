# Task Manager CLI
> **Note**: This project is part of the [roadmap.sh/projects](https://roadmap.sh/projects?g=backend) series


A simple command-line interface (CLI) for managing tasks. This project allows you to add, delete, list, and mark tasks as "in-progress", "done", or "to-do". The tasks are stored in a JSON file and managed through the TaskManager class.

## Features
- Add a task: Adds a new task to the list.
- Delete a task: Removes a task by its ID.
- List tasks: Lists all tasks or tasks filtered by their current state (e.g., "to-do", "in-progress", "done").
- Mark task state: Change the state of a task to "to-do", "in-progress", or "done".


## Installation
To get started with the Task Manager project, clone this repository and install the required dependencies:

```shell
# Clone the repository
git clone https://github.com/ahoramismo/task-tracker.git

# (Optional but recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required dependencies
pip install -r requirements.txt
```
Ensure that you have a Python version of 3.6 or higher installed.

## Usage
### CLI Commands
The Task Manager CLI allows the following commands:

#### 1. Add a task:

```bash
task-cli add <task_name>
```

#### 2. List tasks:

List all tasks:
```bash
task-cli list
```
List tasks filtered by state (e.g., "to-do", "in-progress", "done"):
```bash
task-cli list <state>
```

#### 3. Delete a task:
```bash
task-cli delete <task_id>
```

#### 4. Mark task state:

Mark a task as in-progress:

```bash
task-cli mark-in-progress <task_id>
```
Mark a task as done:

```bash
task-cli mark-done <task_id>
```
Mark a task as to-do:

```bash
task-cli mark-todo <task_id>
```

### Example
Here is an example of how you might interact with the CLI:

```bash

$ task-cli add "Complete project report"
Task added successfully (ID: 1)

$ task-cli list
1: Complete project report [todo]

$ task-cli mark-in-progress 1
Task updated successfully.

$ task-cli list IN_PROGRESS
1: Complete project report [in-progress]
```


## File Structure

```
task-tracker/
├── src/
│   ├── constants.py            # Constants used by the application (e.g., task file path)
│   ├── storage.py              # Handles loading and saving data from JSON
│   ├── task_manager.py         # Main task manager logic and CLI commands
│   ├── task_state.py           # Task states (e.g., TODO, IN_PROGRESS, DONE)
│
├── requirements.txt            # List of dependencies
├── setup.py                    # (if using setuptools for pip install -e .)
└── README.md
```

## Requirements
* Python 3.6 or higher

