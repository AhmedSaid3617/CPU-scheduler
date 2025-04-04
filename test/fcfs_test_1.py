import unittest
import sys
sys.path.insert(0, '..')
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task

class TestFCFS(unittest.TestCase):
    def test_basic_assertions(self):
        """Test FCFS scheduler with basic task loading and scheduling."""
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        sim.load(Task(name="task 1", burst_time=1))

        sim.load_bulk([
            Task(name="task 2", arr_time=1, burst_time=1),
            Task(name="task 3", arr_time=2, burst_time=1)
        ])

        # advance returns task that runs currently and moves 1 second forward
        self.assertEqual(sim.advance(), "task 1")
        self.assertEqual(sim.advance(), "task 2")
        self.assertEqual(sim.advance(), "task 3")
        self.assertEqual(sim.advance(), None) # no task in queue Returns None

if __name__ == "__main__":
    unittest.main()