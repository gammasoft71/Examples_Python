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

    self.button1 = tkinter.ttk.Button(self.frame, command=self.OnExit, text="Close")
    self.button1.place(x=10, y=10)

    self.geometry("300x300+200+100")
    self.protocol('WM_DELETE_WINDOW', self.OnExit)
    self.title("Form example")

  def main(self=None):
    form = Form1()
    form.mainloop()

  def OnExit(self):
    if tkinter.messagebox.askyesno(message="Are you sure you want exit?", parent=self, title="Close Form") == True:
      self.destroy()

if __name__ == '__main__':
  Form1.main()
