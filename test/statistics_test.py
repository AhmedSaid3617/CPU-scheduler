import unittest

from core.common.AreLoadedTasksSatisfied import AreLoadedTasksSatisfied
from core.common.Simulator import Simulator
from core.common.SchedulerStats import SchedulerStats
from core.common.Task import Task
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.schedulers.SJF_prem import SJF_prem_Scheduler
from core.utils import is_finished

class TestStatistics(unittest.TestCase):
    def test_case_1(self):
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        tasks_list = [
            Task(name="task 1", arr_time=0, burst_time=9),
            Task(name="task 2", arr_time=1, burst_time=4),
            Task(name="task 3", arr_time=2, burst_time=1)
        ]

        sim.load_bulk(tasks_list)

        # Make sure all tasks are served and done
        for i in range(100):
            sim.advance()

        stat = SchedulerStats()

        result = sim.accept(stat)

        self.assertEqual(result["avg_turnaround"], 11.0)
        self.assertAlmostEqual(result["avg_waiting"], 6.33, places=2)
        self.assertAlmostEqual(result["avg_response"], 6.33, places=2)
    

        

if __name__ == "__main__":
    unittest.main()