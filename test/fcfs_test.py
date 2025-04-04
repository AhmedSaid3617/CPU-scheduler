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

if __name__ == "__main__":
    unittest.main()