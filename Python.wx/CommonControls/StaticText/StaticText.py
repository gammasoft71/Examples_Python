#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self, parent=None):
    super().__init__(parent, wx.ID_ANY, 'Static text example', wx.DefaultPosition, wx.Size(300, 300))
    self.panel = wx.Panel(self)
    self.staticText1 = wx.StaticText(self.panel, wx.ID_ANY, 'staticText1', wx.Point(10, 10))
    
  def main(self=None):
    application = wx.App()
    Frame1(None).Show()
    application.MainLoop()

if __name__ == '__main__':
  Frame1.main()
