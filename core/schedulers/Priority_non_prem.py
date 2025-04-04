from queue import Queue
import heapq
import sys

sys.path.insert(0, '..')
from core.common.Scheduler import Scheduler
from core.common.Task import Task
from core.common.Priorit_Task import Priorit_Task


class Priority_non_prem_Scheduler(Scheduler):
    def __init__(self):
        """
        First-Come, First-Served Scheduler
        attribute: Queue FIFO
        """
        self.min_heap = []
        self.current_task = None


    def reset(self) -> None:
        """Reset the scheduler by clearing the queue."""
        self.min_heap = []
        self.current_task = None

    def run(self, task: Task):
        """
        Load a task into the scheduler multiple times based on burst time
        Queue Size for task as Large as bust time
        example: 8 seconds burst time = 8 entries of task in queue
        """
        heapq.heappush(self.min_heap, task)

    def rearrange_min_heap(self)-> Task:
        heapq.heapify(self.min_heap)
        task=self.min_heap[0]
        return task

    def schedule(self) -> str:
        """Return the next task in the queue if available."""
        if not self.min_heap:
            return None
        if self.current_task is None:
            self.current_task = self.rearrange_min_heap()
        if(self.current_task.burst_time >= 1):
            self.current_task.burst_time -= 1
            return self.current_task.name
        else:
            # Current task is finished
            self.current_task = None
            heapq.heappop(self.min_heap)

            # Check if there are more tasks
            if self.min_heap:
                self.current_task = self.rearrange_min_heap()
                self.current_task.burst_time -= 1
                return self.current_task.name
            else:
                return None

