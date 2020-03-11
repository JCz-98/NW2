#This code is based on https://null-byte.wonderhowto.com/how-to/build-arp-scanner-using-scapy-and-python-0162731/
import sys
import time
from datetime import datetime
from scapy.all import srp, Ether, ARP, conf

lastname_1 = 'NAUNAY'
lastname_2 = 'CAZCO'
delimiter = '_'
scanMode_1 = 'LAN'
scanMode_2 = 'WLAN'
extension = '.txt'

if __name__ == "__main__":

    try:
        interface = input("Enter desired interface: ")
        ips = input("Enter range of IPs to Scan for: ")
        mode = input("Connection (1.WiFi 2.Lan): ")
        timeout_max = int(input("Enter desire timeout (15,30,60):"))

    except KeyboardInterrupt:
        print ("\n User requested shutdown")
        print ("Quiting...")
        sys.exit(1)

    print ("\n Scanning... ")

    timeStamp = time.time()
    strTimeStamp = datetime.fromtimestamp(timeStamp).strftime('%Y.%m.%d.%H.%M.%S')

    start_time = datetime.now()

    fd = open(lastname_2+delimiter+lastname_1+delimiter+scanMode_1+delimiter+strTimeStamp+extension, 'w')

    if mode == '1':
        title = lastname_2+delimiter+lastname_1+delimiter+scanMode_2+delimiter+strTimeStamp+extension
    else:
        title = lastname_2+delimiter+lastname_1+delimiter+scanMode_1+delimiter+strTimeStamp+extension

    fd.write("<{}>\n".format(title))
    fd.write(ips + "\n")

    conf.verb = 0
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ips), timeout=timeout_max, iface=interface, verbose=False)

    #print ans.summary()
    print ('MAC - IP')
    for s, r in ans:
        #print (r.sprintf(r'%Ether.src% %ARP.psrc%'))
        line = "{}\t{}".format(r.sprintf(r'%Ether.hwsrc%'), r.sprintf(r'%ARP.psrc%'))
        fd.write(line + "\n")
        print(line)

    stop_time = datetime.now()
    total_time = stop_time - start_time

    print ("\n Scan Complete!")
    print ("Scan Duration: %s" %(total_time))

