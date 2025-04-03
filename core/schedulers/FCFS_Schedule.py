from queue import Queue
from typing import Generic, TypeVar, Optional
from core.common.Scheduler import Scheduler
from core.common.EmptyOption import EmptyOption

T = TypeVar('T')

class FCFS_Scheduler(Scheduler[T, EmptyOption]):
    def __init__(self):
        """First-Come, First-Served Scheduler"""
        self.queue: Queue[T] = Queue()
    
    def reset(self) -> None:
        """Reset the scheduler by clearing the queue."""
        self.queue = Queue()
    
    def load(self, task: T, burst: int, option: Optional[EmptyOption] = None) -> None:
        """Load a task into the scheduler multiple times based on burst time."""
        for _ in range(burst):
            self.queue.put(task)
    
    def schedule(self) -> Optional[T]:
        """Return the next task in the queue if available."""
        if self.queue.empty():
            return None
        return self.queue.get()