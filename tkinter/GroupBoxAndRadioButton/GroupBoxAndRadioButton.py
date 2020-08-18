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

    self.groupBox1 = tkinter.ttk.LabelFrame(self.frame, text="Group 1", height=140, width=135)
    self.groupBox1.place(x=10, y=10)

    self.radioButtonGroup1Var = tkinter.IntVar()
    self.radioButtonGroup1Var.set(0)
    
    self.radioButton1 = tkinter.ttk.Radiobutton(self.groupBox1, text="radio 1", value=0, variable=self.radioButtonGroup1Var)
    self.radioButton1.place(x = 10, y = 10) 
    
    self.radioButton2 = tkinter.ttk.Radiobutton(self.groupBox1, text="radio 2", value=1, variable=self.radioButtonGroup1Var)
    self.radioButton2.place(x = 10, y = 40) 
    
    self.radioButton3 = tkinter.ttk.Radiobutton(self.groupBox1, text="radio 3", value=2, variable=self.radioButtonGroup1Var)
    self.radioButton3.place(x = 10, y = 70) 

    self.groupBox2 = tkinter.ttk.LabelFrame(self.frame, text="Group 2", height=140, width=135)
    self.groupBox2.place(x=155, y=10)

    self.radioButtonGroup2Var = tkinter.IntVar()
    self.radioButtonGroup2Var.set(1)
    
    self.radioButton4 = tkinter.ttk.Radiobutton(self.groupBox2, text="radio 4", value=0, variable=self.radioButtonGroup2Var)
    self.radioButton4.place(x = 10, y = 10) 
    
    self.radioButton5 = tkinter.ttk.Radiobutton(self.groupBox2, text="radio 5", value=1, variable=self.radioButtonGroup2Var)
    self.radioButton5.place(x = 10, y = 40) 
    
    self.radioButton6 = tkinter.ttk.Radiobutton(self.groupBox2, text="radio 6", value=2, variable=self.radioButtonGroup2Var)
    self.radioButton6.place(x = 10, y = 70) 

    self.geometry("300x160+200+100")
    self.title("GroupBox and CheckBox example")
   
  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
