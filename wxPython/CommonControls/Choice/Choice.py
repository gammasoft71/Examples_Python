#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None, wx.ID_ANY, 'Choice example', wx.DefaultPosition, wx.Size(300, 300))
    self.panel = wx.Panel(self)

    self.choice1 = wx.Choice(self.panel, wx.ID_ANY, wx.Point(10, 10))
    self.choice1.AppendItems(["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10"])
    self.choice1.SetSelection(0)
    self.choice1.Bind(wx.EVT_CHOICE, self.OnChoiceClick)

    self.choice2 = wx.Choice(self.panel, wx.ID_ANY, wx.Point(10, 50))
    self.choice2.AppendItems(["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10"])
    self.choice2.SetSelection(0)    
    self.choice2.Bind(wx.EVT_CHOICE, self.OnChoiceClick)

  def OnChoiceClick(self, event):
    self.choice1.SetSelection(event.GetEventObject().GetSelection())
    self.choice2.SetSelection(event.GetEventObject().GetSelection())

application = wx.App()
Frame1().Show()
application.MainLoop()
