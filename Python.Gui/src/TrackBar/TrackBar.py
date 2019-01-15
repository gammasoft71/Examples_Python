#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()    

    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.frameTrackBar = tkinter.ttk.Frame(self.frame, width=200, height=25)
    self.frameTrackBar.pack_propagate(0)
    self.frameTrackBar.place(x = 20, y = 50)

    self.value = tkinter.DoubleVar()
    self.value.set(100.0)

    self.trackBar = tkinter.ttk.Scale(self.frameTrackBar, command=self.OnTrackBarChanged, from_=0, orient="horizontal", to=200, variable=self.value)
    self.trackBar.pack(fill = tkinter.BOTH, expand=1)

    self.frameProgressBar = tkinter.ttk.Frame(self.frame, width=200, height=25)
    self.frameProgressBar.pack_propagate(0)
    self.frameProgressBar.place(x = 20, y = 100)

    self.progressBar = tkinter.ttk.Progressbar(self.frameProgressBar, maximum=200, orient="horizontal", variable=self.value)
    self.progressBar.pack(fill = tkinter.BOTH, expand=1)

    self.label1 = tkinter.ttk.Label(self.frame, textvariable=self.value)
    self.label1.place(x=20, y=150) 

    self.geometry("300x300+200+100")
    self.title("TrackBar Example")
    
  def main():    
    form = Form1()
    form.mainloop()
  
  def OnTrackBarChanged(self, e=None):
    value = self.trackBar.get()
    if int(value) != value:
      self.trackBar.set(round(value))

if __name__ == '__main__':
  Form1.main()
