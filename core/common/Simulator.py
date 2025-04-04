from collections import defaultdict
from typing import List, Tuple, Dict
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from core.common.Task import Task
from core.schedulers.FCFS_Schedule import FCFS_Scheduler

class Simulator():
    """"
    with Simulator Class we can simulate each time step and get an ouput of task that runned
    the past second , also we can load tasks and list of tasks.
    """
    def __init__(self, scheduler):
        """
        Initialize the simulator with a scheduler.
        first attribute: schedular instance
        second attribute: dictionary of arrival time as key and tasks as list of values
        third attribute: current time
        Note: batch has arrival times with all tasks that have arrived in that time
        """
        self.scheduler = scheduler
        self.batch=defaultdict(list)
        self.timestep = 0

    def load(self, task: Task):
        """
        Load a task into the batch based on its arrival time.
        index with key arrival time and append the task
        """
        # arr_time = self.timestep + task.arr_time  # shams part i don't get it
        arr_time=self.timestep # fixed
        self.batch[arr_time].append(task)
    
    def load_bulk(self, tasks: List):
        """
        Load multiple task entries at once.
        """
        for task in tasks:  # loop over tasks and load each one independently
            self.load(task)
    
    def next(self) ->str :
        """
        Process the next batch of tasks and schedule one.

        checks timestep in arrival time of batch dictionary
        if there loads all tasks in that arrival time

        DOES NOT INCREMENT TIME ( ask shams why )
        """
        if self.timestep in self.batch:
            self.scheduler.load_bulk(self.batch[self.timestep])
        return self.scheduler.schedule()
    
    def advance(self) -> str:
        """
        Same as Next but increments timestep by 1 after doing next
        Move the simulation forward by one timestep.
        """
        name=self.next()
        self.timestep = self.timestep + 1
        return name
    
    def reset(self) -> None:
        """
        Reset the simulator and the scheduler.
        """
        self.timestep = 0
        self.scheduler.reset()

"""
tests ran on Simulator file
Verified
"""
# def main():
#     sim=Simulator(FCFS_Scheduler())
#     sim.load(Task(name="task 1",burst_time=2))
#     sim.load(Task(name="task 2",burst_time=2))
#     print(sim.advance())
#     print(sim.advance())
#     print(sim.advance())
#     print(sim.advance())
#     print(sim.advance())
#
# if __name__ == "__main__":
#     main()
