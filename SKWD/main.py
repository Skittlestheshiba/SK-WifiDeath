#Written by Skittles_
import sys
from os import system, name
import deauth
import colors

#Current Version:
ver = '0.2'

def main():
    print(colors.blue(' ________________________\n|SK-WifiDeath ' + ver +'       |\n| Written By Skittles_  |\n|       ssssssss        |\n|    sss        sss     |\n| ss     sssss      ss  |\n|    ssss     ssss      |\n|         sss           |\n|          _            |\n|_________|S|___________|'))
    print('')
    print('')
    selectionFromMenu = input(colors.white('What would you like to do?\n'
      '1)Deauth a client\n2)Deauth an Access Point\nE)Exit WifiDeath\nSKWD>'))

    if selectionFromMenu == '1':
        system('clear')
        print('OK, Client Deauth.')
        deauth.wifiDeauthClient()
        mainMenu()

    elif selectionFromMenu == '2':
        print('OK, AP Deauth.')
        deauth.wifiDeauthAP()
        mainMenu()
    elif selectionFromMenu == 'E':
        sys.exit()
    else:
      if name == 'nt':
        system('cls')
      else:
        system('clear')
      mainMenu()

if __name__ == '__main__':
  main()
#Written by Skittles_
