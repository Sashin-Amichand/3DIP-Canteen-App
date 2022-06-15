# Sashin Amichand 11/05/22
# 3DIP Internal Assessment - An online canteen ordering application
import tkinter as tk
from tkinter import ttk
import sys, tkinter.messagebox
#class StaffLogin:

#class OrderMenu:
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.title('Canteen Orderng Applicaton')

        window = ttk.LabelFrame(self, text="Choose who you are:")
        window.grid(row=0, column=0)


        test = ttk.Button(window, text="Staff", command=self.staff)
        test.grid(row=1, column=0)

        test_two = ttk.Button(window, text="Student", command=self.student)
        test_two.grid(row=2, column=0)

    def close_window(self):
        Exit = tkinter.messagebox.askyesno("Exit?", "Are you sure you wish to exit?")
        if Exit > 0:
            sys.exit()

    def staff(self):
        self.withdraw()
        window = tk.Toplevel(self)
        Staff(window)
    
    def student(self):
        print("Bye")
        
class Staff(tk.Frame, MainApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.login_frm = ttk.LabelFrame(self.parent, text='Login:', width=500,
                                    height=500)
        self.login_frm.grid(row=0, column=0)

        self.login()

    def login(self):
        test = ttk.Label(self.login_frm, text='hi!')
        test.grid(row=1, column=1)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()