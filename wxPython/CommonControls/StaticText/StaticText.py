#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None, wx.ID_ANY, 'Static text example', wx.DefaultPosition, wx.Size(300, 300))
    self.panel = wx.Panel(self)
    self.staticText1 = wx.StaticText(self.panel, wx.ID_ANY, 'staticText1', wx.Point(10, 10))
    
application = wx.App()
Frame1().Show()
application.MainLoop()
