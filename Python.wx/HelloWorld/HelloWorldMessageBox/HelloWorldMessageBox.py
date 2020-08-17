#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None)
    self.SetClientSize(300, 300);
    self.SetLabel('Hello world! (message dialog)')
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.button = wx.Button(self.panel, wx.ID_ANY, 'Click me', wx.Point(10, 10))
    self.button.Bind(wx.EVT_BUTTON, self.OnButtonClick)

  def OnButtonClick(self, event):
    wx.MessageDialog(None, "Hello, World!").ShowModal()

  def Main(self=None):
    application = wx.App()
    Frame1().Show()
    application.MainLoop()

if __name__ == '__main__':
  Frame1.Main()
