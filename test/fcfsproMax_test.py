import unittest
from core.common.SchedulerStats import SchedulerStats
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task

class TestFCFS(unittest.TestCase):
    def test_case_1(self):
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        task_list = [Task(name="T1",arr_time=0, burst_time=7),Task(name="T2",arr_time=2, burst_time=1)]
        sim.load_bulk(task_list)
        for i in range (10):
            sim.advance()

        # sim.history_matches([task_list[0]*7,task_list[1]*2]) 
        self.assertTrue(sim.history_matches([task_list[0]]*7 + [task_list[1]]*1))
        stat = SchedulerStats()
        result = sim.accept(stat)
        self.assertEqual(result["turnaround"][task_list[0]],7)

        #self.assertEqual(task.name , "T2")

        