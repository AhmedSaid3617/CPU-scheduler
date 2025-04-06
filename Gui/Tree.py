import tkinter as tk
from tkinter import ttk

class Tree:
    def __init__(self,parent):
        self.parent = parent
        self.tree=None

    def create_tree(self):
        # Define Treeview (table)
        columns = ("name", "arrival", "burst")
        self.tree = ttk.Treeview(self.parent, columns=columns, show="headings")
        self.tree.heading("name", text="Process Name")
        self.tree.heading("arrival", text="Arrival Time")
        self.tree.heading("burst", text="Burst Time")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def delete_all(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def add(self, task):
        self.tree.insert("", tk.END, values=[task.name, task.arr_time, task.burst_time])

    def update(self, process_name):
        print(process_name)
        for item in self.tree.get_children():
            row = self.tree.item(item)["values"]
            if row[0] == process_name:
                self.tree.item(item, values=(row[0], row[1], max(0, row[2] - 1)))