#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.font
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
    
    self.panel = tkinter.ttk.Frame(self)
    self.panel.pack(fill = tkinter.BOTH, expand=1)

    self.label1 = tkinter.ttk.Label(self.panel, text="label1")
    self.label1.place(x=10, y=10)

    self.geometry("300x300+200+100")
    self.title("Label example")

  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
