#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

def OnButtonClick(event):
  wx.MessageDialog(None, "Hello, World!").ShowModal()

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, 'Hello world! (message dialog)', wx.DefaultPosition, wx.Size(300, 300))
frame.panel = wx.Panel(frame, wx.ID_ANY)
frame.button = wx.Button(frame.panel, wx.ID_ANY, 'Click me', wx.Point(10, 10))
frame.button.Bind(wx.EVT_BUTTON, OnButtonClick)
frame.Show()
application.MainLoop()
