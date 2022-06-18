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
        '''Intiliazes the styling and frames used for this window.'''
        super().__init__(parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.styling()
        self.parent.configure(background=self.bg_color)

        self.intro_frm = ttk.LabelFrame(self.parent, text='Order:', width=700,
                                    height=700, style='LF.TLabelframe')
        self.menu_frm = ttk.LabelFrame(self.parent, text='Menu:',
                                        style='LF.TLabelframe')
        self.order_frm = ttk.LabelFrame(self.parent, text='Order Items:', 
                                        width=700, height=700, 
                                        style='LF.TLabelframe')
        self.intro_frm.grid(row=0, columnspan=8, padx=10)
        self.menu_frm.grid(row=1, columnspan=8, padx=10)

        order = "Please choose the items you would like to order, \nfrom the categories below:"
        order_lbl = ttk.Label(self.intro_frm, text=order, justify='center',
                             font=(self.txt_style), style='L.TLabel')
        order_lbl.grid(row=1, columnspan=8, padx=5, pady=5)
        separator = ttk.Separator(self.intro_frm, orient='horizontal')
        separator.grid(row=2, columnspan=8, ipadx=170, padx=5, pady=5)

        self.menu()

    def menu(self):
        '''Method displaying the widgets on this window and creating variables'''

        # Imports a dictionary storing cafeteria menu items.
        from cafe_menu import menu_items 

        self.menu_items = menu_items
        self.prices = []
        self.quantity = []
        self.food_ordered = []
        self.current_items = []
        self.cost = []
        self.current_cost = []
        self.final_cost = []
        self.total = 0

        special_meals_btn = ttk.Button(self.intro_frm, 
                                       text="Special Meals of the week", 
                                      command=lambda: self.display_category
                                      ('special meals of the week'))

        beverages_btn = ttk.Button(self.intro_frm, text="Beverages", 
                             command=lambda: self.display_category('beverages'))
                             
        hot_lunch_btn = ttk.Button(self.intro_frm, text="Hot Lunchs", 
                        command=lambda: self.display_category('hot lunchs'))

        healthy_choices_btn = ttk.Button(self.intro_frm,
                                        text="Healthy Choices", 
                                        command=lambda: 
                                        self.display_category('healthy choices')
                                        )

        snacks_btn = ttk.Button(self.intro_frm, text="Snacks", 
                             command=lambda: self.display_category('snacks'))

        back_btn = ttk.Button(self.intro_frm, text="Go Back", 
                             command=lambda: self.go_back())

        special_meals_btn.grid(row=3, column=1, padx=5, pady=5, sticky="NW")
        beverages_btn.grid(row=3, column=2, padx=5, pady=5, sticky="NW")    
        hot_lunch_btn.grid(row=3, column=3, padx=5, pady=5, sticky="NW")    
        healthy_choices_btn.grid(row=3, column=4, padx=5, pady=5,
                                sticky="NW")    
        snacks_btn.grid(row=3, column=5, padx=5, pady=5, sticky="NW")    
        back_btn.grid(row=3, column=6, padx=5, pady=5, sticky="NW")

    def display_category(self, type_category):
        '''Method that displays the cafeteria menu item widgets based on the category selected.'''

        for widgets in self.menu_frm.winfo_children():
                widgets.destroy()

        # These if statements clears the lists and current item totals of the previous category of food.
        if self.quantity or self.cost or self.prices or self.current_cost or self.current_items:
            del self.quantity[:]
            del self.cost[:]
            del self.prices[:]
            del self.current_items[:]

            previous_final_cost = self.final_cost[-1]
            del self.final_cost[:]
            self.final_cost.append(previous_final_cost)
            self.calc_total()

        rows = 1
        item_number = 0
        del_item = 0
        self.menu_type = self.menu_items[type_category]
    
        for item, price in self.menu_type.items():
            self.items_txt = f"{item}: ${price}0"
            self.prices.append(price)
            self.quantity.append(0)
            self.cost.append(0)
            self.current_items.append(item)

            self.item_lbl = ttk.Label(self.menu_frm, text=self.items_txt,
                                font=(self.txt_style), justify='left',
                                style='L.TLabel')
            self.item_lbl.grid(row=rows, column=1, padx=5, pady=5)


            self.quantity_btn = ttk.Button(self.menu_frm, text="Add 1x", 
                        command=lambda item_number=item_number:  
                        self.create_cost(item_number))
            self.quantity_btn.grid(row=rows, column=2, padx=5, pady=5, 
                                sticky="NW")
            self.remove_btn = ttk.Button(self.menu_frm, text="Remove item", 
                        command=lambda del_item=del_item: 
                        self.create_cost(del_item, True))
            self.remove_btn.grid(row=rows, column=3, padx=5, pady=5, 
                                sticky="NW")
       
            rows += 1
            item_number += 1
            del_item += 1

    def display_cost(self, calculate=False):
        '''First grabs the total cost of the users order, then displays the total cost and items ordered.'''
        if calculate:
            self.calc_total()

        cost = f"The total cost is ${self.total}0!"
        self.order_frm.grid(row=2, columnspan=8, padx=10)
        cost_lbl = ttk.Label(self.order_frm, text=cost,
                            justify='center', font=(self.txt_style), 
                            style='L.TLabel')
        cost_lbl.grid(row=1, column=1, padx=5, pady=5)
        ordered = f'You have ordered: {", ".join(self.food_ordered)}'
        ordered_lbl = ttk.Label(self.order_frm, text=ordered,
                            justify='center', font=(self.txt_style), 
                            style='L.TLabel')
        ordered_lbl.grid(row=2, column=1, padx=5, pady=5)

    def create_cost(self, chosen_item, remove_item=False):
        '''Method that gets the amount of an item the user wants then adds it together to get the current cost of the category the user is on.'''
        item = f"1x {self.current_items[chosen_item]}"

        if remove_item: # Checks if user wants to remove an item
            try:
                self.food_ordered.remove(item)
            except:
                return
            self.quantity[chosen_item] -= 1
            new_cost_item = self.prices[chosen_item] * self.quantity[chosen_item]
            self.cost[chosen_item] = new_cost_item
            self.final_cost.append(sum(self.cost))
            del self.final_cost[:-1]
            self.total = sum(self.final_cost)

            for widgets in self.order_frm.winfo_children():
                widgets.destroy()

            self.display_cost()
        
        else:
            self.quantity[chosen_item] += 1
            self.food_ordered.append(item)
            cost_item = self.prices[chosen_item] * self.quantity[chosen_item]
            self.cost[chosen_item] = cost_item

            if len(self.current_cost) == 1:
                del self.current_cost[0]

            self.current_cost.append(sum(self.cost))
            self.display_cost(True)

    def calc_total(self):
        '''Calculates the current total whenever the user adds an item or changes the category of food.'''
        if len(self.current_cost) > 0:
            t = self.current_cost.pop(-1)
            self.final_cost.append(t)
            del self.final_cost[:-1]
            del self.current_cost[:]
            if len(self.final_cost) >= 2:
                self.total = sum(self.final_cost)
                return self.total   

            self.total = sum(self.final_cost)
            return self.total


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