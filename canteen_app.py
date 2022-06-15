# Sashin Amichand 11/05/22
# 3DIP Internal Assessment - An online canteen ordering application
# | Import tkinter | Import ttk (tkinter styling) 
# | Imports sys for exit | Messagebox for windows pop up
from textwrap import fill
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

        self.styling()
        self.configure(background=self.bg_color)

        window = ttk.LabelFrame(self, text='Welcome!', width=1000, 
                                height=1000, style='LF.TLabelframe')
        window.grid(row=0, column=0, padx=10, pady=10)

        intro = "Welcome to my Canteen Ordering App! This app will allow you to\n place your order at the canteen, and you shall recieve a notification\n on when it is ready for you to pick up! If you wish to order click\n Student, if you work at the canteen then click Admin."

        intro_lbl = ttk.Label(window, text=intro, font=(self.txt_style), 
                              justify='center', style='L.TLabel')
        intro_lbl.grid(row=1, columnspan=2, padx=5, pady=5)

        admin_btn = ttk.Button(window, text="Admin", 
                              command=lambda: self.open_window(Admin))
        admin_btn.grid(row=2, column=0, padx=5, pady=5, sticky="NE")

        student_btn = ttk.Button(window, text="Student", 
                                command=lambda: self.open_window(Student))
        student_btn.grid(row=2, column=1, padx=5, pady=5, sticky="NW")

    # Creates all the variables for styling (In a method in case I need to access variables from another class)
    def styling(self): 
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

        self.TLabel = ttk.Style()
        self.TLabel.configure('L.TLabel', background=self.bg_color, 
                              foreground=self.txt_color)
        
        self.TEntry = ttk.Style()
        self.TEntry.configure("EntryStyle.TEntry",)
        return

    def close_window(self): # For when the user presses the x(exit) button
        Exit = tkinter.messagebox.askyesno("Exit?", "Are you sure you wish to exit?")
        if Exit > 0:
            sys.exit()
            
    # For when the user clicks something but wishes to return back
    def go_back(self): 
        self.parent.destroy()
        app.deiconify()

    def open_window(self, chosen_window):
        self.withdraw()
        window = tk.Toplevel(self)
        chosen_window(window)

class Student(tk.Frame, MainApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.geometry("450x600")
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        
        self.styling()
        self.parent.configure(background=self.bg_color)

        self.order_frm = ttk.LabelFrame(self.parent, text='Order:', width=500,
                                    height=500, style='LF.TLabelframe')
        self.menu_frm = ttk.LabelFrame(self.parent, text='Menu:', width=500,
                                    height=500, style='LF.TLabelframe')
        self.button_frm = ttk.LabelFrame(self.parent, text='Buttons:', 
                                        width=500, height=500, 
                                        style='LF.TLabelframe')
        self.order_frm.grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_frm.grid(row=2, columnspan=3, padx=10, pady=10)
        self.button_frm.grid(row=20, columnspan=3, padx=10, pady=10)
        order = "Please choose the items you would like to order. From the list\n below"
        order_lbl = ttk.Label(self.order_frm, text=order, justify='center',
                             font=(self.txt_style), style='L.TLabel')
        order_lbl.grid(row=1, columnspan=3, padx=5, pady=5)
        separator = ttk.Separator(self.order_frm, orient='horizontal')
        separator.grid(row=2, columnspan=3, ipadx=170, padx=5, pady=5)


        self.menu()

    def menu(self):
        from cafe_menu import menu_items

        rows = 3
        for cat, price in menu_items['BEVERAGES'].items():
            rows += 1
            items_txt = f"{cat} ${price}0"
            item_lbl = ttk.Label(self.menu_frm, text=items_txt,
                                font=(self.txt_style), justify='left',
                                 style='L.TLabel')
            item_lbl.grid(row=rows, column=1, padx=5, pady=5)

        back_btn = ttk.Button(self.button_frm, text="Go Back", 
                             command=lambda: self.go_back())
        back_btn.grid(row=20, column=1, pady=5, sticky="NW")

        
class Admin(tk.Frame, MainApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.geometry("440x210")
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.styling()
        self.parent.configure(background=self.bg_color)

        self.login_frm = ttk.LabelFrame(self.parent, text='Login:', width=500,
                                    height=500, style='LF.TLabelframe')
        self.login_frm.grid(row=0, columnspan=3, padx=10, pady=10)

        login = "If you are a canteen staff worker, please enter your\n credentials below."
        login_lbl = ttk.Label(self.login_frm, text=login, justify='center',
                             font=(self.txt_style), style='L.TLabel')
        login_lbl.grid(row=1, columnspan=3, padx=5, pady=5)
        separator = ttk.Separator(self.login_frm, orient='horizontal')
        separator.grid(row=2, columnspan=3, ipadx=170, padx=5, pady=5)

        self.login()

    def login(self):
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.check = tk.IntVar()

        username_lbl = ttk.Label(self.login_frm, text='Username:',
                                font=(self.txt_style), style='L.TLabel')
        password_lbl = ttk.Label(self.login_frm, text='Password:',
                                font=(self.txt_style), style='L.TLabel')
        username_lbl.grid(row=3, column=0, padx=5, pady=5)
        password_lbl.grid(row=4, column=0, padx=5, pady=5)

        username_entry = ttk.Entry(self.login_frm, textvariable=self.username, 
                                   width=30, style="EntryStyle.TEntry")
        password_entry = ttk.Entry(self.login_frm, textvariable=self.password, 
                                   show='*', width=30,style="EntryStyle.TEntry")
        username_entry.grid(row=3, column=1, padx=5, pady=5, sticky='NW')
        password_entry.grid(row=4, column=1, padx=5, pady=5, sticky='NW')

        # Creates a check button so the user can toggle to see their password
        show_password = tk.Checkbutton(self.login_frm, text="Show Password",
                                        variable = self.check, onvalue = 1,
                                        offvalue = 0, width = 14,
                                        background=self.bg_color,
                                        foreground=self.txt_color,
                                        command = lambda: 
                                        self.show_pass(password_entry))
        show_password.grid(row=4, column=2, padx=5)

        back_btn = ttk.Button(self.login_frm, text="Go Back", 
                               command=lambda: self.go_back())
        login_btn = ttk.Button(self.login_frm, text="Sign In", 
                               command=lambda: self.sign_in())
        back_btn.grid(row=5, column=1, pady=5, sticky="NW")
        login_btn.grid(row=5, column=1, pady=5, sticky="NE")

    def show_pass(self, password_entry):
        if self.check.get() == 1 :
            password_entry.configure(show = "")
        elif self.check.get() == 0 :
            password_entry.configure(show = "*")
                

if __name__ == "__main__": 
    app = MainApp()
    app.mainloop()