class Task:
    """
        Task Class for tasks in system
        attributes: name , arrival_time , burst_time , priority
        We will add options later ( work in progress )
    """
    def __init__(self, name, arr_time=0, burst_time=1, priority=None):
        self.name = name
        self.arr_time = arr_time
        self.burst_time = burst_time
        self.priority = priority
