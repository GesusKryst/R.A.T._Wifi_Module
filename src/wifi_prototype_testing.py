#!/usr/bin/env python
"""
This is a module dedicated to providing router identification by scanning
surrouding routers. 
"""

# Imports
import iw_parse as working_interface
import csv
import time as time
import getmac




###########################
########## Info ###########
###########################
__author__ = "George Cadel-Munoz"
__credits__ = ["George Cadel-Munoz"]
__version__ = "0.8"
__maintainer__ = "George Cadel-Munoz"
__email__ = "gec68@nau.edu"
__status__ = "Prototype"



def displayReq(an_interface_list):
    """
    Displays all scanned connections and routers in currently
    scanned list. 
    Separators added for readability.
    """
    #print "Length of interface list: {}".format(len(an_interface_list))
    returnStr = ""
    for router in an_interface_list:
        print "\n================="
        for cell in router:
            if (cell == "Frequency" or cell == "Signal Level" or
                cell == "Name" or cell == "Channel" or cell == "Address"):
                print "{}: {}".format(cell, router[cell])
                returnStr = returnStr + router[cell] + ","
            #print "{}: {}".format(cell, router[cell])
        print "================\n"
    return returnStr

def displayAll(an_interface_list):
    """
    Displays all scanned connections and routers in currently
    scanned list. 
    Separators added for readability.
    """
    #print "Length of interface list: {}".format(len(an_interface_list))
    returnStr = ""
    for router in an_interface_list:
        print "\n================="
        for cell in router:
            #if cell == "Address"
            print "{}: {}".format(cell, router[cell])
            returnStr = returnStr + router[cell] + ","
            #print "{}: {}".format(cell, router[cell])
        print "================\n"
    return returnStr


def stringToList(a_list_of_strings, max_list_size):
    working_list = a_list_of_strings.split(",")
    working_list.pop()
    inner_list = []
    final_list = []
    while (len(working_list) > 0):
        while(len(inner_list) < max_list_size):
            #inner_list.append(" ")
            inner_list.append(working_list[0])
            working_list.pop(0)
        final_list.append(inner_list)
        inner_list = []
    return final_list


def writeToFile( aTwoDimensionList, filePath, headerFlag ):
    with open(filePath, "wb") as csvfile:
        wr = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
        if(headerFlag):
            wr.writerow(["Frequency", "Name", "Signal Level", "Address", "Channel"])
        for aList in aTwoDimensionList:
            wr.writerow(aList)
    csvfile.close()


def getCSV():
    ### Constants ###
    interface = 'wlp2s0' # Network scanning device
    running_iter = 1 # Starting scan iteraction counter
    total_iter = 1 # Total scan interations
    refresh_rate = 1 # Delay between each scan in seconds
    minimum_router_list = 3 # The minimum amount of routers scanned
    interface_list = [] # Initial list of the interface list
    raw_string_list = [] # List of string lists
    default_list_length = 5 # Capture 4 items in the raw string list
    default_file_path = "/home/george/Documents/Schoolio/Senior_Sem_2/CS486/Stuffs/R.A.T._Wifi_Module/src/routerlist.csv"
    default_csv_header_flag = True # Will add a header to the CSV file if true


    # To compare results to information obtained from the 
    # computer itself, run the following command in the 
    # terminal:
    #     watch -n1 iwconfig
    while(running_iter <= total_iter ):
        # Collect connected router information
        # Show current iteration
        while(len(interface_list) < minimum_router_list):
            print "Length of interface list: {}".format(len(interface_list))
            interface_list = working_interface.call_iwlist(interface).split()
            print "Length of interface list: {}".format(len(interface_list))
        # Pretty printing
        print "\n\n><><><><><><><><><><><><><><><"
        print "><><><>< Iteration {}  ><><><><".format(running_iter)
        print "><><><><><><><><><><><><><><><\n"
        new_list = working_interface.get_interfaces(interface)

        # Display All Routers
        rawDataString = displayReq(new_list)
        finalList = stringToList(rawDataString, default_list_length)

        # Write info to CSV file
        writeToFile(finalList, default_file_path, default_csv_header_flag)

        #printInterfaceList(interface_list)
        #displayImportant(interface_list)

        #for index, item in enumerate(interface_list):
            # Format data into strings for readability
         #   item = item.decode("utf-8")
            #print("Index: ", index, "Item: ", item)
        time.sleep(refresh_rate)
        #isSimilarLen(new_list)
        running_iter += 1
        
        
    
    
    print "\n\nScanning terminated...\n\n" 

getCSV()


#if __name__ == "__main__":
    #main()