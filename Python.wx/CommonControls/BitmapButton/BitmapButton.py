#!/usr/bin/env python3
# -*-coding:utf-8 -*

import os
import wx

class Frame1(wx.Frame):
  def __init__(self, parent=None):
    super().__init__(parent, wx.ID_ANY, 'Bitmap button example', wx.DefaultPosition, wx.Size(300, 300))
    self.button1Clicked = 0
    self.button2Clicked = 0
    self.panel = wx.Panel(self)
    self.button1 = wx.Button(self.panel, wx.ID_ANY, 'Gammasoft', wx.Point(50, 50))
    self.button2 = wx.Button(self.panel, wx.ID_ANY, 'Gammasoft', wx.Point(50, 80))
    self.button3 = wx.Button(self.panel, wx.ID_ANY, 'Gammasoft', wx.Point(50, 110))
    self.button4 = wx.Button(self.panel, wx.ID_ANY, wx.EmptyString, wx.Point(50, 155))
    
    self.button2.SetBitmapLabel(wx.Bitmap(wx.Image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "gammasoft_16x16.xpm"))));
    self.button2.SetBitmapPosition(wx.LEFT);
    self.button2.SetSize(120, 25);
        
    self.button3.SetBitmapLabel(wx.Bitmap(wx.Image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "gammasoft_32x32.xpm"))));
    self.button3.SetBitmapPosition(wx.LEFT);
    self.button3.SetSize(140, 40);
        
    self.button4.SetBitmapLabel(wx.Bitmap(wx.Image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "gammasoft_64x64.xpm"))));
    self.button4.SetSize(70, 70);
        
  def Main(self=None):
    application = wx.App()
    #swx.InitAllImageHandlers()
    Frame1(None).Show()
    application.MainLoop()

if __name__ == '__main__':
  Frame1.Main()
