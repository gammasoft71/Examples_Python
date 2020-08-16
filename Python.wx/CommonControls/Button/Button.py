#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self, parent=None):
    super().__init__(parent, wx.ID_ANY, 'Button example', wx.DefaultPosition, wx.Size(300, 300))
    self.button1Clicked = 0
    self.button2Clicked = 0
    self.panel = wx.Panel(self)
    self.button1 = wx.Button(self.panel, wx.ID_ANY, 'button1', wx.Point(50, 50))
    self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Click)
    self.button2 = wx.Button(self.panel, wx.ID_ANY, 'button2', wx.Point(50, 100), wx.Size(200, 75))
    self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Click)
    self.staticText1 = wx.StaticText(self.panel, wx.ID_ANY, 'button1 clicked 0 times', wx.Point(50, 200))
    self.staticText2 = wx.StaticText(self.panel, wx.ID_ANY, 'button2 clicked 0 times', wx.Point(50, 230))
    
  def OnButton1Click(self, event):
    self.button1Clicked = self.button1Clicked + 1
    self.staticText1.SetLabel('button1 clicked {0} times'.format(self.button1Clicked))
    
  def OnButton2Click(self, event):
    self.button2Clicked = self.button2Clicked + 1
    self.staticText2.SetLabel('button2 clicked {0} times'.format(self.button2Clicked))
        
  def Main(self=None):
    application = wx.App()
    Frame1(None).Show()
    application.MainLoop()

if __name__ == '__main__':
  Frame1.Main()
