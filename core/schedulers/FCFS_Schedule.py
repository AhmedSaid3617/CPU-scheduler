from queue import Queue
from core.common.Scheduler import Scheduler
from core.common.Task import Task

class FCFS_Scheduler(Scheduler):
    def __init__(self):
        """
        First-Come, First-Served Scheduler
        attribute: Queue FIFO
        """
        self.queue= Queue()
    
    def reset(self) -> None:
        """Reset the scheduler by clearing the queue."""
        self.queue = Queue()
    
    def run(self, task: Task):
        """
        Load a task into the scheduler multiple times based on burst time
        Queue Size for task as Large as bust time
        example: 8 seconds burst time = 8 entries of task in queue
        """
        for _ in range(task.burst_time):
            self.queue.put(task.name)
    
    def schedule(self) ->str:
        """Return the next task in the queue if available."""
        if self.queue.empty():
            return None
        return self.queue.get()