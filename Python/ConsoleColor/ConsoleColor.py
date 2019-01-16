#!/usr/bin/env python3
# -*-coding:utf-8 -*

# @remarks To enable ANSI colors on Windows, add following key in the registry :
# [HKEY_CURRENT_USER\Console] "VirtualTerminalLevel"=dword:00000001

import sys

class Program:
  def main(self=None):
    FOREGROUND_BLUE = '\033[94m'
    FOREGROUND_YELLOW = '\033[93m'
    FOREGROUND_DARK_GRAY = '\033[90m'
    FOREGROUND_RESET = '\033[00m'

    print(FOREGROUND_BLUE + '                          ▄▄▄█████████████████▄▄▄')
    print(FOREGROUND_BLUE + '                        ▄██████████████████████████████▄')
    print(FOREGROUND_BLUE + '                      ████████████████████████████████████')
    print(FOREGROUND_BLUE + '                     █████▀    ▀███████████████████████████')
    print(FOREGROUND_BLUE + '                     ████▌      ▐██████████████████████████▌')
    print(FOREGROUND_BLUE + '                     █████▄    ▄███████████████████████████▌')
    print(FOREGROUND_BLUE + '                     ██████████████████████████████████████▌')
    print(FOREGROUND_BLUE + '                     ██████████████████████████████████████▌')
    print(FOREGROUND_BLUE + '                                        ███████████████████▌')
    print(FOREGROUND_BLUE + '         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄███████████████████▌' + FOREGROUND_YELLOW + '  ████████▄▄▄')
    print(FOREGROUND_BLUE + '      ▄████████████████████████████████████████████████████▌' + FOREGROUND_YELLOW + '  █████████████')
    print(FOREGROUND_BLUE + '    ███████████████████████████████████████████████████████▌' + FOREGROUND_YELLOW + '  ███████████████')
    print(FOREGROUND_BLUE + '  ▄████████████████████████████████████████████████████████▌' + FOREGROUND_YELLOW + '  ████████████████')
    print(FOREGROUND_BLUE + ' ▄█████████████████████████████████████████████████████████▌' + FOREGROUND_YELLOW + '  █████████████████')
    print(FOREGROUND_BLUE + ' ██████████████████████████████████████████████████████████' + FOREGROUND_YELLOW + '   █████████████████')
    print(FOREGROUND_BLUE + '▐█████████████████████████████████████████████████████████' + FOREGROUND_YELLOW + '   ▄██████████████████')
    print(FOREGROUND_BLUE + '████████████████████████████████████████████████████████' + FOREGROUND_YELLOW + '    ▄███████████████████')
    print(FOREGROUND_BLUE + '███████████████████████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀' + FOREGROUND_YELLOW + '      ▄█████████████████████')
    print(FOREGROUND_BLUE + '██████████████████████▀' + FOREGROUND_YELLOW + '                              ▄▄▄████████████████████████')
    print(FOREGROUND_BLUE + '████████████████████▀' + FOREGROUND_YELLOW + '    ▄▄█████████████████████████████████████████████████████')
    print(FOREGROUND_BLUE + '▀██████████████████' + FOREGROUND_YELLOW + '    █████████████████████████████████████████████████████████')
    print(FOREGROUND_BLUE + ' █████████████████▌' + FOREGROUND_YELLOW + '   █████████████████████████████████████████████████████████')
    print(FOREGROUND_BLUE + ' ▀████████████████' + FOREGROUND_YELLOW + '   ██████████████████████████████████████████████████████████')
    print(FOREGROUND_BLUE + '  ████████████████' + FOREGROUND_YELLOW + '   █████████████████████████████████████████████████████████')
    print(FOREGROUND_BLUE + '   ███████████████' + FOREGROUND_YELLOW + '   ███████████████████████████████████████████████████████')
    print(FOREGROUND_BLUE + '    ▀█████████████' + FOREGROUND_YELLOW + '   █████████████████████████████████████████████████████')
    print(FOREGROUND_BLUE + '      ▀▀██████████' + FOREGROUND_YELLOW + '   ████████████████████████████████████████████████▀▀▀')
    print(FOREGROUND_YELLOW + '                     ███████████████████')
    print(FOREGROUND_YELLOW + '                     ██████████████████████████████████████')
    print(FOREGROUND_YELLOW + '                     ██████████████████████████████████████')
    print(FOREGROUND_YELLOW + '                     ███████████████████████████▀    ▀█████')
    print(FOREGROUND_YELLOW + '                     ██████████████████████████▌      ▐████')
    print(FOREGROUND_YELLOW + '                     ███████████████████████████▄    ▄█████')
    print(FOREGROUND_YELLOW + '                      ▀███████████████████████████████████')
    print(FOREGROUND_YELLOW + '                        ▀███████████████████████████████▀')
    print(FOREGROUND_YELLOW + '                            ▀▀▀███████████████████▀▀▀')
    print(FOREGROUND_DARK_GRAY + '          Python is a programming language that lets you work quickly')
    print(FOREGROUND_DARK_GRAY + '                    and integrate systems more effectively.' + FOREGROUND_RESET)

if __name__ == '__main__':
  Program.main()
