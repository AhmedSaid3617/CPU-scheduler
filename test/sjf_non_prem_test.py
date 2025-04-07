import unittest
from core.schedulers.SJF_non_prem import SJF_non_prem_Scheduler
from core.common.SchedulerStats import SchedulerStats
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

    def test_case_1(self):  # Equal burst times
        sch = SJF_non_prem_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=5), Task(name="T2", arr_time=0, burst_time=5)]
        sim.load_bulk(task_list)
        for _ in range(13):
            sim.advance()
        # Expected: T1 (0-5), T2 (5-10)
        self.assertTrue(sim.history_matches([task_list[0]]*5 + [task_list[1]]*5))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 5)
        self.assertEqual(result["waiting"][task_list[0]], 0)
        self.assertEqual(result["turnaround"][task_list[1]], 10)
        self.assertEqual(result["waiting"][task_list[1]], 5)
        self.assertAlmostEqual(result["avg_turnaround"], 7.5)
        self.assertAlmostEqual(result["avg_waiting"], 2.5)

    def test_case_2(self):  # Shorter process arrives just after a longer one starts
        sch = SJF_non_prem_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=10), Task(name="T2", arr_time=1, burst_time=2)]
        sim.load_bulk(task_list)
        for _ in range(12):
            sim.advance()
        # Expected: T1 (0-10), T2 (10-12)
        self.assertTrue(sim.history_matches([task_list[0]]*10 + [task_list[1]]*2))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 10)
        self.assertEqual(result["waiting"][task_list[0]], 0)
        self.assertEqual(result["turnaround"][task_list[1]], 11)
        self.assertEqual(result["waiting"][task_list[1]], 9)
        self.assertAlmostEqual(result["avg_turnaround"], 10.5)
        self.assertAlmostEqual(result["avg_waiting"], 4.5)

    def test_case_3(self):  # Mix of very short and very long burst times
        sch = SJF_non_prem_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=1), Task(name="T2", arr_time=0, burst_time=1000)]
        sim.load_bulk(task_list)
        for _ in range(1001):
            sim.advance()
        # Expected: T1 (0-1), T2 (1-1001)
        self.assertTrue(sim.history_matches([task_list[0]]*1 + [task_list[1]]*1000))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 1)
        self.assertEqual(result["waiting"][task_list[0]], 0)
        self.assertEqual(result["turnaround"][task_list[1]], 1001)
        self.assertEqual(result["waiting"][task_list[1]], 1)
        self.assertAlmostEqual(result["avg_turnaround"], 501)
        self.assertAlmostEqual(result["avg_waiting"], 0.5)
