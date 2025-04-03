from typing import Generic, TypeVar, Optional, List, Tuple, Dict

T = TypeVar('T')
M = TypeVar('M')

class Simulator(Generic[T, M]):
    def __init__(self, scheduler):
        """
        Initialize the simulator with a scheduler.
        """
        self.scheduler = scheduler
        self.batch: Dict[int, List[Tuple[T, int, Optional[M]]]] = {}
        self.timestep = 0

    def load(self, entry):
        """
        Load a task entry into the batch based on its arrival time.
        """
        arrival_time = self.timestep + entry.arrival_time
        if arrival_time not in self.batch:
            self.batch[arrival_time] = []
        self.batch[arrival_time].append((entry.task, entry.burst_time, entry.option))
    
    def load_bulk(self, entries: List):
        """
        Load multiple task entries at once.
        """
        for entry in entries:
            self.load(entry)
    
    def next(self) -> Optional[T]:
        """
        Process the next batch of tasks and schedule one.
        """
        if self.timestep in self.batch:
            self.scheduler.load_bulk(self.batch[self.timestep])
        return self.scheduler.schedule()
    
    def advance(self) -> None:
        """
        Move the simulation forward by one timestep.
        """
        self.next()
    
    def reset(self) -> None:
        """
        Reset the simulator and the scheduler.
        """
        self.timestep = 0
        self.scheduler.reset()