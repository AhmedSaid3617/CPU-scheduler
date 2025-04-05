import tkinter as tk
from tkinter import ttk
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from Gannt import Gannt
from Tree import Tree


class SchedulerApp:
    def __init__(self, simulator:Simulator):
        self.root = tk.Tk()
        self.root.title("CPU Scheduler - Process Table")
        self.root.geometry("2000x2000")
        self.current_time = 0
        self.task_list = []
        self.simulator = simulator

        self.setup_ui()
        self.setup_simulation()
        self.root.mainloop()

    def setup_ui(self):
        self.top_frame = ttk.Frame(self.root)
        self.bottom_frame = ttk.Frame(self.root)

        self.top_frame.pack(side="top", fill="both", expand=True)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)

        self.tree = Tree(self.top_frame)
        self.tree.create_tree()

        self.chart = Gannt(self.bottom_frame)
        self.chart.create_gantt_chart(0, [])

    def setup_simulation(self):

        #self.simulator.load_bulk(tasks)

        self.total_time = sum(task.burst_time for tasks in self.simulator.batch.values() for task in tasks)
        for tasks in self.simulator.batch.values():
            for task in tasks:
                self.tree.add(task)

        self.run()

    def run(self):
        if self.current_time == 0:
            self.root.after(1000,self.run)
            self.current_time += 1
        elif self.current_time <= self.total_time:
            self.root.after(1000, self.run)  # Schedule next tick

            task = self.simulator.advance()
            if task:
                self.tree.update(task.name)
                self.task_list.append(task.name)
                print(self.task_list)
                self.chart.create_gantt_chart(self.current_time, self.task_list)

            self.current_time += 1


if __name__ == "__main__":
    SchedulerApp()
