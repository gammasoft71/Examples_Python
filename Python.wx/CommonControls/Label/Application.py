#!/usr/bin/env python3
# -*-coding:utf-8 -*

import wx

class Program:
  def main(self=None):
    application = wx.App()
    wx.Frame(None).Show()
    application.MainLoop()

if __name__ == '__main__':
  Program.main()
