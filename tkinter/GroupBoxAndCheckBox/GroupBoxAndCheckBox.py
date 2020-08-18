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

    self.checkBoxVar1 = tkinter.BooleanVar()
    self.checkBoxVar1.set(False)
    
    self.checkBox1 = tkinter.ttk.Checkbutton(self.groupBox1, text="check 1", variable=self.checkBoxVar1)
    self.checkBox1.place(x = 10, y = 10) 
    
    self.checkBoxVar2 = tkinter.BooleanVar()
    self.checkBoxVar2.set(True)
    
    self.checkBox2 = tkinter.ttk.Checkbutton(self.groupBox1, text="check 2", variable=self.checkBoxVar2)
    self.checkBox2.place(x = 10, y = 40) 
    
    self.checkBoxVar3 = tkinter.BooleanVar()
    self.checkBoxVar3.set(False)

    self.checkBox3 = tkinter.ttk.Checkbutton(self.groupBox1, text="check 3", variable=self.checkBoxVar3)
    self.checkBox3.place(x = 10, y = 70) 

    self.groupBox2 = tkinter.ttk.LabelFrame(self.frame, text="Group 2", height=140, width=135)
    self.groupBox2.place(x=155, y=10)

    self.checkBoxVar4 = tkinter.BooleanVar()
    self.checkBoxVar4.set(False)
    
    self.checkBox4 = tkinter.ttk.Checkbutton(self.groupBox2, text="check 4", variable=self.checkBoxVar4)
    self.checkBox4.place(x = 10, y = 10) 
    
    self.checkBoxVar5 = tkinter.BooleanVar()
    self.checkBoxVar5.set(False)
    
    self.checkBox5 = tkinter.ttk.Checkbutton(self.groupBox2, text="check 5", variable=self.checkBoxVar5)
    self.checkBox5.place(x = 10, y = 40) 
    
    self.checkBoxVar6 = tkinter.BooleanVar()
    self.checkBoxVar6.set(True)

    self.checkBox6 = tkinter.ttk.Checkbutton(self.groupBox2, text="check 6", variable=self.checkBoxVar6)
    self.checkBox6.place(x = 10, y = 70) 

    self.geometry("300x160+200+100")
    self.title("GroupBox and CheckBox example")
   
  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
