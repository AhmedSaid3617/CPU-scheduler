from collections import defaultdict
from typing import List, Tuple, Dict
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
        self.batch = defaultdict(list)
        self.timestep = 0
        self.history = list() # what process executed in each timestep

    def load(self, task: Task):
        """
        Load a task into the batch based on its arrival time.
        index with key arrival time and append the task
        """
        arr_time = task.arr_time  # Absolute time
        self.batch[arr_time].append(task)
    
    def load_bulk(self, tasks: List):
        """
        Load multiple task entries at once.
        """
        for task in tasks:  # loop over tasks and load each one independently
            self.load(task)
    
    def next(self) -> Task :
        """
        Process the next batch of tasks and schedule one.

        checks timestep in arrival time of batch dictionary
        if there loads all tasks in that arrival time

        DOES NOT INCREMENT TIME ( ask shams why )
        """
        if self.timestep in self.batch:
            self.scheduler.load_bulk(self.batch[self.timestep])
        return self.scheduler.schedule()
    
    def advance(self) -> Task:
        """
        Same as Next but increments timestep by 1 after doing next
        Move the simulation forward by one timestep.
        Appends to history the task that runned in this timestep, even if it was None
        """
        task=self.next()
        self.timestep = self.timestep + 1
        self.history.append(task)
        return task

    def history_matches(self, tasks: List[Task]) -> bool:
        """
        Match history of scheduled CPU tasks with a given list of tasks.
        Does not affect the history of the simulator.
        If given list is smaller than history, it will match only the first len(tasks) elements.
        """
        for i in range(len(tasks)):
            if self.history[i] != tasks[i]:
                return False

        return True
    
    def reset(self) -> None:
        """
        Reset the simulator and the scheduler.
        """
        self.timestep = 0
        self.scheduler.reset()

    def accept(self, visitor):
        return visitor.visit(self)

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
