#Written by Skittles_
import sys
from os import system, name
import deauth
import colors
ver = '0.3'


def mainMenu():
    print(colors.blue(' ________________________\n|SK-WifiDeath ' + ver +'       |\n| Written By Skittles_  |\n|       ssssssss        |\n|    sss        sss     |\n| ss     sssss      ss  |\n|    ssss     ssss      |\n|         sss           |\n|          _            |\n|_________|S|___________|'))
    print('')
    print('')
    selectionFromMenu = input(colors.white('What would you like to do?\n'
      '1)Deauth a client\n2)Deauth an Access Point\nE)Exit WifiDeath\n>'))

    if selectionFromMenu == '1':
      if name == 'nt':
        system('cls')
      else:
        system('clear')
        print('OK, Client Deauth.')
        deauth.wifiDeauthClient()
    elif selectionFromMenu == '2':
      if name == 'nt':
        system('cls')
      else:
        system('clear')
        print('OK, AP Deauth.')
        deauth.wifiDeauthAP()
    elif selectionFromMenu == 'E':
        sys.exit()
    else:
      if name == 'nt':
        system('cls')
      else:
        system('clear')
      mainMenu()


mainMenu()
