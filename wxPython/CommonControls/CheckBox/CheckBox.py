#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None, wx.ID_ANY, 'Check box example', wx.DefaultPosition, wx.Size(300, 300))
    self.panel = wx.Panel(self)
    
    self.checkBox1 = wx.CheckBox(self.panel, wx.ID_ANY, 'Unchecked', wx.Point(30, 30), wx.Size(200, wx.DefaultCoord))
    self.checkBox1.Bind(wx.EVT_CHECKBOX, self.OnCheckBox1Click)
    
    self.checkBox2 = wx.CheckBox(self.panel, wx.ID_ANY, 'Checked', wx.Point(30, 60), wx.Size(200, wx.DefaultCoord))
    self.checkBox2.SetValue(True)
    self.checkBox2.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClick)

    self.checkBox3 = wx.CheckBox(self.panel, wx.ID_ANY, 'Indeterminate', wx.Point(30, 90), wx.Size(200, wx.DefaultCoord), wx.CHK_3STATE | wx.CHK_ALLOW_3RD_STATE_FOR_USER)
    self.checkBox3.Set3StateValue(wx.CHK_UNDETERMINED)
    self.checkBox3.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClick)
    
  def OnCheckBox1Click(self, event):
    self.checkBox1.SetValue(False)

  def OnCheckBoxClick(self, event):
    event.GetEventObject().SetLabel(self.ToString(event.GetEventObject().Get3StateValue()))

  def ToString(self, state):
    if state == wx.CHK_UNCHECKED: return "Unchecked"
    if state == wx.CHK_CHECKED: return "Checked"
    return "Indeterminate"
  
application = wx.App()
Frame1().Show()
application.MainLoop()
