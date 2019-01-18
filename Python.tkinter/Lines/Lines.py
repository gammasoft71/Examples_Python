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

    self.lineSeparator = tkinter.LabelFrame(self.panel, height=2, width=280)
    self.lineSeparator.place(x=10, y=10)

    self.lineRed = tkinter.LabelFrame(self.panel, borderwidth=0, background="red", height=250, width=2)
    self.lineRed.place(x=10, y=20)

    self.lineGreen = tkinter.LabelFrame(self.panel, borderwidth=0, background="green", height=250, width=2)
    self.lineGreen.place(x=149, y=20)

    self.lineBlue = tkinter.LabelFrame(self.panel, borderwidth=0, background="blue", height=250, width=2)
    self.lineBlue.place(x=288, y=20)

    self.lineSeparator2 = tkinter.LabelFrame(self.panel, borderwidth=1, height=2, width=280)
    self.lineSeparator2.place(x=10, y=278)

    self.geometry("300x300+200+100")
    self.title("Label example")

  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
