from canteen_app import *

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
        self.menu_frm.grid(row=1, columnspan=8, padx=10, pady=10)

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
        item = f"{self.current_items[chosen_item]}"
        old_quantity = self.current_quantity[chosen_item]

        if len(self.total_quantity[self.current_category]) != 0:
            self.current_quantity[:] = self.total_quantity[self.current_category]
            self.current_category_cost[:] = self.total_category_cost[self.current_category]
            old_quantity = self.current_quantity[chosen_item]
        

        if remove_item: # Checks if user wishes to remove an item
            if self.current_quantity[chosen_item] == 0:
                return

            try:
                self.food_ordered.remove(f"{old_quantity}x {item}")
            except:
                return

            self.current_quantity = self.total_quantity[self.current_category]
            self.current_category_cost = self.total_category_cost[self.current_category] 
            self.current_quantity[chosen_item] -= 1

            self.food_ordered.append(f"{self.current_quantity[chosen_item]}x {item}")
            new_cost_item = self.prices[chosen_item] * self.current_quantity[chosen_item]
            self.current_category_cost[chosen_item] = new_cost_item

            for widgets in self.order_frm.winfo_children():
                widgets.destroy()

            self.create_total_cost()      

        else:
            if self.current_quantity[chosen_item] >= 5:
                tkinter.messagebox.showinfo("Maxium Quantity", "Please do not add an item more than 5x.")               
                return 
                
            self.current_quantity[chosen_item] += 1
        
            if f"{old_quantity}x {item}" in self.food_ordered:
                self.food_ordered.remove(f"{old_quantity}x {item}")

            self.food_ordered.append(f"{self.current_quantity[chosen_item]}x {item}")
            
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

        self.order_frm.grid(row=2, columnspan=8, padx=10, pady=10)
        ordered_lbl.grid(row=1, column=1, padx=5, pady=5)
        cost_lbl.grid(row=2, column=1, padx=5, pady=5)