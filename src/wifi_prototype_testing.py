#!/usr/bin/env python
"""
This is a module dedicated to providing router identification by scanning
surrouding routers. 
"""

# Imports
import iw_parse as working_interface
import time as time




###########################
########## Info ###########
###########################
__author__ = "George Cadel-Munoz"
__credits__ = ["George Cadel-Munoz"]
__version__ = "0.1"
__maintainer__ = "George Cadel-Munoz"
__email__ = "gec68@nau.edu"
__status__ = "Prototype"


def printInterfaceList(an_interface_list):
    """
    Decode a list of byte arrays into readable
    strings and display to user
    """
    #for item in range(len(an_interface_list)):
    for item in an_interface_list: 
        print item.decode("utf-8")


def isSimilarLen(an_interface_list):
    length_of_list = len(an_interface_list)
    print "List length: ", length_of_list


def displayImportant(an_interface_list):
    """
    Allows for easier viewing of the router address,
    channel, frequency, link quality (of 70), and signal level
    """
    important_categories = ["Address",
                            "Channel",
                            "Frequency",
                            "Quality",
                            "Signal"]


def main():
    ### Constants ###
    interface = 'wlp2s0' # Network scanning device
    running_iter = 1 # Starting scan iteraction counter
    total_iter = 20 # Total scan interations
    refresh_rate = 4 # Delay between each scan in seconds
    #interface_list = (iw_parse.call_iwlist(interface)).split()
    
    # To compare results to information obtained from the 
    # computer itself, run the following command in the 
    # terminal:
    #     watch -n1 iwconfig

    while(running_iter <= total_iter ):
        # Collect connected router information
        # Show current iteration
        interface_list = working_interface.call_iwlist(interface).split()

        # Pretty printing
        print "\n\n><><><><><><><><><><><><><><><"
        print "><><><>< Iteration {}  ><><><><".format(running_iter)
        print "><><><><><><><><><><><><><><><\n"
        new_list = working_interface.get_interfaces(interface)
        
        # Router info cells in the first item in the list
        router_info = new_list[0]
        for cell in router_info:
            print "{}: {}".format(cell, router_info[cell])
        
        
        #printInterfaceList(interface_list)
        #displayImportant(interface_list)

        #for index, item in enumerate(interface_list):
            # Format data into strings for readability
         #   item = item.decode("utf-8")
            #print("Index: ", index, "Item: ", item)
        time.sleep(refresh_rate)
        isSimilarLen(new_list)
        running_iter += 1
    print "\n\nScanning terminated...\n\n" 


if __name__ == "__main__":
    main()