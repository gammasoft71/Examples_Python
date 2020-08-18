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

    self.geometry("300x300+200+100")
    self.title("Click anywhere on the form")
    self.bind("<Button-1>", self.OnFormClick)

  def main(self=None):
    form = Form1()
    form.mainloop()

  def OnFormClick(self, event):
    tkinter.messagebox.showinfo(message="The form is clicked at {{X={},Y={}}}".format(event.x, event.y), parent=self, title="FormClick")

if __name__ == '__main__':
  Form1.main()
