TimeStomper v.1.0
===========
---
Description
---
TimeStomper takes timestamps from old packet capture files and updates them to look like the capture ended at  current time. Mainly to be used for training purposes when using tcpreplay with Kibana.

Installation
--
TimeStomper requires a few python libraries:
* datetime
* dpkt
* time
* subprocess
* Wireshark is also needed for the 'editcap' command

A requirements.txt is included for use with pip, or they can be installed individually.

**`pip install -r requirements.txt `**

TimeStomper Usage
---
with v.1.0 TimeStomper is ran with
`python TimeStomper.py`.
The script will prompt you for an input PCAP file. A few notes:
* The input file should be an Absolute Path if not in the current directory

* If the file youre looking for is in the current directory, the file name will suffice.

* The file will automatically be named "updated.pcap" and put in the current directory.

