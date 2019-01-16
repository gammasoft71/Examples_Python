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

    self.button1 = tkinter.ttk.Button(self.frame, command=self.OnClickMeClick, text="Click me")
    self.button1.place(x=10, y=10)

    self.geometry("300x300+200+100")
    self.title("Hello World Form")

  def main(self=None):
    form = Form1()
    form.mainloop()

  def OnClickMeClick(self):
    tkinter.messagebox.showinfo(message="Hello World", parent=self)

if __name__ == '__main__':
  Form1.main()
