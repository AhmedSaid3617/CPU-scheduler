from typing import Generic, TypeVar, Optional

T = TypeVar('T')
M = TypeVar('M')

class TaskEntry(Generic[T, M]):
    def __init__(self, task: T, burst_time: int, arrival_time: int = 0, option: Optional[M] = None):
        """
        Initialize a TaskEntry with task details.
        """
        self.task = task
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.option = option