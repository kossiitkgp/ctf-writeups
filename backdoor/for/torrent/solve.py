import zipfile
import pyshark
from binascii import unhexlify

display_filter = "bittorrent.continuous_data and ip.src == 10.0.0.1"
torrent = pyshark.FileCapture('./torrent.pcap', display_filter=display_filter)
result = []

print("processing pcap")
for index, packet in enumerate(torrent):
    print(f"processing packet no {index}")
    data = packet.bittorrent.continuous_data.replace(":", "")
    data = unhexlify(data)[13:]
    print(data[:20])
    if data not in result:
        result.append(data)

final = b"".join(result)
with open("flag.zip", "wb") as f:
    f.write(final)

with zipfile.PyZipFile("flag.zip", mode="r") as flag:
    flag.printdir()

torrent.close()
