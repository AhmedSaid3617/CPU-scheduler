import tkinter as tk
from tkinter import ttk
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from Gui.Gannt import Gannt
from Gui.Tree import Tree
from core.utils import is_finished
from Gui.Statistics_Window import StatisticsWindow
from core.common.SchedulerStats import SchedulerStats

class SchedulerApp(tk.Toplevel):
    def __init__(self, simulator:Simulator, live:bool):
        super().__init__()
        self.title("CPU Scheduler - Process Table")
        self.geometry("990x1030+920+50")
        self.current_time = 0
        self.task_list = []
        self.simulator = simulator
        self.live = live

        self.setup_ui()
        self.setup_simulation()

    def setup_ui(self):
        self.top_frame = ttk.Frame(self)
        self.bottom_frame = ttk.Frame(self)

        self.top_frame.pack(side="top", fill="both", expand=True)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)

        self.tree = Tree(self.top_frame)
        self.tree.create_tree()

        self.chart = Gannt(self.bottom_frame)
        self.chart.create_gantt_chart(0, [])

    def setup_simulation(self):

        self.total_time = sum(task.burst_time for tasks in self.simulator.batch.values() for task in tasks)
        for tasks in self.simulator.batch.values():
            for task in tasks:
                self.tree.add(task)

        self.run()

    def run(self):
        if self.current_time == 0:
            self.after(1000, self.run)
            self.current_time += 1
        else:
            if not is_finished(self.simulator): 
                self.after(1000, self.run)  # Schedule next tick
                task = self.simulator.advance()
                if task:
                    self.tree.update(task.name)
                    self.task_list.append(task.name)
                else:
                    self.task_list.append("Idle")
                self.chart.create_gantt_chart(self.current_time, self.task_list)
                self.current_time += 1
            else:
                stat = SchedulerStats()
                result = self.simulator.accept(stat)
                StatisticsWindow(result["avg_turnaround"], result["avg_waiting"], result["avg_response"])




if __name__ == "__main__":
    SchedulerApp()

