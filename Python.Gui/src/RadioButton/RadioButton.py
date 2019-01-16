#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
  
    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.radioButtonVar = tkinter.IntVar()
    self.radioButtonVar.set(0)
    
    self.radioButton1 = tkinter.ttk.Radiobutton(self.frame, text="radioButton 1", value=0, variable=self.radioButtonVar)
    self.radioButton1.place(x = 30, y = 30) 

    self.radioButton2 = tkinter.ttk.Radiobutton(self.frame, text="radioButton 2", value=1, variable=self.radioButtonVar)
    self.radioButton2.place(x = 30, y = 60)

    self.radioButton3 = tkinter.ttk.Radiobutton(self.frame, text="radioButton 3", value=2, variable=self.radioButtonVar)
    self.radioButton3.place(x = 30, y = 90) 

    self.geometry("300x300+200+100")
    self.title("RadioButton Example")

  def main(self=None):    
    form = Form1()
    form.mainloop()
 
if __name__ == '__main__':
  Form1.main()
  
