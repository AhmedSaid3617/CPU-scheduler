import unittest
from core.schedulers.RoundRobin import RoundRobinScheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from core.common.SchedulerStats import SchedulerStats


class MyTestCase(unittest.TestCase):

    def test_something(self):
        def test_equal(self, sim, name, quanta):
            for i in range(quanta):
                self.assertEqual(sim.advance().name, name)

        quanta = 3
        sch = RoundRobinScheduler(quanta)
        sim = Simulator(sch)

        sim.load(Task(name="task 1", arr_time=0, burst_time=7))
        sim.load(Task(name="task 2", arr_time=0, burst_time=10))
        sim.load(Task(name="task 3", arr_time=0, burst_time=15))
        sim.load(Task(name="task 4", arr_time=0, burst_time=8))

        # advance returns task that runs currently and moves 1 second forward
        test_equal(self, sim, "task 1", quanta)
        test_equal(self, sim, "task 2", quanta)
        test_equal(self, sim, "task 3", quanta)
        test_equal(self, sim, "task 4", quanta)
        test_equal(self, sim, "task 1", quanta)
        test_equal(self, sim, "task 2", quanta)
        test_equal(self, sim, "task 3", quanta)
        test_equal(self, sim, "task 4", quanta)
        self.assertEqual(sim.advance().name, "task 1")
        test_equal(self, sim, "task 2", quanta)
        test_equal(self, sim, "task 3", quanta)
        self.assertEqual(sim.advance().name, "task 4")
        self.assertEqual(sim.advance().name, "task 4")
        self.assertEqual(sim.advance().name, "task 2")
        test_equal(self, sim, "task 3", quanta)
        test_equal(self, sim, "task 3", quanta)
        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertEqual(result["avg_turnaround"], 33)
        self.assertAlmostEqual(result["avg_waiting"], 23)
        self.assertAlmostEqual(result["avg_response"], 4.5)

    def test_1(self):
        def test_equal(self, sim, name, quanta):
            for i in range(quanta):
                self.assertEqual(sim.advance().name, name)

        quanta = 7
        sch = RoundRobinScheduler(quanta)
        sim = Simulator(sch)

        sim.load(Task(name="task 1", arr_time=0, burst_time=7))
        sim.load(Task(name="task 2", arr_time=7, burst_time=14))
        sim.load(Task(name="task 3", arr_time=14, burst_time=7))
        sim.load(Task(name="task 4", arr_time=28, burst_time=3))

        test_equal(self, sim, "task 1", quanta)
        test_equal(self, sim, "task 2", quanta)
        test_equal(self, sim, "task 3", quanta)
        test_equal(self, sim, "task 2", quanta)
        self.assertEqual(sim.advance().name, "task 4")
        self.assertEqual(sim.advance().name, "task 4")
        self.assertEqual(sim.advance().name, "task 4")
        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertEqual(result["avg_turnaround"], 9.5)
        self.assertAlmostEqual(result["avg_waiting"], 1.75)
        self.assertAlmostEqual(result["avg_response"], 0)

    def test_2(self):
        quanta = 20
        sch = RoundRobinScheduler(quanta)
        sim = Simulator(sch)

        sim.load(Task(name="task 1", arr_time=0, burst_time=7))
        sim.load(Task(name="task 2", arr_time=7, burst_time=14))
        sim.load(Task(name="task 3", arr_time=14, burst_time=7))
        sim.load(Task(name="task 4", arr_time=30, burst_time=3))

        for i in range(7):
            self.assertEqual(sim.advance().name, "task 1")

        for i in range(14):
            self.assertEqual(sim.advance().name, "task 2")

        for i in range(7):
            self.assertEqual(sim.advance().name, "task 3")

        self.assertEqual(sim.advance(), None)
        self.assertEqual(sim.advance(), None)

        for i in range(3):
            self.assertEqual(sim.advance().name, "task 4")

        self.assertEqual(sim.advance(), None)

        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertEqual(result["avg_turnaround"], 9.5)
        self.assertAlmostEqual(result["avg_waiting"], 1.75)
        self.assertAlmostEqual(result["avg_response"], 1.75)

    def test_3(self):
        quanta = 20
        sch = RoundRobinScheduler(quanta)
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
