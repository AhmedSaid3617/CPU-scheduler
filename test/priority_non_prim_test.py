import unittest
from core.schedulers.Priority_non_prem import Priority_non_prem_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from core.common.Priority_Task import Priority_Task

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


if __name__ == '__main__':
    unittest.main()

def test_equal_priority_fcfs_order(self):
    """Tests that tasks with equal priority execute in first-come-first-served order"""
    sch = Priority_non_prem_Scheduler()
    sim = Simulator(sch)
    
    # All tasks have same priority (2)
    t1 = Priority_Task(name="T1", arr_time=0, burst_time=3, priority=2)
    t2 = Priority_Task(name="T2", arr_time=1, burst_time=2, priority=2)
    t3 = Priority_Task(name="T3", arr_time=2, burst_time=1, priority=2)
    
    sim.load(t1)
    self.assertEqual(sim.advance().name, "T1")  # Time 0-1
    
    sim.load(t2)
    self.assertEqual(sim.advance().name, "T1")  # Time 1-2
    
    sim.load(t3)
    self.assertEqual(sim.advance().name, "T1")  # Time 2-3 (T1 completes)
    
    # Should continue with T2 then T3 (FCFS order)
    self.assertEqual(sim.advance().name, "T2")  # Time 3-4
    self.assertEqual(sim.advance().name, "T2")  # Time 4-5 (T2 completes)
    self.assertEqual(sim.advance().name, "T3")  # Time 5-6 (T3 completes)
    self.assertIsNone(sim.advance())            # No more tasks
