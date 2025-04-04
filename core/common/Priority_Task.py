from core.common.Task import Task

class Piriority_Task(Task):
    """
        Task Class for tasks in system
        attributes: name , arrival_time , burst_time , priority
        We will add options later ( work in progress )
    """
    def __init__(self, name, arr_time=0, burst_time=1, priority=10):
        super().__init__(name=name, arr_time=arr_time, burst_time=burst_time, priority=priority)

    def __lt__(self, other):
        """Compare tasks by burst_time for min-heap behavior"""
        return self.priority < other.priority
