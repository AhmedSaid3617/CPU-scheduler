import unittest
from sched import scheduler

from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.TaskEntry import TaskEntry

class TestFCFS(unittest.TestCase):
    def test_basic_assertions(self):
        """Test FCFS scheduler with basic task loading and scheduling."""
        sch = FCFS_Scheduler[str]()
        sim = Simulator(sch)
        
        sim.load(TaskEntry("task 1", 1))
        
        sim.load_bulk([
            TaskEntry("task 2", 1, 0),
            TaskEntry("task 3", 1, 0)
        ])
        
        self.assertEqual(sim.next(), "task 1")
        self.assertEqual(sim.next(), "task 2")
        self.assertEqual(sim.next(), "task 3")

if __name__ == "__main__":
    unittest.main()