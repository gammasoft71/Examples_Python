#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.font
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
    
    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.label = tkinter.ttk.Label(self.frame, font=tkinter.font.Font(family='Arial', size=-46, weight='bold', slant='italic'), foreground="green", text="Hello, World!")
    self.label.place(x=5, y=100)

    self.geometry("300x300+200+100")
    self.title("My first application")

  def main():
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
