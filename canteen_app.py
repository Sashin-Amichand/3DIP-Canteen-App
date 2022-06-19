# Sashin Amichand 11/05/22
# 3DIP Internal Assessment - An online canteen ordering application
# | Import tkinter | Import ttk (tkinter styling) 
# | Imports the dictionary containing the cafeteria menu
# | Imports sys for exit | Messagebox for windows pop up 
import tkinter as tk
from tkinter import ttk
import sys, tkinter.messagebox, json

class MainApp(tk.Tk):
    '''The class where my tkinter app is initilized, and any methods needed for the majority of my other classes is stored here ready for inhertiance.'''
    def __init__(self):
        '''Intializes tkinter and the basic window attributes.'''
        super().__init__()
        self.title('Canteen Orderng Applicaton')
        # For when the user clicks the exit button
        self.protocol("WM_DELETE_WINDOW", self.close_window) 

        self.styling()
        self.configure(background=self.bg_color)

        self.window = ttk.LabelFrame(self, text='Welcome!', width=620, height=200, style='TLabelframe')
        self.window.grid(row=0, column=0, padx=10, pady=10)

        self.center_window(self.window)
        self.x = 'hi'
        intro = "Welcome to my Canteen Ordering App! This app will allow you to\n place your order at the canteen, and you shall recieve a notification\n on when it is ready for you to pick up! \nIf you wish to order click Student, if you work at the canteen then click Admin."

        intro_lbl = ttk.Label(self.window, text=intro, font=(self.txt_style), 
                              justify='center', style='TLabel')
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
            new_window = tk.Toplevel(self)
            chosen_window(new_window)

    def center_window(self, window=None):
        if window is not None:
            self.window = window
            self.window.update_idletasks() #Add this line

            width = self.window.winfo_width()
            height = self.window.winfo_height()
            x = (self.window.winfo_screenwidth() // 2) - (width // 2)
            y = (self.window.winfo_screenheight() // 2) - (height // 2)

            self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        return

    def close_window(self): 
        '''Required for when the user wishes to close the program'''
        Exit = tkinter.messagebox.askyesno("Exit?", "Are you sure you wish to exit?")
        if Exit > 0:
            sys.exit()
            
    def go_back(self): 
        '''Required for when the user wishes to go back a window/screen.'''
        self.parent.withdraw()
        app.deiconify()

    def cafe_menu(self):
        '''This method opens up the cafe menu file, and reads it and saves the contents in a variable.'''
        with open("cafe_menu.json") as file:
            contents = json.load(file)
        self.menu_items = contents["menu_items"][0]

    def styling(self): 
        '''Creates the variables used for styling'''
        self.bg_color = '#61002f'
        self.frm_style = 'Cormorant', '20', 'bold'
        self.btn_style = 'Cormorant', '13', 'bold'
        self.txt_style = 'Cormorant', '13'
        self.txt_color = "#89c9ec"
        self.btn_color = "#28a8ed"

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.TLF = ttk.Style()
        self.TLF.theme_use('alt')
        self.TLF.configure('TLabelframe', background=self.bg_color, 
                            borderwidth=10, relief='raised')
        self.TLF.configure('TLabelframe.Label', 
                    background=self.bg_color, foreground=self.txt_color, 
                    font=(self.frm_style))

        self.TLabel = ttk.Style()
        self.TLabel.configure('TLabel', background=self.bg_color, 
                              foreground=self.txt_color)

        self.TEntry = ttk.Style()
        self.TEntry.configure("EntryStyle.TEntry", )

        self.TButton = ttk.Style()
        self.TButton.configure('TButton', background=self.btn_color,
                                foreground='black', font=(self.btn_style))
        self.TButton.configure('Del.TButton', background=self.btn_color, 
                                foreground='black')
        self.TButton.configure('Add.TButton', background=self.btn_color,
                              foreground='black')

        self.TButton.map('TButton', background=[('active', self.bg_color)], 
                        foreground=[('active', self.btn_color)])
        self.TButton.map('Del.TButton', background=[('active','red')], foreground=[('active', 'white')])
        self.TButton.map('Add.TButton', background=[('active','green')], 
                        foreground=[('active', 'white')])
        

class Student(tk.Frame, MainApp):
    '''The class that models the student window/ordering processes.'''
    def __init__(self, parent):
        '''Intiliazes the styling and variables used for the order widgets.'''
        super().__init__(parent)
    
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.styling()
        self.cafe_menu()

        self.parent.configure(background=self.bg_color)

        # Variables storing cost/menu item/food in a category and currently ordered food
        self.prices = []
        self.food_ordered = []
        self.current_items = []

        # Variables used to hold the quantity of items the user is ordering, plus the cost of items in a category.
        self.current_quantity = []
        self.total_quantity = {}
        self.current_category_cost = []
        self.total_category_cost = {}

        # Variable for the storing individual category costs and then the total cost itself.
        self.final_cost = {}
        self.total = 0

        # Frames set
        self.about_frm = ttk.LabelFrame(self.parent, text='Order:', width=700,
                                    height=700, style='TLabelframe')
        self.menu_frm = ttk.LabelFrame(self.parent, text='Menu:',
                                        style='TLabelframe')
        self.order_frm = ttk.LabelFrame(self.parent, text='Order Items:', 
                                        width=700, height=700, 
                                        style='TLabelframe')

        self.about_frm.grid(row=0, columnspan=8, padx=10)
        self.menu_frm.grid(row=1, columnspan=8, padx=20)

        self.order()

    def order(self):
        '''Method displaying what this window is about, and the category of food.'''

        order = "Please choose the items you would like to order, \nfrom the categories below:"
        order_lbl = ttk.Label(self.about_frm, text=order, justify='center',
                             font=(self.txt_style), style='TLabel')
        order_lbl.grid(row=1, columnspan=8, padx=5, pady=5)

        separator = ttk.Separator(self.about_frm, orient='horizontal')
        separator.grid(row=2, columnspan=8, ipadx=170, padx=5, pady=5)

        # Goes through the dictionary in cafe_menu.py which hosts the cafeteria items. This allows me to dynamically allocate the amount of buttons needed for the amount of categories there are in that file.
        columns = 1
        for name in self.menu_items.keys():
            beverages_btn = ttk.Button(self.about_frm, text=name.title(), 
                                command=lambda category=name: self.display_category(category))
            beverages_btn.grid(row=3, column=columns, padx=5, pady=5, sticky="NW")    
            columns += 1

        back_btn = ttk.Button(self.about_frm, text="Go Back", 
                             command=lambda: self.go_back())

        back_btn.grid(row=3, column=columns+1, padx=5, pady=5, sticky="NW")

    def display_category(self, type_category):
        '''Method that displays the cafeteria menu item widgets based on the category selected.'''
        self.current_category = type_category

        for widgets in self.menu_frm.winfo_children(): 
                widgets.destroy()

        # This if statement clears the old lists so that the new category stuff may be added
        if self.current_quantity or self.prices or self.current_category_cost or self.current_items:
            del self.current_quantity[:]
            del self.current_category_cost[:]
            del self.prices[:]
            del self.current_items[:]

        # Checks if the total quantity and final cost dictonaries are empty
        # If so, it will then add values to them.
        if len(self.total_quantity) == 0 and len(self.final_cost) == 0:
            for name in self.menu_items.keys():
                self.total_quantity[name]  = ''
                self.final_cost[name]  = 0
                self.total_category_cost[name]  = 0

        rows = 1
        item_number = 0
        del_item = 0

        # Goes through the dictionary in cafe_menu.py which hosts the cafeteria items. This allows me to dynamically allocate values to the necessary 
        # lists, as well as the number of labels and buttons based on whats in that file.
        for item, price in self.menu_items[self.current_category].items():
            self.items_txt = f"{item}: ${price}0"
            self.current_items.append(item)
            self.prices.append(price)
            self.current_quantity.append(0)
            self.current_category_cost.append(0)

            item_lbl = ttk.Label(self.menu_frm, text=self.items_txt,
                                font=(self.txt_style), justify='left',
                                style='TLabel')

            quantity_btn = ttk.Button(self.menu_frm, text="Add 1x", 
                        command=lambda item_number=item_number:  
                        self.create_cost(item_number), style='Add.TButton')

            remove_btn = ttk.Button(self.menu_frm, text="Remove 1x", 
                        command=lambda del_item=del_item: 
                        self.create_cost(del_item, True), style='Del.TButton')

            item_lbl.grid(row=rows, column=1, padx=5, pady=5)
            quantity_btn.grid(row=rows, column=2, padx=5, pady=5, sticky="NW")
            remove_btn.grid(row=rows, column=3, padx=5, pady=5, sticky="NW")

            rows += 1
            item_number += 1
            del_item += 1

    def create_cost(self, chosen_item, remove_item=False):
        '''Method that gets the amount of an item the user wants then adds it together to get the current cost of the category the user is on.'''
        item = f"1x {self.current_items[chosen_item]}"

        if remove_item: # Checks if user wishes to remove an item
            try:
                self.food_ordered.remove(item)
            except:
                return
            self.current_quantity = self.total_quantity[self.current_category]
            self.current_category_cost = self.total_category_cost[self.current_category] 
            self.current_quantity[chosen_item] -= 1
            new_cost_item = self.prices[chosen_item] * self.current_quantity[chosen_item]
            self.current_category_cost[chosen_item] = new_cost_item

            for widgets in self.order_frm.winfo_children():
                widgets.destroy()

            self.create_total_cost()      

        else:
            if len(self.total_quantity[self.current_category]) != 0:
                self.current_quantity[:] = self.total_quantity[self.current_category]
                self.current_category_cost[:] = self.total_category_cost[self.current_category]

            self.current_quantity[chosen_item] += 1
            self.food_ordered.append(item)
            cost_item = self.prices[chosen_item] * self.current_quantity[chosen_item]
            self.current_category_cost[chosen_item] = cost_item

            self.create_total_cost()

    def create_total_cost(self):
        '''Small method that adds up all the different total values(Quantity, Category Costs) to make up the total cost.'''
        self.total_quantity[self.current_category] = self.current_quantity[:]
        self.total_category_cost[self.current_category] = self.current_category_cost[:]

        self.final_cost[self.current_category] = sum(self.total_category_cost[self.current_category])
        
        self.total = sum(self.final_cost.values())

        self.display_cost()

    def display_cost(self):
        '''First grabs the total cost of the users order, then displays the total cost and items ordered.'''
        cost = f"The total cost is ${self.total}0!"
        cost_lbl = ttk.Label(self.order_frm, text=cost,
                            justify='center', font=('Cormorant', '14', 'bold'), 
                            style='TLabel')
        ordered = f'You have ordered: {", ".join(self.food_ordered)}'
        ordered_lbl = ttk.Label(self.order_frm, text=ordered,
                            justify='center', font=('Cormorant', '12', 'bold'), 
                            style='TLabel')

        self.order_frm.grid(row=2, columnspan=8, padx=10)
        ordered_lbl.grid(row=1, column=1, padx=5, pady=5)
        cost_lbl.grid(row=2, column=1, padx=5, pady=5)

class Admin(tk.Frame, MainApp):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.styling()
        self.parent.configure(background=self.bg_color)

        self.login_frm = ttk.LabelFrame(self.parent, text='Login:', width=500,
                                    height=500, style='TLabelframe')
        self.login_frm.grid(row=0, columnspan=3, padx=10, pady=10)

        login = "If you are a canteen staff worker, please enter your\n credentials below."
        login_lbl = ttk.Label(self.login_frm, text=login, justify='center',
                             font=(self.txt_style), style='TLabel')
        login_lbl.grid(row=1, columnspan=3, padx=5, pady=5)
        separator = ttk.Separator(self.login_frm, orient='horizontal')
        separator.grid(row=2, columnspan=3, ipadx=170, padx=5, pady=5)

        self.login()

    def login(self):
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.check = tk.IntVar()

        username_lbl = ttk.Label(self.login_frm, text='Username:',
                                font=(self.txt_style), style='TLabel')
        password_lbl = ttk.Label(self.login_frm, text='Password:',
                                font=(self.txt_style), style='TLabel')
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
                               command=lambda: self.go_back(), width=10)
        login_btn = ttk.Button(self.login_frm, text="Sign In", 
                               command=lambda: self.sign_in(), width=10)
        back_btn.grid(row=5, column=1, padx=2, pady=5, sticky="NE")
        login_btn.grid(row=5, column=2, pady=5, sticky="Ne")

    def show_pass(self, password_entry):
        if self.check.get() == 1 :
            password_entry.configure(show = "")
        elif self.check.get() == 0 :
            password_entry.configure(show = "*")
      

if __name__ == "__main__": 
    app = MainApp()
    app.mainloop()