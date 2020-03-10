import plotly.express as px
from mac_vendor_lookup import MacLookup
import os
import pandas as pd

path = "./data"
files = os.listdir(path)

mac_set = set()
vendors_dict = {}

for file_name in files:
    print(file_name)

    f_ad = open(path + "/" + file_name, "r")

    f_lines = f_ad.read().splitlines()
    # print(f_lines)
    f_ad.close()

    timestamp = f_lines[0]
    ipRange = f_lines[1]
    mac_ip = []

    for i in range(2, len(f_lines)):
        mac_ip.append(f_lines[i])
        # print(f_lines[i])

    # print(mac_ip)

    macsplit = []

    for dataline in mac_ip:
        macsplit.append(dataline.split())

    # print(macsplit)

    mac_addresses = []
    ips = []

    for data_tuple in macsplit:
        mac_addresses.append(data_tuple[0])
        mac_set.add(data_tuple[0])
        ips.append(data_tuple[1])

# identify mac
macad = MacLookup()
macad.load_vendors()

for mac_address in mac_set:
    mac_vendor = macad.lookup(mac_address)
    print(mac_address, " --> ", mac_vendor)
    if mac_vendor in vendors_dict:
        vendors_dict[mac_vendor] = vendors_dict[mac_vendor] + 1
    else:
        vendors_dict[mac_vendor] = 1

print(vendors_dict)

# vendors_dict['Hewlett Packard'] = 5
vendors = []
freq = []
for k,v in vendors_dict.items():
    vendors.append(k)
    freq.append(v)

# print(vendors)
# print(freq)

wide_df = pd.DataFrame(dict(Vendor=vendors, Dispositivos=freq))
tidy_df = wide_df.melt(id_vars="Vendor")
print(tidy_df)


mac_bar = px.bar(tidy_df, x="Vendor", y="value", color='variable')
mac_pie = px.pie(tidy_df, values="value", names="Vendor")
mac_bar.show()
mac_pie.show()