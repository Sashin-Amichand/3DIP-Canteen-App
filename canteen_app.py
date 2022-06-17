# Sashin Amichand 11/05/22
# 3DIP Internal Assessment - An online canteen ordering application
# | Import tkinter | Import ttk (tkinter styling) 
# | Imports sys for exit | Messagebox for windows pop up
import tkinter as tk
from tkinter import ttk
import sys, tkinter.messagebox

class MainApp(tk.Tk):
    '''The class where my tkinter app is initilized, and any methods needed for the majority of my other classes is stored here ready for inhertiance.'''

    def __init__(self):
        '''Intializes tkinter and the basic window attributes.'''
        super().__init__()
        self.title('Canteen Orderng Applicaton')
        self.geometry("500x170")
        # For when the user clicks the exit button
        self.protocol("WM_DELETE_WINDOW", self.close_window) 

        self.styling()
        self.configure(background=self.bg_color)
        self.intro()

    def intro(self):
        '''Creates/Displays the introduction widgets.'''
        self.window = ttk.LabelFrame(self, text='Welcome!', width=1000, 
                                height=1000, style='LF.TLabelframe')
        self.window.grid(row=0, column=0, padx=10, pady=10)

        intro = "Welcome to my Canteen Ordering App! This app will allow you to\n place your order at the canteen, and you shall recieve a notification\n on when it is ready for you to pick up! If you wish to order click\n Student, if you work at the canteen then click Admin."

        intro_lbl = ttk.Label(self.window, text=intro, font=(self.txt_style), 
                              justify='center', style='L.TLabel')
        intro_lbl.grid(row=1, columnspan=2, padx=5, pady=5)

        admin_btn = ttk.Button(self.window, text="Admin", 
                                command=lambda: self.open_window(Admin))
        student_btn = ttk.Button(self.window, text="Student", 
                                command=lambda: self.open_window(Student))

        admin_btn.grid(row=2, column=0, padx=5, pady=5, sticky="NE")
        student_btn.grid(row=2, column=1, padx=5, pady=5, sticky="NW")
        
    def open_window(self, chosen_window=None):
        '''Simple method to display the window of the users choice.'''
        if chosen_window is not None:
            self.withdraw()
            show_window = tk.Toplevel(self)
            chosen_window(show_window)

    def styling(self): 
        '''Creates the variables used for styling'''
        self.bg_color = '#61002f'
        self.frm_style = 'Cormorant', '18', 'bold'
        self.txt_style = 'Cormorant', '12'
        self.txt_color = "#89c9ec"

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

    def close_window(self): 
        '''Required for when the user wishes to close the program'''
        Exit = tkinter.messagebox.askyesno("Exit?", "Are you sure you wish to exit?")
        if Exit > 0:
            sys.exit()
            
    def go_back(self): 
        '''Required for when the user wishes to go back a window/screen.'''
        self.parent.withdraw()
        app.deiconify()


class Student(tk.Frame, MainApp):
    '''The class that models the student window/ordering processes.'''

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.styling()
        self.parent.configure(background=self.bg_color)

        self.order_frm = ttk.LabelFrame(self.parent, text='Order:', width=700,
                                    height=700, style='LF.TLabelframe')
        self.menu_frm = ttk.LabelFrame(self.parent, text='Menu:',
                                        style='LF.TLabelframe')
        self.button_frm = ttk.LabelFrame(self.parent, text='Type of Food:', 
                                        width=700, height=700, 
                                        style='LF.TLabelframe')
        self.order_frm.grid(row=0, columnspan=3, padx=10, pady=10)
        self.button_frm.grid(row=1, columnspan=3, padx=10, pady=10)
        self.menu_frm.grid(row=2, columnspan=3, padx=10, pady=10)

        order = "Please choose the items you would like to order. From the list\n below"
        order_lbl = ttk.Label(self.order_frm, text=order, justify='center',
                             font=(self.txt_style), style='L.TLabel')
        order_lbl.grid(row=1, columnspan=3, padx=5, pady=5)
        separator = ttk.Separator(self.order_frm, orient='horizontal')
        separator.grid(row=2, columnspan=3, ipadx=170, padx=5, pady=5)

        self.menu()

    def menu(self):
        '''Method displaying the widgets on this window.'''

        # Imports a dictionary storing cafeteria menu items.
        from cafe_menu import menu_items 

        self.menu_items = menu_items

        special_meals_btn = ttk.Button(self.button_frm, 
                                       text="Special Meals of the week", 
                                      command=lambda: self.display_category
                                      ('special meals of the week'))

        beverages_btn = ttk.Button(self.button_frm, text="Beverages", 
                             command=lambda: self.display_category('beverages'))
                             
        hot_lunch_btn = ttk.Button(self.button_frm, text="Hot Lunchs", 
                        command=lambda: self.display_category('hot lunchs'))

        healthy_choices_btn = ttk.Button(self.button_frm,
                                        text="Healthy Choices", 
                                        command=lambda: 
                                        self.display_category('healthy choices')
                                        )

        snacks_btn = ttk.Button(self.button_frm, text="Snacks", 
                             command=lambda: self.display_category('snacks'))

        back_btn = ttk.Button(self.button_frm, text="Go Back", 
                             command=lambda: self.go_back())

        cost_btn = ttk.Button(self.button_frm, text="Cost", 
                             command=lambda: self.add_cost())

        special_meals_btn.grid(row=3, column=1, padx=5, pady=5, sticky="NW")
        beverages_btn.grid(row=3, column=2, padx=5, pady=5, sticky="NW")    
        hot_lunch_btn.grid(row=3, column=3, padx=5, pady=5, sticky="NW")    
        healthy_choices_btn.grid(row=3, column=4, padx=5, pady=5,
                                sticky="NW")    
        snacks_btn.grid(row=3, column=5, padx=5, pady=5, sticky="NW")    
        back_btn.grid(row=3, column=6, padx=5, pady=5, sticky="NW")
        cost_btn.grid(row=3, column=7, padx=5, pady=5, sticky="NW")

    def display_category(self, type_category):
        '''Method that displays the cafeteria menu item widgets based on the category selected.'''

        self.item_prices = []
        self.menu_category = self.menu_items[type_category]
        num_items = len(self.menu_category)
        rows = 3
        columns = 1
        self.test = []
        for widgets in self.menu_frm.winfo_children():
            widgets.grid_remove()

        for item, price in self.menu_category.items():
            rows += 1
            self.items_txt = f"{item}: ${price}0"
            self.item_lbl = ttk.Label(self.menu_frm, text=self.items_txt,
                                font=(self.txt_style), justify='left',
                                style='L.TLabel')
            self.item_lbl.grid(row=rows, column=columns, padx=5, pady=5)
            self.item_prices.append(price)
            self.test.append(item)

        rows = 3
        for i in range(num_items):
            rows += 1
            print(i)
            self.test_btn = ttk.Button(self.menu_frm, 
                                        text=self.test[i], 
                                    command=self.test.append(i))
            self.test_btn.grid(row=rows, column=2, padx=5, pady=5, 
                                sticky="NW")

    def add_cost(self):
        print(self.test)

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