#!/usr/bin/env python3
# -*-coding:utf-8 -*

# You must install Pillow package before use it :
# pip install Pillow
# More information :  https://pillow.readthedocs.io/en/3.0.x/index.html

import os
import tkinter
import tkinter.font
import tkinter.ttk
import PIL.ImageTk
import PIL.Image

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
    
    self.panel = tkinter.ttk.Frame(self)
    self.panel.pack(fill = tkinter.BOTH, expand=1)

    self.image1 = PIL.ImageTk.PhotoImage(PIL.Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "Logo.png")))
    self.pictureBox1 = tkinter.ttk.Label(self.panel, image=self.image1, borderwidth=2, relief="groove")
    self.pictureBox1.place(x=20, y=20)

    self.geometry("300x300+200+100")
    self.title("PictureBox example")

  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
