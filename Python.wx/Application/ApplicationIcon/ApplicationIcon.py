#!/usr/bin/env python3
# -*-coding:utf-8 -*

import os
import wx

class Program:
  def Main():
    application = wx.App()
    frame = wx.Frame(None)
    frame.SetIcon(wx.Icon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "Gammasoft.ico")))
    frame.Show()
    application.MainLoop()

if __name__ == '__main__':
  Program.Main()
