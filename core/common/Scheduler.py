from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Tuple

T = TypeVar('T')
M = TypeVar('M', bound=Optional[None])  # Default to None if not specified

class Scheduler(ABC, Generic[T, M]):
    
    @abstractmethod
    def reset(self) -> None:
        """Reset the state of the scheduler and remove all tasks."""
        pass
    
    @abstractmethod
    def load(self, task: T, burst: int, option: Optional[M] = None) -> None:
        """Load a task into the scheduler."""
        pass
    
    def load_bulk(self, tasks: List[Tuple[T, int, Optional[M]]]) -> None:
        """Load multiple tasks into the scheduler."""
        for task, burst, option in tasks:
            self.load(task, burst, option)
    
    @abstractmethod
    def schedule(self) -> Optional[T]:
        """Schedule the next task."""
        pass
