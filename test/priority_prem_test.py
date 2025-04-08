import unittest
from core.schedulers.Priority_prem import Priority_prem_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from core.common.Priority_Task import Priority_Task
from core.common.SchedulerStats import SchedulerStats


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sch = Priority_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Priority_Task(name="task 1", arr_time=0, burst_time=3,priority=2))
        sim.load(Priority_Task(name="task 2", arr_time=1, burst_time=5,priority=1))
        sim.load(Priority_Task(name="task 3", arr_time=2, burst_time=3))

        # advance returns task that runs currently and moves 1 second forward

        self.assertEqual(sim.advance().name, "task 1")
        for i in range(5):
            self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 1")
        self.assertEqual(sim.advance().name, "task 1")
        for i in range(3):
            self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance(), None)  # no task in queue Returns None

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertAlmostEqual(result["avg_turnaround"], 22/3)
        self.assertAlmostEqual(result["avg_waiting"], 11/3)
        self.assertAlmostEqual(result["avg_response"], 2)

    def test_2(self):
        sch = Priority_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Priority_Task(name="task 1", arr_time=0, burst_time=3, priority=2))
        sim.load(Priority_Task(name="task 2", arr_time=0, burst_time=5, priority=1))
        sim.load(Priority_Task(name="task 3", arr_time=0, burst_time=3))
        sim.load(Priority_Task(name="task 4", arr_time=8, burst_time=5, priority=1))

        for i in range(5):
            self.assertEqual(sim.advance().name, "task 2")
        for i in range(3):
            self.assertEqual(sim.advance().name, "task 1")
        for i in range(5):
            self.assertEqual(sim.advance().name, "task 4")
        for i in range(3):
            self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertAlmostEqual(result["avg_turnaround"], 8.5)
        self.assertAlmostEqual(result["avg_waiting"], 18/4)
        self.assertAlmostEqual(result["avg_response"], 18/4)

    def test_3(self):
        sch = Priority_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Priority_Task(name="task 1", arr_time=0, burst_time=3, priority=4))
        sim.load(Priority_Task(name="task 2", arr_time=1, burst_time=5, priority=3))
        sim.load(Priority_Task(name="task 3", arr_time=2, burst_time=3, priority=2))
        sim.load(Priority_Task(name="task 4", arr_time=3, burst_time=5, priority=1))

        self.assertEqual(sim.advance().name, "task 1")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 3")

        for i in range(5):
            self.assertEqual(sim.advance().name, "task 4")

        for i in range(2):
            self.assertEqual(sim.advance().name, "task 3")

        for i in range(4):
            self.assertEqual(sim.advance().name, "task 2")

        for i in range(2):
            self.assertEqual(sim.advance().name, "task 1")

        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertAlmostEqual(result["avg_turnaround"], 6.5)
        self.assertAlmostEqual(result["avg_waiting"], 6.5)
        self.assertAlmostEqual(result["avg_response"], 0)

    def test_3(self):
        sch = Priority_prem_Scheduler()
        sim = Simulator(sch)

        self.assertEqual(sim.advance(), None)
        self.assertEqual(sim.advance(), None)
        self.assertEqual(sim.advance(), None)
        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertAlmostEqual(result["avg_turnaround"], 0)
        self.assertAlmostEqual(result["avg_waiting"], 0)
        self.assertAlmostEqual(result["avg_response"], 0)


if __name__ == '__main__':
    unittest.main()
