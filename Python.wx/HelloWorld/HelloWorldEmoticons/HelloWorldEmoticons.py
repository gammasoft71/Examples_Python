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
    self.SetLabel('Hello world! (emoticons)')
    self.staticText = wx.StaticText(self, wx.ID_ANY, '\U0001F44B, \U0001F30E\U00002757')
    self.staticText.SetFont(wx.Font(PointsToNativeFontGraphicsUntit(72), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    self.SetClientSize(self.staticText.GetSize());

  def Main(self=None):
    application = wx.App()
    Frame1().Show()
    application.MainLoop()

if __name__ == '__main__':
  Frame1.Main()
