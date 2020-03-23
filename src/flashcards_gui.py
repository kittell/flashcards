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
        self.start = tk.Button(self)
        self.start["text"] = "Start"
        self.start["command"] = self.start_round
        self.start.pack(side="left")
        
        self.quit = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit.pack(side="left")
        
    def start_round(self):
        print("Start round")