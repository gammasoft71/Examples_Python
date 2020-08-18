#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
    
    self.counter = 0
    self.destroyed = False

    self.geometry('300x300+200+100')
    self.protocol('WM_DELETE_WINDOW', self.OnQuit)
    self.title('')
    
  def main(self=None):    
    form = Form1()
    while not form.destroyed:
      form.after_idle(form.OnIdle)
      form.update_idletasks()
      form.update()

  def OnIdle(self):
    self.counter += 1
    self.title(str(self.counter))

  def OnQuit(self):
    self.destroyed = True
    self.destroy()

if __name__ == '__main__':
  Form1.main()
