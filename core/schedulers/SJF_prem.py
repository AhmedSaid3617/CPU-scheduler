from queue import Queue
import heapq
from core.common.Scheduler import Scheduler
from core.common.Task import Task
from core.common.SJF_Task import SJF_Task


class SJF_prem_Scheduler(Scheduler):
    def __init__(self):
        """
        First-Come, First-Served Scheduler
        attribute: Queue FIFO
        """
        self.min_heap = []


    def reset(self) -> None:
        """Reset the scheduler by clearing the queue."""
        self.min_heap = []

    def run(self, task: Task):
        """
        Load a task into the scheduler multiple times based on burst time
        Queue Size for task as Large as bust time
        example: 8 seconds burst time = 8 entries of task in queue
        """
        heapq.heappush(self.min_heap, task)

    def rearrange_min_heap(self):
        heapq.heapify(self.min_heap)

    def schedule(self) -> str:
        """Return the next task in the queue if available."""
        if not self.min_heap:
            return None
        if(self.min_heap[0].burst_time >= 1):
            self.min_heap[0].burst_time -= 1
            task = self.min_heap[0]
            self.rearrange_min_heap()
            if self.min_heap[0].burst_time == 0:
                heapq.heappop(self.min_heap)

            return task
        else:
            return None
