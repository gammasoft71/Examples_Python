#!/usr/bin/env python3
# -*-coding:utf-8 -*

import os
import tkinter

class Program:
  def main(self=None):
    application = tkinter.Tk()
    application.iconbitmap('Resources/Python.ico' if os.path.isfile('Resources/Python.ico') else None)
    application.mainloop()

if __name__ == '__main__':
  Program.main()
  