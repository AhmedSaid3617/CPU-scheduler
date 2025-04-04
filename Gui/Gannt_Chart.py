import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from queue import Queue

class GanttChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FCFS Gantt Chart")

        # FCFS queue of processes
        self.process_queue = Queue()
        self.process_list = [
            {"name": "P1", "duration": 5, "executed": 0, "color": 'skyblue'},
            {"name": "P2", "duration": 3, "executed": 0, "color": 'lightgreen'},
            {"name": "P3", "duration": 4, "executed": 0, "color": 'lightcoral'}
        ]
        for p in self.process_list:
            self.process_queue.put(p)

        self.timeline = 0
        self.executed_processes = []

        # Button to simulate 1 tick
        self.step_button = tk.Button(root, text="Step", command=self.step)
        self.step_button.pack()

        self.canvas = None
        self.current_process = self.process_queue.get() if not self.process_queue.empty() else None
        self.auto_run()

    def step(self):
        if self.current_process:
            self.current_process["executed"] += 1
            self.timeline += 1

            # Log executed process for visualization
            self.executed_processes.append({
                "name": self.current_process["name"],
                "start": self.timeline - 1,
                "duration": 1,
                "color": self.current_process["color"]
            })

            if self.current_process["executed"] >= self.current_process["duration"]:
                self.current_process = self.process_queue.get() if not self.process_queue.empty() else None

            self.create_gantt_chart()

    def create_gantt_chart(self):
        fig, ax = plt.subplots(figsize=(16, 8))

        for i, process in enumerate(self.executed_processes):
            ax.barh(0, process["duration"], left=process["start"], height=0.5, color=process["color"])
            ax.text(process["start"] + 0.5, 0, process["name"], ha='center', va='center', color='black')

        ax.set_xlim(0, max(self.timeline, 10))
        ax.set_yticks([])
        ax.set_xlabel('Time')
        ax.set_title('FCFS Gantt Chart')

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def auto_run(self):
        self.step()  # Perform one step
        self.root.after(1000, self.auto_run)

if __name__ == "__main__":
    root = tk.Tk()
    app = GanttChartApp(root)
    root.mainloop()
