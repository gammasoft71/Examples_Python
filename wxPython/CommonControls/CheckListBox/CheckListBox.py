#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None, wx.ID_ANY, 'Check list box example')
    self.SetClientSize(200, 240)
    self.panel = wx.Panel(self)
    self.checkListBox = wx.CheckListBox(self.panel, wx.ID_ANY, wx.Point(20, 20), wx.Size(160, 200))
    
    for index in range(1, 21):
      self.checkListBox.Append("Item {}".format(index))
      self.checkListBox.Check(index - 1, index % 2 != 0)
      self.checkListBox.EnsureVisible(0)

application = wx.App()
Frame1().Show()
application.MainLoop()
