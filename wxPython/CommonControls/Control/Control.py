#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None, wx.ID_ANY, 'Control example', wx.DefaultPosition, wx.Size(300, 300))
    self.panel = wx.Panel(self)
    self.control1 = wx.Control(self.panel, wx.ID_ANY, wx.Point(50, 50), wx.Size(100, 50))
    self.control1.SetBackgroundColour(wx.TheColourDatabase.Find("Spring Green"));
    self.control1.Bind(wx.EVT_LEFT_DOWN, self.OnControlLeftDown)

  def OnControlLeftDown(self, event):
    self.control1.SetBackgroundColour(wx.TheColourDatabase.Find("Orange Red") if self.control1.GetBackgroundColour() == wx.TheColourDatabase.Find("Spring Green") else wx.TheColourDatabase.Find("Spring Green"))
    self.control1.Refresh()
    
application = wx.App()
Frame1().Show()
application.MainLoop()
