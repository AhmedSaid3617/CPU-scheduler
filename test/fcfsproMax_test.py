import unittest
from core.common.SchedulerStats import SchedulerStats
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task

class TestFCFS(unittest.TestCase):
    def test_case_1(self):  # Processes arriving at the same time
        sch = FCFS_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=5), Task(name="T2", arr_time=0, burst_time=3)]
        sim.load_bulk(task_list)
        for _ in range(8):
            sim.advance()
        # Expected: T1 (0-5), T2 (5-8)
        self.assertTrue(sim.history_matches([task_list[0]]*5 + [task_list[1]]*3))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 5)  # 5-0
        self.assertEqual(result["waiting"][task_list[0]], 0)     # 5-5
        self.assertEqual(result["turnaround"][task_list[1]], 8)  # 8-0
        self.assertEqual(result["waiting"][task_list[1]], 5)     # 8-3
        self.assertAlmostEqual(result["avg_turnaround"], 6.5)   # (5+8)/2
        self.assertAlmostEqual(result["avg_waiting"], 2.5)      # (0+5)/2

    def test_case_2(self):  # Process with zero burst time
        sch = FCFS_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=0), Task(name="T2", arr_time=1, burst_time=3)]
        sim.load_bulk(task_list)
        for _ in range(4):
            sim.advance()  
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 0)  # 0-0
        self.assertEqual(result["waiting"][task_list[0]], 0)     # 0-0
        self.assertEqual(result["turnaround"][task_list[1]], 3)  # 4-1
        self.assertEqual(result["waiting"][task_list[1]], 0)     # 3-3
        self.assertAlmostEqual(result["avg_turnaround"], 1.5)   # (0+3)/2
        self.assertAlmostEqual(result["avg_waiting"], 0)        # (0+0)/2

    def test_case_3(self):  # Single process
        sch = FCFS_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=10)]
        sim.load_bulk(task_list)
        for _ in range(10):
            sim.advance()
        # Expected: T1 (0-10)
        self.assertTrue(sim.history_matches([task_list[0]]*10))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 10)  # 10-0
        self.assertEqual(result["waiting"][task_list[0]], 0)      # 10-10
        self.assertAlmostEqual(result["avg_turnaround"], 10)      # (10)/1
        self.assertAlmostEqual(result["avg_waiting"], 0)          # (0)/1

    def test_case_4(self):  # Very large burst time
        sch = FCFS_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=1000), Task(name="T2", arr_time=1, burst_time=3)]
        sim.load_bulk(task_list)
        for _ in range(1003):  # Simulate full duration
            sim.advance()
        # Expected: T1 (0-1000), T2 (1000-1003)
        self.assertTrue(sim.history_matches([task_list[0]]*1000 + [task_list[1]]*3))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 1000)  # 1000-0
        self.assertEqual(result["waiting"][task_list[0]], 0)        # 1000-1000
        self.assertEqual(result["turnaround"][task_list[1]], 1002)  # 1003-1
        self.assertEqual(result["waiting"][task_list[1]], 999)      # 1002-3
        self.assertAlmostEqual(result["avg_turnaround"], 1001)      # (1000+1002)/2
        self.assertAlmostEqual(result["avg_waiting"], 499.5)        # (0+999)/2

    def test_case_5(self): # Random sequence
        sch = FCFS_Scheduler()
        sim = Simulator(sch)
        task_list = [Task(name="T1", arr_time=0, burst_time=5), Task(name="T2", arr_time=2, burst_time=3), Task(name="T3", arr_time=4, burst_time=1)]
        sim.load_bulk(task_list)
        for _ in range(9):
            sim.advance()
        # Expected: T1 (0-5), T2 (5-8), T3 (8-9)
        self.assertTrue(sim.history_matches([task_list[0]]*5 + [task_list[1]]*3 + [task_list[2]]*1))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]], 5)  # 5-0
        self.assertEqual(result["waiting"][task_list[0]], 0)     # 5-5
        self.assertEqual(result["turnaround"][task_list[1]], 6)  # 8-2
        self.assertEqual(result["waiting"][task_list[1]], 3)     # 6-3
        self.assertEqual(result["turnaround"][task_list[2]], 5)  # 9-4
        self.assertEqual(result["waiting"][task_list[2]], 4)     # 5-1
        self.assertAlmostEqual(result["avg_turnaround"], 5.333, places=3)  # (5+6+5)/3
        self.assertAlmostEqual(result["avg_waiting"], 2.333, places=3)     # (0+3+4)/3


        