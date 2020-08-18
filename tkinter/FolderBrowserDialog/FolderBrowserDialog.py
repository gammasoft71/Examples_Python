#!/usr/bin/env python3
# -*-coding:utf-8 -*

import os
import platform
import tkinter
import tkinter.filedialog
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()

    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.button = tkinter.ttk.Button(self.frame, command=self.OnButtonClick, text='Folder...')
    self.button.place(x=10, y=10)

    self.label = tkinter.ttk.Label(self.frame, text='Path = ')
    self.label.place(x=10, y=40)

    self.geometry('300x300+200+100')
    self.title('FolderBrowser example')

  def main(self=None):
    form = Form1()
    form.mainloop()

  def OnButtonClick(self):
    directory = tkinter.filedialog.askdirectory(initialdir=os.path.join(os.environ['HOMEPATH' if platform.system() == 'Windows' else 'HOME'], 'Desktop'))
    if directory:
      self.label['text'] = 'Path = {}'.format(directory)

if __name__ == '__main__':
  Form1.main()
