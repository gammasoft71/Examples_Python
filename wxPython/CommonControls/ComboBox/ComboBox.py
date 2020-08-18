#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx
import platform

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None, wx.ID_ANY, 'Combo box example', wx.DefaultPosition, wx.Size(300, 300))
    self.panel = wx.Panel(self)

    self.comboBox1 = wx.ComboBox(self.panel, wx.ID_ANY, wx.EmptyString, wx.Point(10, 10))
    self.comboBox1.AppendItems(["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10"])
    self.comboBox1.SetSelection(0)
    self.comboBox1.Bind(wx.EVT_COMBOBOX, self.OnComboBoxClick)

    self.comboBox2 = wx.ComboBox(self.panel, wx.ID_ANY, wx.EmptyString, wx.Point(10, 50), wx.DefaultSize, [], wx.CB_READONLY)
    self.comboBox2.AppendItems(["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10"])
    self.comboBox2.SetSelection(0)
    self.comboBox2.Bind(wx.EVT_COMBOBOX, self.OnComboBoxClick)

    self.comboBox3 = wx.ComboBox(self.panel, wx.ID_ANY, wx.EmptyString, wx.Point(10, 90), wx.Size(110, 163) if platform.system() == 'Windows' else wx.DefaultSize, [], wx.CB_SIMPLE)
    self.comboBox3.AppendItems(["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10"])
    self.comboBox3.SetSelection(0)
    self.comboBox3.Bind(wx.EVT_COMBOBOX, self.OnComboBoxClick)

  def OnComboBoxClick(self, event):
    self.comboBox1.SetSelection(event.GetEventObject().GetSelection())
    self.comboBox2.SetSelection(event.GetEventObject().GetSelection())
    self.comboBox3.SetSelection(event.GetEventObject().GetSelection())

application = wx.App()
Frame1().Show()
application.MainLoop()
