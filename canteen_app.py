# Sashin Amichand 11/05/22
# 3DIP Internal Assessment - An online canteen ordering application
# | Import tkinter | Import ttk (tkinter styling) 
# | Imports sys for exit | Messagebox for windows pop up
import tkinter as tk
from tkinter import ttk
import sys, tkinter.messagebox

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Canteen Orderng Applicaton')
        self.geometry("500x170")

        # For when the user clicks the exit button
        self.protocol("WM_DELETE_WINDOW", self.close_window) 

        # Variables for styling
        self.bg_color = '#61002f'
        self.frm_style = 'Cormorant', '18', 'bold'
        self.txt_style = 'Cormorant', '12'
        self.txt_color = "#89c9ec"

        # Styling my app (colors etc) 
        self.MLFrame = ttk.Style()
        self.MLFrame.configure('LF.TLabelframe', background=self.bg_color)
        self.MLFrame.configure('LF.TLabelframe.Label', 
                    background=self.bg_color, foreground=self.txt_color, 
                    font=(self.frm_style))

        self.TLabel = ttk.Style()
        self.TLabel.configure('L.TLabel', background=self.bg_color, 
                              foreground=self.txt_color)

        self.configure(background=self.bg_color)
        

        window = ttk.LabelFrame(self, text='Welcome!', width=1000, 
                                height=1000, style='LF.TLabelframe')
        window.grid(row=0, column=0, padx=10, pady=10)

        intro = "Welcome to my Canteen Ordering App! This app will allow you to\n place your order at the canteen, and you shall recieve a notification\n on when it is ready for you to pick up! If you wish to order click\n Student, if you work at the canteen then click Admin."

        intro_lbl = ttk.Label(window, text=intro, font=(self.txt_style), 
                              justify='center', style='L.TLabel')
        intro_lbl.grid(row=1, columnspan=2, padx=5, pady=5)

        admin_btn = ttk.Button(window, text="Admin", command=self.staff)
        admin_btn.grid(row=2, column=0, padx=5, pady=5, sticky="NE")

        student_btn = ttk.Button(window, text="Student", command=self.student)
        student_btn.grid(row=2, column=1, padx=5, pady=5, sticky="NW")

    def close_window(self): # For when the user presses the x(exit) button
        Exit = tkinter.messagebox.askyesno("Exit?", "Are you sure you wish to exit?")
        if Exit > 0:
            sys.exit()

    def staff(self): # For when a canteen staff wants to do Admin stuff
        self.withdraw()
        window = tk.Toplevel(self)
        Admin(window)
    
    def student(self): # For when a student wishes to place an order
        print("Bye")
        
class Admin(tk.Frame, MainApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.login_frm = ttk.LabelFrame(self.parent, text='Login:', width=500,
                                    height=500, style='MF.TFrame')
        self.login_frm.grid(row=0, column=0)

        self.login()

    def login(self):
        test = ttk.Label(self.login_frm, text='hi!', style='L.TLabel')
        test.grid(row=1, column=1)

if __name__ == "__main__": 
    app = MainApp()
    app.mainloop()