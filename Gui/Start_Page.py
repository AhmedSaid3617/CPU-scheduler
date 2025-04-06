import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from core.common.Task import Task
from core.schedulers.FCFS_Schedule import *
from core.schedulers.Priority_non_prem import *
from core.schedulers.Priority_prem import *
from core.schedulers.SJF_non_prem import *
from core.schedulers.SJF_prem import *
from core.common.Simulator import Simulator
from Gui.Table_and_Gannt import SchedulerApp

class SchedulerNames:
    FCFS = str("FCFS")
    SJF_NON_PREM = str("SJF (Non-preemptive)")
    SRTF_PREM = str("SRTF (Preemptive)")
    PRIORITY_PREM = str("Priority (Preemptive)")
    PRIORITY_NON_PREM = str("Priority (Non-preemptive)")
    ROUND_ROBIN = str("Round Robin")


class TaskManagerApp(tk.Tk):
    ENTRY_WIDTH = 15
    def __init__(self):
        super().__init__()
        self.title("CPU Task Manager")
        self.geometry("910x570+0+50")
        self.tasks_list = []
        self.started_sim = False
        #self.scheduler_app = None

        # Configure grid columns to match Treeview column widths
        self.grid_columnconfigure(0, weight=0)  # Column 0 stays compact
        self.grid_columnconfigure(1, weight=0)  # Column 1 stays compact
        self.grid_columnconfigure(2, weight=0)  # Column 2 stays compact

        # Dropdown menu for choosing scheduler type.
        self.scheduler_types_strings = ["Scheduler Type", SchedulerNames.FCFS, SchedulerNames.SJF_NON_PREM, SchedulerNames.SRTF_PREM, SchedulerNames.PRIORITY_PREM, SchedulerNames.PRIORITY_NON_PREM, SchedulerNames.ROUND_ROBIN]
        self.chosen_scheduler = tk.StringVar()
        self.scheduler_menu = ttk.OptionMenu(self, self.chosen_scheduler, *self.scheduler_types_strings, command=self.update_options)
        self.scheduler_menu.config(width=20)
        self.scheduler_menu.grid(row=0, column=0, padx=10, pady=20, sticky="W")

        # Task labels
        frame_task_input = tk.Frame()
        task_name_label = tk.Label(frame_task_input, text="Task Name")
        burst_time_label = tk.Label(frame_task_input, text="Burst Time")
        arr_time_label = tk.Label(frame_task_input, text="Arrival Time")
        self.priority_label = tk.Label(frame_task_input, text="Priority")

        frame_task_input.grid(row=1, column=0, padx=10, pady=10, sticky="w", columnspan=5)
        task_name_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")
        burst_time_label.grid(row=0, column=1, padx=10, pady=0, sticky="w")
        arr_time_label.grid(row=0, column=2, padx=10, pady=0, sticky="w")
        

        # Task input
        self.entry_task_name = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        self.entry_burst_time = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        self.entry_arr_time = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        self.entry_priority = tk.Entry(frame_task_input, width=self.ENTRY_WIDTH)
        button_task_input = tk.Button(frame_task_input, text="Add Task", command=self.add_task)

        self.entry_task_name.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")
        self.entry_burst_time.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="w")
        self.entry_arr_time.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="w")
        button_task_input.grid(row=1, column=5, padx=10, pady=(0, 10), sticky="w")

        # Task table

        style = ttk.Style()
        style.configure("Treeview",
                        background="blue",
                        foreground="white",
                        grid=True,
                        rowheight=25,  # Adjust row height if necessary
                        borderwidth=1,  # Add border around the table
                        relief="solid", # Make borders solid
                        font=("Arial", 10))
        style.configure("Treeview.Heading",
                        font=("Arial", 10, "bold"),  # Font style and size
                        foreground="green",  # Text color of the column header
                        background="white")  # Background color of the column header

        self.task_tree = ttk.Treeview(self, columns=('Name', 'Burst Time', 'Arrival Time', 'Priority'), show='headings',style="Treeview")

        self.task_tree.heading('Name', text='Task Name')
        self.task_tree.heading('Burst Time', text='Burst Time')
        self.task_tree.heading('Arrival Time', text='Arrival Time')
        self.task_tree.heading('Priority', text='Priority')

        self.task_tree.column('Name', width=150)
        self.task_tree.column('Burst Time', width=150)
        self.task_tree.column('Arrival Time', width=150)
        self.task_tree.column('Priority', width=150)
        self.task_tree.grid(row=2, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="nsew")

        # Bottom
        frame_bottom = tk.Frame(self)
        self.quantum_entry = tk.Entry(frame_bottom, width=self.ENTRY_WIDTH)
        self.quantum_label = tk.Label(frame_bottom, text="Quantum time:")
        self.live_checkbox = tk.Checkbutton(frame_bottom)
        live_label = tk.Label(frame_bottom, text="Enable live scheduling:")
        start_button = tk.Button(self, text="Start", command=self.start_simulation)

        frame_bottom.grid(row=3, column=0, padx=10, pady=20, sticky="w")
        live_label.grid(row=0, column=2, padx=(20, 0), pady=20, sticky="e")
        self.live_checkbox.grid(row=0, column=3, padx=5, pady=20, sticky="w")
        start_button.grid(row=3, column=2, padx=20, pady=20, sticky="e")

        # List of scheduler-dependant options
        self.optional_widgets = [self.quantum_entry, self.quantum_label, self.entry_priority, self.priority_label]
        

    def add_task(self):
        try:
            
            # Live update option.
            if self.started_sim:
                new_task = Task(self.entry_task_name.get(), self.scheduler_app.current_time, int(self.entry_burst_time.get()))
                self.simulator.load(new_task)
            else:
                new_task = Task(self.entry_task_name.get(), int(self.entry_arr_time.get()), int(self.entry_burst_time.get()))
                self.chosen_option_indx = self.scheduler_types_strings.index(self.chosen_scheduler.get())

            # If priority is needed
            if (self.chosen_option_indx == 4 or self.chosen_option_indx == 5):
                new_task.priority = int(self.entry_priority.get())
            
            # TODO: we need to add an option for Round Robin.
            for task in self.tasks_list:
                if task.name == new_task.name:
                    messagebox.showwarning(title="Duplicate Tasks", message="Please enter unique task names.")
                    return
            self.tasks_list.append(new_task)
            self.task_tree.insert('', 'end', values=(new_task.name, new_task.burst_time, new_task.arr_time, new_task.priority))
        except TypeError:
            messagebox.showerror(title="Input Error", message="Incorrect parameters in task input.")
    

    def start_simulation(self):
        self.started_sim = True
        if self.chosen_scheduler.get() == SchedulerNames.FCFS:
            scheduler = FCFS_Scheduler()
        elif self.chosen_scheduler.get() == SchedulerNames.PRIORITY_NON_PREM:
            scheduler = Priority_non_prem_Scheduler()
        elif self.chosen_scheduler.get() == SchedulerNames.PRIORITY_PREM:
            scheduler = Priority_prem_Scheduler()
        elif self.chosen_scheduler.get() == SchedulerNames.SJF_NON_PREM:
            scheduler = SJF_non_prem_Scheduler()
        elif self.chosen_scheduler.get() == SchedulerNames.SRTF_PREM:
            scheduler = SJF_prem_Scheduler()

        self.simulator = Simulator(scheduler)
        self.simulator.load_bulk(self.tasks_list)

        self.scheduler_app = SchedulerApp(self.simulator)
        # self.destroy()
        #self.scheduler_app.root.mainloop()
        

    
    def update_options(self, *args):
        
        for widget in self.optional_widgets:
            widget.grid_remove()

        if self.chosen_scheduler.get() == SchedulerNames.PRIORITY_PREM or self.chosen_scheduler.get() == SchedulerNames.PRIORITY_NON_PREM:
            self.priority_label.grid(row=0, column=3, padx=10, pady=0, sticky="w")
            self.entry_priority.grid(row=1, column=3, padx=10, pady=(0, 10), sticky="w")

        elif self.chosen_scheduler.get() == SchedulerNames.ROUND_ROBIN:
            self.quantum_label.grid(row=0, column=0, padx=10, pady=20, sticky="w")
            self.quantum_entry.grid(row=0, column=1, padx=10, pady=20, sticky="w")
            
        

if __name__ == "__main__":
    app = TaskManagerApp()
    print(app.winfo_screenheight())
    print(app.winfo_screenwidth())
    app.mainloop()