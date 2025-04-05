import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from core.common.Task import Task

class TaskManagerApp:
    ENTRY_WIDTH = 15
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Task Manager")
        self.root.geometry("900x600")
        self.tasks_list = []

        # Configure grid columns to match Treeview column widths
        root.grid_columnconfigure(0, weight=0)  # Column 0 stays compact
        root.grid_columnconfigure(1, weight=0)  # Column 1 stays compact
        root.grid_columnconfigure(2, weight=0)  # Column 2 stays compact

        # Dropdown menu for choosing scheduler type.
        chosen_scheduler = tk.StringVar()
        scheduler_menu = ttk.OptionMenu(root, chosen_scheduler, "Scheduler Type", "FCFS", "SJF")
        scheduler_menu.config(width=20)
        scheduler_menu.grid(row=0, column=0, padx=10, pady=20, sticky="W")

        # Task labels
        frame_task_input = tk.Frame()
        task_name_label = tk.Label(frame_task_input, text="Task Name")
        burst_time_label = tk.Label(frame_task_input, text="Burst Time")
        arr_time_label = tk.Label(frame_task_input, text="Arrival Time")
        priority_label = tk.Label(frame_task_input, text="Priority")

        frame_task_input.grid(row=1, column=0, padx=10, pady=10, sticky="w", columnspan=3)
        task_name_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")
        burst_time_label.grid(row=0, column=1, padx=10, pady=0, sticky="w")
        arr_time_label.grid(row=0, column=2, padx=10, pady=0, sticky="w")
        priority_label.grid(row=0, column=3, padx=10, pady=0, sticky="w")
        

        # Task input
        self.entry_task_name = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        self.entry_burst_time = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        self.entry_arr_time = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        self.entry_priority = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        button_task_input = tk.Button(frame_task_input, text="Add Task", command=self.add_task)

        self.entry_task_name.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")
        self.entry_burst_time.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="w")
        self.entry_arr_time.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="w")
        self.entry_priority.grid(row=1, column=3, padx=10, pady=(0, 10), sticky="w")
        button_task_input.grid(row=1, column=5, padx=10, pady=(0, 10), sticky="w")

        # Task table
        self.task_tree = ttk.Treeview(root, columns=('Name', 'Burst Time', 'Arrival Time', 'Priority'), show='headings')
        self.task_tree.heading('Name', text='Task Name')
        self.task_tree.heading('Burst Time', text='Burst Time')
        self.task_tree.heading('Arrival Time', text='Arrival Time')
        self.task_tree.heading('Priority', text='Priority')

        self.task_tree.column('Name', width=150)
        self.task_tree.column('Burst Time', width=150)
        self.task_tree.column('Arrival Time', width=150)
        self.task_tree.column('Priority', width=150)
        self.task_tree.grid(row=2, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="nsew")

    def add_task(self):
        try:
            new_task = Task(self.entry_task_name.get(), int(self.entry_arr_time.get()), int(self.entry_arr_time.get()))
            for task in self.tasks_list:
                if task.name == new_task.name:
                    messagebox.showwarning(title="Duplicate Tasks", message="Please enter unique task names.")
                    return
            self.tasks_list.append(new_task)
            self.task_tree.insert('', 'end', values=(new_task.name, new_task.burst_time, new_task.arr_time, new_task.priority))
        except TypeError:
            messagebox.showerror(title="Input Error", message="Incorrect parameters in task input.")
        print("Clicked")
        ...

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()