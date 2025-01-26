# No Shark

Points: 50

> Where's baby shark at?

`Author: skat`

---

We were given the text in `noshark.txt`. At first sight it feels
obvious that these are raw packets. We just have to interpret them. Now
I didn't know enough about networks to properly read the packets, so I
asked chatgpt for help. From there I extracted the data packets which
turned out to be an image that gave us the flag.

However I would now like to actually understand the packets in depth.

I found [this](https://www.cs.ait.ac.th/~on/O/oreilly/tcpip/firewall/ch06_03.htm)
fantastic read that really breaks down the structure of a packet. 

Packets are constructed in such a way that layers in each protocol are wrapped around
each other. So our first layer would be the **Network Access Layer** or the 
**Ethernet** Layer. 

## Network Access Layer
| Field Name           | Size         | Description                               |
|----------------------|--------------|-------------------------------------------|
| Destination MAC      | 6 bytes      | The MAC address of the frame's recipient.|
| Source MAC           | 6 bytes      | The MAC address of the frame's sender.   |
| **EtherType**        | 2 bytes      | Indicates the type of payload.           |
| Payload              | Variable     | Contains the encapsulated protocol data. |
| Frame Check Sequence | 4 bytes      | Ensures data integrity.                  |

as we can see our type is `0800` which says the internal packet is an `IPv4` packet

| EtherType | Protocol            | Description                                  |
|-----------|---------------------|----------------------------------------------|
| `0800`    | IPv4                | Internet Protocol version 4                 |
| `0806`    | ARP                 | Address Resolution Protocol                 |
| `86DD`    | IPv6                | Internet Protocol version 6                 |
| `8847`    | MPLS                | Multiprotocol Label Switching (unicast)     |
| `8100`    | VLAN-tagged frame   | Indicates a VLAN-tagged frame (802.1Q)      |

`0000000000000000000000000800` so our packet breaks into

| Destination | Source | Type/Length | Data | CRC32 |
| ---      | ---         | ---    | ---         | ---  |
| 0000 0000 0000 0000 | 0000 0000 0000 0000 | 0800 | - | -

After the Network Acess Layer we have the Internet Layer which as we know from
the type above is **IPv4**

## Internet Layer
| Field Name           | Size         |
|----------------------|--------------|
| Version              | 4 bits       |
| HLEN                 | 4 bits       |
| Type of Service      | 1 byte       |
| Total Length         | 2 bytes      |
| Identification       | 2 bytes      |
| Flags                | 3 bits       |
| Fragment Offset      | 13 bits      |
| Time to Live         | 2 bytes      |
| Protocol             | 1 byte       |
| Header Checksum      | 2 bytes      |
| Source IP            | 4 byte       |
| Destination IP       | 4 byte       |
| Options              | 0-40 bytes   |
| Data                 |              |

`4500  003c  7d15  4000 4006  bfa4  7f000001  7f000001`

The **Protocol** byte is `06` which means that the next packet is TCP
| Protocol Number | Protocol Name          | Description                           |
|-----------------|------------------------|---------------------------------------|
| `01`            | ICMP                   | Internet Control Message Protocol     |
| `02`            | IGMP                   | Internet Group Management Protocol    |
| `06`            | TCP                    | Transmission Control Protocol         |
| `11`            | UDP                    | User Datagram Protocol                |
| `29`            | IPv6-Route             | Routing Header for IPv6               |
| `84`            | SCTP                   | Stream Control Transmission Protocol  |

The full list can be found in [IANA's Protocol Numbers registry](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

## Transport Layer

```
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Source Port          |       Destination Port        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        Sequence Number                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Acknowledgment Number                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Data |       |C|E|U|A|P|R|S|F|                               |
   | Offset| Rsrvd |W|C|R|C|S|S|Y|I|            Window             |
   |       |       |R|E|G|K|H|T|N|N|                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Checksum            |         Urgent Pointer        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                           [Options]                           |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                                                               :
   :                             Data                              :
   :                                                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

First we have the **TCP Header**. The data offset and flags are usually the most important.
We also have some options. 

However in the end the main thing we want is the data, which we can extract with the
very simple `solve.py` to get the image

![flag](./image.jpg)

---

```sh
irisctf{welcome_to_net_its_still_ez_to_read_caps_without_wireshark}
```
