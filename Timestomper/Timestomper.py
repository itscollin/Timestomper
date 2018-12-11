import datetime, dpkt, time, subprocess, argparse

#################################################################
# About TimeStomper:                                            #
# TimeStomper takes timestamps from old packet capture          #
# files and updates them to look like the capture ended at      #
# current time. Mainly to be used for training purposes when    #
# using tcpreplay w/ Kibana & Bro                               #
#################################################################

# Add argparse
parser = argparse.ArgumentParser(description=
'TimeStomper takes timestamps from old packet capture files and updates them to look like the capture ended at current time.' +
' Mainly to be used for training purposes when using tcpreplay w/ Kibana & Bro.')
parser.add_argument('file' , help='Pcap file to be edited')
parser.add_argument('-l', '--linux',  help='Dictates linux operating system',
            action='store_true')
parser.add_argument('-w', '--windows', help='Dictates windows operating system',
            action='store_true')
args = parser.parse_args()

originalTimestampList = []        # Original Timestamp

fileName = args.file

#Open pcap File
fileReader = open(fileName, 'rw')
capture = dpkt.pcap.Reader(fileReader)

no = datetime.datetime.now()      #Date time now.
now = time.mktime(no.timetuple()) #Sets date time to unix time

#Initial import of timestamps.
def originalTimestamp():
    #Appends original timestamps
    for ts, buf in capture:
        originalTimestampList.append(ts)

    quickMaths()

#Converts timestamps to current time.
def quickMaths():

    global secondsToAdd
    legnthOfList = len(originalTimestampList)    #Finds legnthOfList
    legnthOfList = legnthOfList - 1     #Last item in the list
    secondsToAdd = now - originalTimestampList[legnthOfList] #Seconds to add to Timestamps

    #Calls function to write new timestamps to file.
    writetofile()

def writetofile():

    # Timestamp Changes
    if args.linux == True:
        subprocess.check_output(['Linux_binary/editcap', '-t', str(secondsToAdd), fileName, 'updated.pcap'])

    elif args.windows == True:
        subprocess.check_output(['Windows_binary\\editcap.exe', '-t', str(secondsToAdd), fileName, 'updated.pcap'])

originalTimestamp()
