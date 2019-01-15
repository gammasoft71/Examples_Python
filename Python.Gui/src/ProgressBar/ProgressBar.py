#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()    

    self.frame = tkinter.ttk.Frame(self.master)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.frameProgressBar1 = tkinter.ttk.Frame(self.frame, width=200, height=25)
    self.frameProgressBar1.pack_propagate(0)
    self.frameProgressBar1.place(x = 50, y = 50)

    self.progressBar1 = tkinter.ttk.Progressbar(self.frameProgressBar1, orient="horizontal")
    self.progressBar1.pack(fill = tkinter.BOTH, expand=1)

    self.frameProgressBar2 = tkinter.ttk.Frame(self.frame, width=200, height=25)
    self.frameProgressBar2.pack_propagate(0)
    self.frameProgressBar2.place(x = 50, y = 80)

    self.progressBar2 = tkinter.ttk.Progressbar(self.frameProgressBar2, maximum=100, orient="horizontal", value=50)
    self.progressBar2.pack(fill = tkinter.BOTH, expand=1)

    self.frameProgressBar3 = tkinter.ttk.Frame(self.frame, width=200, height=25)
    self.frameProgressBar3.pack_propagate(0)
    self.frameProgressBar3.place(x = 50, y = 110)

    self.progressBar3 = tkinter.ttk.Progressbar(self.frameProgressBar3, maximum=300, orient="horizontal", value=300)
    self.progressBar3.pack(fill = tkinter.BOTH, expand=1)

    self.frameProgressBar4 = tkinter.ttk.Frame(self.frame, width=200, height=25)
    self.frameProgressBar4.pack_propagate(0)
    self.frameProgressBar4.place(x = 50, y = 140)

    self.progressBar4 = tkinter.ttk.Progressbar(self.frameProgressBar4, maximum=200, orient="horizontal", value=0)
    self.progressBar4.pack(fill = tkinter.BOTH, expand=1)

    self.frameProgressBar5 = tkinter.ttk.Frame(self.frame, width=200, height=25)
    self.frameProgressBar5.pack_propagate(0)
    self.frameProgressBar5.place(x = 50, y = 170)

    self.progressBar5 = tkinter.ttk.Progressbar(self.frameProgressBar5, mode="indeterminate", orient="horizontal")
    self.progressBar5.pack(fill = tkinter.BOTH, expand=1)
    self.progressBar5.start()

    self.after(50, self.OnProgressBar4Update)
    self.geometry("300x300+200+100")
    self.title("TrackBar Example")
    
  def main():    
    form = Form1()
    form.mainloop()
    
  def OnProgressBar4Update(self):
    self.progressBar4["value"] = self.progressBar4["value"] + 1 if self.progressBar4["value"] < self.progressBar4["maximum"] else 0
    self.after(50, self.OnProgressBar4Update)

if __name__ == '__main__':
  Form1.main()
