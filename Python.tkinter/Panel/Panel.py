#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.messagebox
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()

    self.panel = tkinter.ttk.Frame(self)
    self.panel.pack(fill = tkinter.BOTH, expand=1)

    self.panel1 = tkinter.LabelFrame(self.panel, height=460, width=305)
    self.panel1.place(x=10, y=10)

    self.panel2 = tkinter.LabelFrame(self.panel, borderwidth=1, height=460, width=305)
    self.panel2.place(x=325, y=10)

    self.geometry("640x480+200+100")
    self.title("Panel example")

  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
