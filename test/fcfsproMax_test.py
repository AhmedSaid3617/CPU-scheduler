import unittest
from core.common.SchedulerStats import SchedulerStats
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task

class TestFCFS(unittest.TestCase):
    
    def test_case_1(self):  #Processes arriving at the same time
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        task_list = [Task(name="T1",arr_time=0, burst_time=5),Task(name="T2",arr_time=0, burst_time=3)]
        sim.load_bulk(task_list)
        for i in range (8):
            sim.advance()
        
        # Expected behavior : T1 0->5 , T2 5->8
        self.assertTrue(sim.history_matches([task_list[0]]*5 + [task_list[1]]*3))
        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertEqual(result["turnaround"][task_list[0]],5)
        self.assertEqual(result["waiting"][task_list[0]],0)
        self.assertEqual(result["turnaround"][task_list[1]],8)
        self.assertEqual(result["waiting"][task_list[1]],5)

        self.assertAlmostEqual(result["avg_turnaround"], 6.5)
        self.assertAlmostEqual(result["avg_waiting"], 2.5)

###########################################

    def test_case_2(self):  # Process with zero burst time
        sch = FCFS_Scheduler()
        sim = Simulator(sch)

        task_list = [Task(name="T1",arr_time=0, burst_time=0),Task(name="T2",arr_time=1, burst_time=3)]
        sim.load_bulk(task_list)
        for i in range (4):
            sim.advance()
        
        # Expected behavior : T1 0->0 , T2 1->4
        #self.assertTrue(sim.history_matches([task_list[0]] + [task_list[1]]*3))
        stat = SchedulerStats()
        result = sim.accept(stat)

        self.assertEqual(result["turnaround"][task_list[0]],0)
        self.assertEqual(result["waiting"][task_list[0]],0)
        self.assertEqual(result["turnaround"][task_list[1]],3)
        self.assertEqual(result["waiting"][task_list[1]],0)

        self.assertAlmostEqual(result["avg_turnaround"], 1.5)
        self.assertAlmostEqual(result["avg_waiting"], 0)


    #def test_case_3(self):

    
    ########################################################
    # def test_case_(self): 
    #     sch = FCFS_Scheduler()
    #     sim = Simulator(sch)

    #     task_list = [Task(name="T1",arr_time=0, burst_time=7),Task(name="T2",arr_time=2, burst_time=1)]
    #     sim.load_bulk(task_list)
    #     for i in range (10):
    #         sim.advance()

    #     self.assertTrue(sim.history_matches([task_list[0]]*7 + [task_list[1]]*1))
    #     stat = SchedulerStats()
    #     result = sim.accept(stat)
    #     self.assertEqual(result["turnaround"][task_list[0]],7)

    #     #self.assertEqual(task.name , "T2")

        