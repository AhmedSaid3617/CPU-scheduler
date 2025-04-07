from Gui.Start_Page import TaskManagerApp

if __name__ == "__main__":
    app = TaskManagerApp()
    print(app.winfo_screenheight())
    print(app.winfo_screenwidth())
    app.mainloop()