from abc import ABC, abstractmethod
from typing import  List , Tuple
from core.common.Task import Task
class Scheduler(ABC):
    """
    Scheduler is an abstract base class that defines the Predefined Structure
    of All Schedulers Made in this project. Every Scheduler inherits this Class
    """
    @abstractmethod

    def reset(self) -> None:
        """Reset the state of the scheduler and remove all tasks."""
        pass
    
    @abstractmethod
    def load(self, task: Task) -> None:
        """Load a task into the scheduler."""
        pass
    
    def load_bulk(self, tasks) -> None:
        """Load multiple tasks into the scheduler."""
        for task in tasks:
            self.load(task)
    
    @abstractmethod
    def schedule(self):
        """Schedules the next task. this function returns task that should run now
        for example using FCFS scheduler if task 1 arrives first and
        has burt of 8 seconds after 5 seconds , we should output
        task 1 as task running currently
        """
        pass
