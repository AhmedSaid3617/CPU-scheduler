import tkinter as tk
from tkinter import ttk
from core.schedulers.FCFS_Schedule import FCFS_Scheduler
from core.common.Simulator import Simulator
from core.common.Task import Task
from Gannt import Gannt
from Tree import Tree

def merge():
    root = tk.Tk()
    root.title("CPU Scheduler - Process Table")
    root.geometry("2000x2000")
    top_frame = ttk.Frame(root)
    bottom_frame = ttk.Frame(root)

    top_frame.pack(side="top",fill="both",expand=True)
    bottom_frame.pack(side="bottom", fill="both",expand=True)

    tree = Tree(top_frame)
    tree.create_tree()
    chart=Gannt(bottom_frame)
    chart.create_gantt_chart(0,[])

    sch = FCFS_Scheduler()
    sim = Simulator(sch)
    tasks_list = [Task(name="task 1", arr_time=0, burst_time=1),
                  Task(name="task 2", arr_time=1, burst_time=7),
                  Task(name="task 3", arr_time=2, burst_time=1)]
    sim.load_bulk(tasks_list)
    total_time, current_time = 0, 0
    for task in tasks_list:
        tree.add(task)
        total_time += task.burst_time
    list = []
    run(current_time, 20, root, tree, chart, sim, list)

    root.mainloop()


def run(current_time,total_time,root,tree,chart,sim,list):
    if current_time ==0:
        root.after(1000, run, current_time + 1, total_time, root, tree, chart,sim,list)
    elif current_time <= total_time:
        root.after(1000, run, current_time + 1, total_time, root,tree,chart,sim,list)
        task=sim.advance()
        if task:
            tree.update(task.name)
            list.append(task.name)
            print(list)
            chart.create_gantt_chart(current_time,list)


if __name__ == "__main__":
    merge()