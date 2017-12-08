import datetime, dpkt, time, subprocess

#################################################################
# About TimeStomper:                                            #
# TimeStomper takes timestamps from old packet capture          #
# files and updates them to look like the capture ended at      #
# current time. Mainly to be used for training purposes when    #
# using tcpreplay w/ Kibana                                     #
#################################################################

originalTimestampList = []        # Original Timestamp

fileName = raw_input('Input file: ')

#Open pcap File
fileReader = open(fileName, 'rw')
capture = dpkt.pcap.Reader(fileReader)

no = datetime.datetime.now()      #Date time now.
now = time.mktime(no.timetuple()) #Sets date time to unix time
print(now)

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
    print (originalTimestampList[legnthOfList])
    print(secondsToAdd)

    #Calls function to write new timestamps to file.
    writetofile()

def writetofile():

    subprocess.check_output(['editcap', '-t', str(secondsToAdd), fileName, 'updated.pcap'])


originalTimestamp()
