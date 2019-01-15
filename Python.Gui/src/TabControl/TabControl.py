#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
    
    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.tabControl = tkinter.ttk.Notebook(self.frame, width=320, height=200)
    self.tabControl.place(x=10, y=10)

    self.tabPage1 = tkinter.ttk.Frame(self.tabControl)
    self.tabControl.add(self.tabPage1, text='tabPage1')
    
    self.tabPage2 = tkinter.ttk.Frame(self.tabControl)
    self.tabControl.add(self.tabPage2, text='tabPage2')
    
    self.tabPage3 = tkinter.ttk.Frame(self.tabControl)
    self.tabControl.add(self.tabPage3, text='tabPage3')
    
    self.geometry("390x270+200+100")
    self.title("TabControl Example")

  def main():
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
