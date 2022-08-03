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
        
        # Imports the other classes used in this application
        from ordering import Student
        from manage import Admin 

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


        student_btn = ttk.Button(self.window, text="Student", 
                                command=lambda: self.open_window(Student))

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
        self.TEntry.configure("EntryStyle.TEntry", )\

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

if __name__ == "__main__": 
    app = MainApp()
    app.mainloop()