#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.messagebox
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()

    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.groupBox1 = tkinter.ttk.LabelFrame(self.frame, text="GroupBox 1", height=460, width=305)
    self.groupBox1.place(x=10, y=10)

    self.groupBox2 = tkinter.ttk.LabelFrame(self.frame, height=460, width=305)
    self.groupBox2.place(x=325, y=10)

    self.geometry("640x480+200+100")
    self.title("GroupBox example")

  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
