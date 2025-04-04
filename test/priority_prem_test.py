import unittest
from core.schedulers.Priority_prem import Priority_prem_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from core.common.Priority_Task import Priority_Task

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sch = Priority_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Priority_Task(name="task 1",arr_time=0, burst_time=3,priority=2))
        self.assertEqual(sim.advance().name, "task 1")
        sim.load(Priority_Task(name="task 2", arr_time=1, burst_time=5,priority=1))
        self.assertEqual(sim.advance().name, "task 2")

        sim.load(Priority_Task(name="task 3", arr_time=2, burst_time=3))

        self.assertEqual(sim.advance().name, "task 2")


        # advance returns task that runs currently and moves 1 second forward

        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 1")
        self.assertEqual(sim.advance().name, "task 1")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance(), None)  # no task in queue Returns None


if __name__ == '__main__':
    unittest.main()
