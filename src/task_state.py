from enum import Enum


class TaskState(str, Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'
