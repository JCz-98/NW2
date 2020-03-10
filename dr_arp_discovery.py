#This code is based on https://null-byte.wonderhowto.com/how-to/build-arp-scanner-using-scapy-and-python-0162731/
import sys
from datetime import datetime
from scapy.all import srp, Ether, ARP, conf


if __name__ == "__main__":

    f_ad = open("data/addresses.txt", "w+")

    timestamp = "<CAZCO_ÑAUÑAY_WLAN_2020.03.08.04.46.59.txt>\n"

    try:
        interface = input("Enter desired interface: ")
        ips = input("Enter range of IPs to Scan for: ")

    except KeyboardInterrupt:
        print ("\n User requested shutdown")
        print ("Quiting...")
        sys.exit(1)

    f_ad.write(timestamp)
    f_ad.write(ips)
    f_ad.write("\n")

    print ("\n Scanning... ")
    start_time = datetime.now()
    print(start_time)

    conf.verb = 0
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ips), timeout=30, iface=interface, verbose=False)

    print(ans.summary())
    print ('MAC - IP')
    for s, r in ans:
        print(r.sprintf(r'%Ether.src% -- %ARP.psrc%'))
        f_ad.write(r.sprintf(r'%Ether.src% -- %ARP.psrc%'))
        f_ad.writelines("\n")


    stop_time = datetime.now()
    total_time = stop_time - start_time
    f_ad.close()


    print ("\n Scan Complete!")
    print ("Scan Duration: %s" %(total_time))
