import unittest
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task

class TestFCFS(unittest.TestCase):
    def test_case_1(self):
        """Test FCFS scheduler with basic task loading and scheduling."""
        sch = FCFS_Scheduler()
        sim = Simulator(sch)
        tasks_list = [Task(name="task 1", arr_time=0, burst_time=1),
                      Task(name="task 2", arr_time=1, burst_time=1),
                      Task(name="task 3", arr_time=2, burst_time=1)]
        
        sim.load_bulk(tasks_list)

        # advance returns task that runs currently and moves 1 second forward
        self.assertEqual(sim.advance(), tasks_list[0])
        self.assertEqual(sim.advance(), tasks_list[1])
        self.assertEqual(sim.advance(), tasks_list[2])
        self.assertEqual(sim.advance(), None) # no task in queue Returns None

    def test_case_2(self):
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        tasks_list = [Task(name="task 1", arr_time=0, burst_time=1),
                      Task(name="task 2", arr_time=1, burst_time=7),
                      Task(name="task 3", arr_time=2, burst_time=1)]
        
        sim.load_bulk(tasks_list)
        
        self.assertEqual(sim.advance(), tasks_list[0])

        for i in range(6):
            sim.advance()
        
        self.assertEqual(sim.advance(), tasks_list[1])
        self.assertEqual(sim.advance(), tasks_list[2])
    
    def test_case_3(self):
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        tasks_list = [Task(name="task 1", arr_time=2, burst_time=4),
                      Task(name="task 2", arr_time=3, burst_time=3),
                      Task(name="task 3", arr_time=2, burst_time=8)]

        sim.load_bulk(tasks_list)

        self.assertEqual(sim.advance(), None)
        self.assertEqual(sim.advance(), None)

        self.assertEqual(sim.advance(), tasks_list[0])

        for i in range(4):
            sim.advance()

        self.assertEqual(sim.advance(), tasks_list[2])

        for i in range(8):
            sim.advance()

        self.assertEqual(sim.advance(), tasks_list[1])

        for i in range(3):
            sim.advance()

        self.assertEqual(sim.advance(), None)

    def test_case_4(self):
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        tasks_list = [Task(name="task 1", arr_time=2, burst_time=4),
                      Task(name="task 2", arr_time=3, burst_time=3),
                      Task(name="task 3", arr_time=2, burst_time=8)]

        sim.load_bulk(tasks_list)

        for i in range(4 + 3 + 8 + 2):
            sim.advance()

        self.assertTrue(sim.history_matches([
            None,
            None,
            tasks_list[0],
            tasks_list[0],
            tasks_list[0],
            tasks_list[0],
            tasks_list[2],
            tasks_list[2],
            tasks_list[2],
            tasks_list[2],
            tasks_list[2],
            tasks_list[2],
            tasks_list[2],
            tasks_list[2],
            tasks_list[1],
            tasks_list[1],
            tasks_list[1],
        ]))

if __name__ == "__main__":
    unittest.main()

def test_case_5(self):  # Tasks arriving during execution
    sch = FCFS_Scheduler()
    sim = Simulator(sch)
    task_list = [
        Task(name="T1", arr_time=0, burst_time=5),
        Task(name="T2", arr_time=3, burst_time=4),
        Task(name="T3", arr_time=6, burst_time=2)
    ]
    sim.load_bulk(task_list)
    for _ in range(11):  # Total runtime: T1(5) + T2(4) + T3(2) = 11
        sim.advance()
    # Expected: T1 (0-5), T2 (5-9), T3 (9-11)
    self.assertTrue(sim.history_matches(
        [task_list[0]]*5 + [task_list[1]]*4 + [task_list[2]]*2
    ))
    stat = SchedulerStats()
    result = sim.accept(stat)
    # T1: arrived at 0, started at 0, finished at 5
    self.assertEqual(result["turnaround"][task_list[0]], 5)  # 5-0
    self.assertEqual(result["waiting"][task_list[0]], 0)     # 5-5
    # T2: arrived at 3, started at 5, finished at 9
    self.assertEqual(result["turnaround"][task_list[1]], 6)  # 9-3
    self.assertEqual(result["waiting"][task_list[1]], 2)     # 6-4
    # T3: arrived at 6, started at 9, finished at 11
    self.assertEqual(result["turnaround"][task_list[2]], 5)  # 11-6
    self.assertEqual(result["waiting"][task_list[2]], 3)     # 5-2
    self.assertAlmostEqual(result["avg_turnaround"], 5.333, places=3)  # (5+6+5)/3
    self.assertAlmostEqual(result["avg_waiting"], 1.666, places=3)     # (0+2+3)/3

def test_case_6(self):  # Mixed scenario with idle time
    sch = FCFS_Scheduler()
    sim = Simulator(sch)
    task_list = [
        Task(name="T1", arr_time=2, burst_time=3),
        Task(name="T2", arr_time=0, burst_time=2),
        Task(name="T3", arr_time=7, burst_time=4)
    ]
    sim.load_bulk(task_list)
    for _ in range(11):  # Timeline: idle(0-0), T2(0-2), idle(2-2), T1(2-5), idle(5-7), T3(7-11)
        sim.advance()
    # Expected: T2 (0-2), T1 (2-5), T3 (7-11)
    # Note: Need to handle idle time in history_matches or adjust test
    stat = SchedulerStats()
    result = sim.accept(stat)
    # T2: arrived at 0, started at 0, finished at 2
    self.assertEqual(result["turnaround"][task_list[1]], 2)  # 2-0
    self.assertEqual(result["waiting"][task_list[1]], 0)     # 2-2
    # T1: arrived at 2, started at 2, finished at 5
    self.assertEqual(result["turnaround"][task_list[0]], 3)  # 5-2
    self.assertEqual(result["waiting"][task_list[0]], 0)     # 3-3
    # T3: arrived at 7, started at 7, finished at 11
    self.assertEqual(result["turnaround"][task_list[2]], 4)  # 11-7
    self.assertEqual(result["waiting"][task_list[2]], 0)     # 4-4
    self.assertAlmostEqual(result["avg_turnaround"], 3)      # (2+3+4)/3
    self.assertAlmostEqual(result["avg_waiting"], 0)         # (0+0+0)/3
