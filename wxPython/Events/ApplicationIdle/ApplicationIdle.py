#!/usr/bin/env python3
# -*-coding:utf-8 -*

import time
import wx

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None)
    self.counter = 0
    self.lastIdleTime = 0
    wx.App.Get().Bind(wx.EVT_IDLE, self.OnApplicationIdle)

  def OnApplicationIdle(self, event):
    elapsedTime = time.time_ns() - self.lastIdleTime;
    if elapsedTime >= 100000000: # 100 ms
      self.counter = self.counter + 1
      self.SetLabel("{0}".format(self.counter))
      self.lastIdleTime = time.time_ns()
    event.RequestMore()

application = wx.App()
Frame1().Show()
application.MainLoop()
