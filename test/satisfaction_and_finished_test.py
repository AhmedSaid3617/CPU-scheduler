import unittest

from core.common.AreLoadedTasksSatisfied import AreLoadedTasksSatisfied
from core.common.Simulator import Simulator
from core.common.Task import Task
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.utils import is_finished


class TestSatisfactionAndFinished(unittest.TestCase):
    def test_case_1(self):
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        tasks_list = [
            Task(name="task 1", arr_time=0, burst_time=9),
            Task(name="task 2", arr_time=1, burst_time=4),
            Task(name="task 3", arr_time=2, burst_time=1)
        ]

        # No unloaded tasks (empty)
        self.assertTrue(sim.are_all_tasks_loaded())
        self.assertTrue(is_finished(sim))

        sim.load_bulk(tasks_list)

        # There are unloaded tasks
        self.assertFalse(sim.are_all_tasks_loaded())

        for i in range(2):
            sim.advance()

        # Simulator should have loaded all tasks
        self.assertTrue(sim.are_all_tasks_loaded())

        # Advance the simulation to finish all tasks
        for i in range(9 + 4 + 1 - 2):
            self.assertFalse(sim.accept(AreLoadedTasksSatisfied()))
            sim.advance()

        self.assertTrue(sim.accept(AreLoadedTasksSatisfied()))

        # Fast alternative
        self.assertTrue(is_finished(sim))

if __name__ == '__main__':
    unittest.main()