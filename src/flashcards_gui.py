'''
Created on Mar 23, 2020

@author: sd931e
'''

import tkinter as tk

class FlashcardsApp:
    def __init__(self):
        root = tk.Tk()
        app = FlashcardsGUI(master=root)
        app.mainloop()
    
    def start_screen(self):
        pass

class FlashcardsGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.start_screen()
        
    def start_screen(self):
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.start_round
        self.start_button.pack(side="left")
        
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="left")
        
    def start_round(self):
        print("Start round")
        
        # TODO load deck - meanwhile, hardcode a loaded deck
        self.select_button = tk.Button(self)
        self.select_button["text"] = "Select deck"
        self.select_button.pack(side="right")
        
