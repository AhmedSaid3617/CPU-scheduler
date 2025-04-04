import unittest
from core.schedulers.SJF_prem import SJF_prem_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sch = SJF_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Task(name="task 1",arr_time=0, burst_time=3))
        self.assertEqual(sim.advance(), "task 1")
        sim.load(Task(name="task 2", arr_time=1, burst_time=1))
        self.assertEqual(sim.advance(), "task 2")
        sim.load  (Task(name="task 3", arr_time=2, burst_time=3))
        self.assertEqual(sim.advance(), "task 1")


        # advance returns task that runs currently and moves 1 second forward

        self.assertEqual(sim.advance(), "task 1")
        self.assertEqual(sim.advance(), "task 3")
        self.assertEqual(sim.advance(), "task 3")
        self.assertEqual(sim.advance(), "task 3")
        self.assertEqual(sim.advance(), None)  # no task in queue Returns None


if __name__ == '__main__':
    unittest.main()
