#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.colorchooser
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()

    self.button = tkinter.ttk.Button(self, command=self.OnButtonClick, text='Color...')
    self.button.place(x=10, y=10)

    self.geometry('300x300+200+100')
    self.title('ColorDialog example')

  def main(self=None):
    form = Form1()
    form.mainloop()

  def OnButtonClick(self):
    color = tkinter.colorchooser.askcolor(color=self['background'], parent=self)
    if color[1]:
      self['background'] = color[1]

if __name__ == '__main__':
  Form1.main()
