import unittest
from core.schedulers.Priority_non_prem import Priority_non_prem_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from core.common.Priority_Task import Priority_Task
from core.common.SchedulerStats import SchedulerStats


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sch = Priority_non_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Priority_Task(name="task 1",arr_time=0, burst_time=3,priority=2))
        self.assertEqual(sim.advance().name, "task 1")
        sim.load(Priority_Task(name="task 2", arr_time=1, burst_time=5,priority=1))
        self.assertEqual(sim.advance().name, "task 1")

        sim.load(Priority_Task(name="task 3", arr_time=2, burst_time=3))

        self.assertEqual(sim.advance().name, "task 1")

        # advance returns task that runs currently and moves 1 second forward

        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 2")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance(), None)  # no task in queue Returns None

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertAlmostEqual(result["avg_turnaround"], 6.33, places=2)
        self.assertAlmostEqual(result["avg_waiting"], 8/3)
        self.assertAlmostEqual(result["avg_response"], 8/3)

    def test_2(self):
        sch = Priority_non_prem_Scheduler()
        sim = Simulator(sch)
        sim.load(Priority_Task(name="task 1", arr_time=0, burst_time=3, priority=2))
        sim.load(Priority_Task(name="task 2", arr_time=0, burst_time=5, priority=1))
        sim.load(Priority_Task(name="task 3", arr_time=2, burst_time=3))
        sim.load(Priority_Task(name="task 4", arr_time=2, burst_time=7, priority=4))

        for i in range(5):
            self.assertEqual(sim.advance().name, "task 2")

        for i in range(3):
            self.assertEqual(sim.advance().name, "task 1")

        for i in range(7):
            self.assertEqual(sim.advance().name, "task 4")

        for i in range(3):
            self.assertEqual(sim.advance().name, "task 3")

        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertAlmostEqual(result["avg_turnaround"], 10.5)
        self.assertAlmostEqual(result["avg_waiting"], 6)
        self.assertAlmostEqual(result["avg_response"], 6)

    def test_3(self):
        sch = Priority_non_prem_Scheduler()
        sim = Simulator(sch)
        sim.load(Priority_Task(name="task 1", arr_time=0, burst_time=3, priority=2))
        sim.load(Priority_Task(name="task 2", arr_time=0, burst_time=5, priority=1))
        sim.load(Priority_Task(name="task 3", arr_time=2, burst_time=3))
        sim.load(Priority_Task(name="task 4", arr_time=11, burst_time=7, priority=4))

        for i in range(5):
            self.assertEqual(sim.advance().name, "task 2")

        for i in range(3):
            self.assertEqual(sim.advance().name, "task 1")

        for i in range(3):
            self.assertEqual(sim.advance().name, "task 3")

        for i in range(7):
            self.assertEqual(sim.advance().name, "task 4")

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertAlmostEqual(result["avg_turnaround"], 7.25)
        self.assertAlmostEqual(result["avg_waiting"], 2.75)
        self.assertAlmostEqual(result["avg_response"], 2.75)

    def test_4(self):
        sch = Priority_non_prem_Scheduler()
        sim = Simulator(sch)

        self.assertEqual(sim.advance(), None)
        self.assertEqual(sim.advance(), None)
        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertEqual(result["avg_turnaround"], 0)
        self.assertAlmostEqual(result["avg_waiting"], 0)
        self.assertAlmostEqual(result["avg_response"], 0)


if __name__ == '__main__':
    unittest.main()
