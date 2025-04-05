import unittest
from core.schedulers.SJF_non_prem import SJF_non_prem_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sch = SJF_non_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Task(name="task 1",arr_time=0, burst_time=3))

        self.assertEqual(sim.advance().name, "task 1")
        self.assertEqual(sim.advance().name, "task 1")

        sim.load_bulk([
            Task(name="task 2", arr_time=2, burst_time=2),
            Task(name="task 3", arr_time=3, burst_time=3)
        ])
        self.assertEqual(sim.advance().name, "task 1")


        # advance returns task that runs currently and moves 1 second forward

        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance(), None)  # no task in queue Returns None


if __name__ == '__main__':
    unittest.main()
