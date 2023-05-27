import time
import tkinter as tk
from tkinter import messagebox

class FocusClock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("专注时钟")
        self.window.geometry("300x150")
        
        self.time_var = tk.StringVar()
        self.time_var.set("25")
        
        time_label = tk.Label(self.window, text="专注时长（分钟）:")
        time_label.pack()
        
        time_entry = tk.Entry(self.window, textvariable=self.time_var)
        time_entry.pack()
        
        start_button = tk.Button(self.window, text="开始", command=self.start_timer)
        start_button.pack()
        
        self.timer_running = False
        
        self.window.mainloop()
    
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            remaining_time = int(self.time_var.get()) * 60
            
            while remaining_time > 0:
                mins, secs = divmod(remaining_time, 60)
                time_str = '{:02d}:{:02d}'.format(mins, secs)
                self.window.title(time_str)
                time.sleep(1)
                remaining_time -= 1
            
            self.timer_running = False
            self.window.title('时间到！')
            messagebox.showinfo(title="时间到！", message="专注任务完成！")
            
clock = FocusClock()
