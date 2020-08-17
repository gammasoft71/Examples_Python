#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

def PointsToNativeFontGraphicsUntit(size):
  import platform
  # On macos font is in pixels and not in points
  return size if platform.system() != 'Darwin' else float(size) / wx.ScreenDC().GetPPI().GetHeight() * 96.0

class Frame1(wx.Frame):
  def __init__(self):
    super().__init__(None)
    self.SetClientSize(300, 300);
    self.SetLabel('Hello world! (static text)')
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.staticText = wx.StaticText(self.panel, wx.ID_ANY, 'Hello, World!', wx.Point(5, 100))
    self.staticText.SetFont(wx.Font(PointsToNativeFontGraphicsUntit(32), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD))
    self.staticText.SetForegroundColour(wx.TheColourDatabase.Find("Forest Green"))

  def Main(self=None):
    application = wx.App()
    Frame1().Show()
    application.MainLoop()

if __name__ == '__main__':
  Frame1.Main()
