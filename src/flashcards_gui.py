import tkinter as tk
from tkinter import ttk

class FlashcardsGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_main = ttk.Frame(self, padding=5)
        
        def callback_start_round():
            print("Start round")
            
            # TODO load deck - meanwhile, hardcode a loaded deck
            self.select_button = tk.Button(self)
            self.select_button["text"] = "Select deck"
            self.select_button.pack(side="right")
    
        self.title('Flashcards')
        self.frame_main.grid()
        
        
        self.quit_button = tk.Button(self.frame_main, text='Quit', command=self.destroy)
        self.quit_button.grid()


