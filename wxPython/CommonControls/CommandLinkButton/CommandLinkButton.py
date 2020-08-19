#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx
import wx.adv

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None, wx.ID_ANY, 'Command link button example', wx.DefaultPosition, wx.Size(300, 300))
    self.commandLinkButton1Clicked = 0
    self.panel = wx.Panel(self)
    self.commandLinkButton1 = wx.adv.CommandLinkButton(self.panel, wx.ID_ANY, 'Link', 'Information text', wx.Point(30, 30), wx.Size(200, 60))
    self.commandLinkButton1.Bind(wx.EVT_BUTTON, self.OnCommandLinkButton1Click)
    self.staticText1 = wx.StaticText(self.panel, wx.ID_ANY, 'commandLinkButton1 clicked 0 times', wx.Point(30, 100), wx.Size(200, 50))
    
  def OnCommandLinkButton1Click(self, event):
    self.commandLinkButton1Clicked += 1
    self.staticText1.SetLabel('commandLinkButton1 clicked {0} times'.format(self.commandLinkButton1Clicked))
   
application = wx.App()
Frame1().Show()
application.MainLoop()
