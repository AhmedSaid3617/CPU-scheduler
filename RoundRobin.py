from queue import Queue
from core.common.Scheduler import Scheduler
from core.common.Task import Task


class RoundRobinScheduler(Scheduler):

    def __init__(self, timequantum):
        self.queue = Queue()
        self.time_quantum = timequantum
        self.task_time = timequantum
        self.current_task = None

    def reset(self, timequantum) -> None:
        self.queue = Queue()
        self.time_quantum = timequantum

    def run(self, task) -> None:
        self.queue.put(task)

    def schedule(self) -> Task:
        if self.queue.empty() and self.current_task.burst_time == 0:
            return None

        task = self.current_task
        if task is None or task.burst_time == 0 or self.task_time == 0:
            if task is not None and task.burst_time > 0:
                self.queue.put(task)
            self.current_task = self.queue.get()
            task = self.current_task
            self.task_time = self.time_quantum

        if self.task_time > 0:
            task.burst_time -= 1
            self.task_time -= 1
            if task.burst_time == 0:
                self.current_task = task
                return task

        self.current_task = task
        return task
