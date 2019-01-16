#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
    
    self.button1Clicked = 0
    self.button2Clicked = 0

    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.button1 = tkinter.ttk.Button(self.frame, command=self.OnButton1Click, text="button1")
    self.button1.place(x=50, y=50)
    
    self.frameButton = tkinter.ttk.Frame(self.frame, width=200, height=75)
    self.frameButton.pack_propagate(0)
    self.frameButton.place(x = 50, y = 100)
    self.button2 = tkinter.ttk.Button(self.frameButton, command=self.OnButton2Click, text="button2")
    self.button2.pack(fill = tkinter.BOTH, expand=1)
    
    self.label1 = tkinter.ttk.Label(self.frame, text="button1 clicked {0} times".format(self.button1Clicked))
    self.label1.place(x=50, y=200) 
    
    self.label2 = tkinter.ttk.Label(self.frame, text="button2 clicked {0} times".format(self.button2Clicked))
    self.label2.place(x=50, y=230) 

    self.geometry("300x300+200+100")
    self.title("")
    
  def main(self=None):    
    form = Form1()
    form.mainloop()
  
  def OnButton1Click(self):
    self.button1Clicked += 1
    self.label1["text"] = "button1 clicked {0} times".format(self.button1Clicked)
  
  def OnButton2Click(self):
    self.button2Clicked += 1
    self.label2["text"] = "button2 clicked {0} times".format(self.button2Clicked)

if __name__ == '__main__':
  Form1.main()
