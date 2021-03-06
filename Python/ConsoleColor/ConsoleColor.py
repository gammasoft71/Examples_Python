#!/usr/bin/env python3
# -*-coding:utf-8 -*

# @remarks To enable ANSI colors on Windows, add following key in the registry :
# [HKEY_CURRENT_USER\Console] "VirtualTerminalLevel"=dword:00000001

import sys

class Program:
  def main(self=None):
    LOGO = [
      U'████████████████████████████████████████████████████████████',
      U'██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████',
      U'██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████',
      U'██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░██████████',
      U'██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████████',
      U'██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████████',
      U'██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████████',
      U'███████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████',
      U'██████████████████████████████████████████████████████████████████████',
      U'██████████████████████████████████████████████████████████████████████',
      U'██████████████████████████▀▄▄▄▄▀███████▀▄▄▄▄▀█████████████████████████',
      U'███████████████████████████▀▀▀▀███████▀▀▀▀▀███████████████████████████',
      U'██████████████████████████      ▀████       ▀█████████████████████████',
      U'███████████             ▐         ▀▀         ▐              ██████████',
      U'█████████               ▐   ███   ▌▐   ███   ▐               █████████',
      U'█████████               ▐   █▄▄▌  ▌▐  ▐▄▄█   ▐               █████████',
      U'█████████                ▐▄  ▀▀ ▄▀  ▀▄ ▀▀  ▄▀                █████████',
      U'█████████                  ▀▀▄▄▀      ▀▀▄▄▀                  █████████',
      U'█████████                                                    █████████',
      U'█████████                 █▄                ▌                █████████',
      U'█████████                  ▌▀▀▄          ▄██                 █████████',
      U'█████████                  ▐   ▀▀▄▄▄▄▄▄█▀ █▌                 █████████',
      U'█████████                   ▐            ▄█                  █████████',
      U'█████████                    █          ▄█                   █████████',
      U'█████████                     ▀▄       █▀                    █████████',
      U'█████████                       ▀▄▄▄▄██▀                     █████████',
      U'█████████                                                    █████████',
      U'█████████                                                    █████████',
      U'█████████                                                    █████████',
      U'█████████                                                    █████████',
      U'█████████                                                    █████████',
      U'██████████████████████████████████████████████████████████████████',
    ]

    BACKGROUND_RESET = '\033[49m'
    BACKGROUND_WHITE = '\033[47m'
    FOREGROUND_DARK_GRAY = '\033[90m'
    FOREGROUND_DARK_BLUE = '\033[94m'
    FOREGROUND__RESET = '\033[39m'

    index = 0
    for line in LOGO:
      print('       ' if index == 0 or index == len(LOGO) - 1 else '     ', end='')
      print(FOREGROUND_DARK_BLUE, end='')
      print(BACKGROUND_WHITE, end='')
      print(line, end='')
      print(FOREGROUND__RESET, end='')
      print(BACKGROUND_RESET, end='')
      print('')
      index += 1
    
    print(FOREGROUND_DARK_BLUE, end='')
    print(U"                                    Gammasoft                                   ")
    print(FOREGROUND_DARK_GRAY, end='')
    print(U" More than thirty years of passion for high technology especially in development")
    print(U" (c++, c#, objective-c, ...).", end='')
    print(FOREGROUND__RESET)

if __name__ == '__main__':
  Program.main()

# This code produces the following output with colors:
#
#        ████████████████████████████████████████████████████████████
#      ██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████
#      ██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████
#      ██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░██████████
#      ██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████████
#      ██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████████
#      ██████████████████████████████░░░░░░░░░░░░░░░░░░░░░░████░░████████████
#      ███████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████
#      ██████████████████████████████████████████████████████████████████████
#      ██████████████████████████████████████████████████████████████████████
#      ██████████████████████████▀▄▄▄▄▀███████▀▄▄▄▄▀█████████████████████████
#      ███████████████████████████▀▀▀▀███████▀▀▀▀▀███████████████████████████
#      ██████████████████████████      ▀████       ▀█████████████████████████
#      ███████████             ▐         ▀▀         ▐              ██████████
#      █████████               ▐   ███   ▌▐   ███   ▐               █████████
#      █████████               ▐   █▄▄▌  ▌▐  ▐▄▄█   ▐               █████████
#      █████████                ▐▄  ▀▀ ▄▀  ▀▄ ▀▀  ▄▀                █████████
#      █████████                  ▀▀▄▄▀      ▀▀▄▄▀                  █████████
#      █████████                                                    █████████
#      █████████                 █▄                ▌                █████████
#      █████████                  ▌▀▀▄          ▄██                 █████████
#      █████████                  ▐   ▀▀▄▄▄▄▄▄█▀ █▌                 █████████
#      █████████                   ▐            ▄█                  █████████
#      █████████                    █          ▄█                   █████████
#      █████████                     ▀▄       █▀                    █████████
#      █████████                       ▀▄▄▄▄██▀                     █████████
#      █████████                                                    █████████
#      █████████                                                    █████████
#      █████████                                                    █████████
#      █████████                                                    █████████
#      █████████                                                    █████████
#        ██████████████████████████████████████████████████████████████████
#                                      Gammasoft
#      More than thirty years of passion for high technology especially in development
#      (c++, c#, objective-c, ...).
