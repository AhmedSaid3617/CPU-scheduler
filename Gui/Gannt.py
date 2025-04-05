import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker

class Gannt():
    def __init__(self, parent):
        self.parent = parent
        self.canvas = None
        self.fig = None
        self.ax = None

    def create_gantt_chart(self, start, task_list):
        colour = ["blue", "red", "green", "purple", "brown", "magenta"]

        # First time setup: create figure and canvas once
        if self.canvas is None:
            self.fig, self.ax = plt.subplots(figsize=(20, 2))
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent)
            self.canvas.get_tk_widget().pack(fill="both", expand=True,padx=10, pady=5)
        else:
            self.ax.clear()  # Clear previous plot instead of destroying canvas

        # Draw bars
        count=0
        for i, task_name in enumerate(task_list):
            count=count+1 if i !=0 and task_list[i-1] != task_list[i] else count
            self.ax.barh(0, width=1, left=i, height=1, color=colour[count % 6])
            self.ax.text(i + 0.5, 0, task_name, ha='center', va='center', color="white", fontsize=12)

        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        self.ax.set_xlim(0, max(start + len(task_list), 20))
        self.ax.set_yticks([])
        self.ax.set_xlabel('Time', fontsize=12)
        self.ax.set_title('Gantt Chart', fontsize=14)
        self.ax.tick_params(axis='x', labelsize=10)

        # Redraw only the canvas
        self.canvas.draw()
