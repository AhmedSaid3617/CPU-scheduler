import tkinter as tk
from tkinter import ttk

class StatisticsWindow(tk.Toplevel):
    def __init__(self,parent,avg_turnaround, avg_waiting, avg_response):
        super().__init__(parent)
        self.avg_turnaround = avg_turnaround
        self.avg_waiting = avg_waiting
        self.avg_response = avg_response
        self.title("FCFS Gantt Chart Simulation")
        self.geometry("600x400")
        self.configure(bg="#ecf0f3")

        self.setup_styles()
        self.setup_ui()

        # self.root.mainloop()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Segoe UI", 12), background="#ffffff", foreground="#333333")
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"), background="#ffffff", foreground="#2c3e50")
        style.configure("Value.TLabel", font=("Segoe UI", 12, "bold"), foreground="#1abc9c", background="#ffffff")
        style.configure("Card.TFrame", background="#ffffff", relief="raised", borderwidth=1)

    def setup_ui(self):
        # Configure root grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Container frame
        container = ttk.Frame(self, style="Card.TFrame", padding=20)
        container.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)

        container.columnconfigure((0, 1), weight=1)
        container.rowconfigure((1, 2, 3), weight=1)

        # Title
        title_label = ttk.Label(container, text="Statistics", style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="n")

        # Labels and values
        labels = ["Average Turnaround Time:", "Average Waiting Time:", "Average Response Time:"]
        values = [self.avg_turnaround, self.avg_waiting, self.avg_response]

        for i in range(3):
            label = ttk.Label(container, text=labels[i], style="TLabel", anchor="w")
            label.grid(row=i+1, column=0, sticky="nsew", padx=(10, 5), pady=5)

            value = ttk.Label(container, text=f"{values[i]:.2f} sec", style="Value.TLabel", anchor="e")
            value.grid(row=i+1, column=1, sticky="nsew", padx=(5, 10), pady=5)


# Example usage
if __name__ == "__main__":
    StatisticsWindow(avg_turnaround=12.5, avg_waiting=4.2, avg_response=5.6)
