import unittest
from core.schedulers.SJF_prem import SJF_prem_Scheduler
from core.common.Simulator import Simulator
from core.common.SchedulerStats import SchedulerStats
from core.common.Task import Task

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sch = SJF_prem_Scheduler()
        sim = Simulator(sch)

        sim.load(Task(name="task 1",arr_time=0, burst_time=3))
        self.assertEqual(sim.advance().name, "task 1")
        sim.load(Task(name="task 2", arr_time=1, burst_time=1))
        self.assertEqual(sim.advance().name, "task 2")
        sim.load  (Task(name="task 3", arr_time=2, burst_time=3))
        self.assertEqual(sim.advance().name, "task 1")


        # advance returns task that runs currently and moves 1 second forward

        self.assertEqual(sim.advance().name, "task 1")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance().name, "task 3")
        self.assertEqual(sim.advance(), None)  # no task in queue Returns None

    def test_case_1(self):  # Shorter process arrives while a longer one is running
        sch = SJF_prem_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=10), Task(name="T2", arr_time=2, burst_time=4)]
        sim.load_bulk(task_list)
        for _ in range(14):
            sim.advance()
        # Expected: T1 (0-2), T2 (2-6), T1 (6-14)
        self.assertTrue(sim.history_matches([task_list[0]]*2 + [task_list[1]]*4 + [task_list[0]]*8))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 14)
        self.assertEqual(result["waiting"][task_list[0]], 4)
        self.assertEqual(result["turnaround"][task_list[1]], 4)
        self.assertEqual(result["waiting"][task_list[1]], 0)
        self.assertAlmostEqual(result["avg_turnaround"], 9)
        self.assertAlmostEqual(result["avg_waiting"], 2)

    def test_case_2(self):  # Multiple processes arriving at the same time
        sch = SJF_prem_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=5), Task(name="T2", arr_time=0, burst_time=3), Task(name="T3", arr_time=0, burst_time=4)]
        sim.load_bulk(task_list)
        for _ in range(12):
            sim.advance()
        # Expected: T2 (0-3), T3 (3-7), T1 (7-12)
        self.assertTrue(sim.history_matches([task_list[1]]*3 + [task_list[2]]*4 + [task_list[0]]*5))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 12)
        self.assertEqual(result["waiting"][task_list[0]], 7)
        self.assertEqual(result["turnaround"][task_list[1]], 3)
        self.assertEqual(result["waiting"][task_list[1]], 0)
        self.assertEqual(result["turnaround"][task_list[2]], 7)
        self.assertEqual(result["waiting"][task_list[2]], 3)
        self.assertAlmostEqual(result["avg_turnaround"], 7.333, places=3)
        self.assertAlmostEqual(result["avg_waiting"], 3.333, places=3)

    def test_case_3(self):  # Frequent arrivals of short processes
        sch = SJF_prem_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=10), Task(name="T2", arr_time=1, burst_time=2), Task(name="T3", arr_time=2, burst_time=1)]
        sim.load_bulk(task_list)
        for _ in range(14):
            sim.advance()
        # Expected: T1 (0-1), T2 (1-3), T3 (3-4), T1 (4-13)
        self.assertTrue(sim.history_matches([task_list[0]]*1 + [task_list[1]]*2 + [task_list[2]]*1 + [task_list[0]]*9))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 13)
        self.assertEqual(result["waiting"][task_list[0]], 3)
        self.assertEqual(result["turnaround"][task_list[1]], 2)
        self.assertEqual(result["waiting"][task_list[1]], 0)
        self.assertEqual(result["turnaround"][task_list[2]], 2)
        self.assertEqual(result["waiting"][task_list[2]], 1)
        self.assertAlmostEqual(result["avg_turnaround"], 5.666, places=2)
        self.assertAlmostEqual(result["avg_waiting"], 1.333, places=3)


if __name__ == '__main__':
    unittest.main()
