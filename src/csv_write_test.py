import csv

"""
This program writes a string to a CSV file, 
"""

def writeToFile( aTwoDimensionList ):
    """
    Takes information given in a 2 dimentional list and writes the contents
    into a file.

    Inputs
    ------
    aTwoDimensionList: 
        
        A two dimension list. Similarly to this, it's like a list
        of lines you want to write to the file.

    Example Use of this function:

        Input:
               [["PersonID", "PersonFirstName", "PersonLastName"],
                ["001", "Frank", "Jones"],
                ["002", "Bobby", "Hill"]]

        Expected Output:
                (In the same directory, outputFile.csv is found)
                A CSV File with the first list as a header, and the following
                lists as "entries" listed underneath

    """
    with open("outputFile.csv", "wb") as csvfile:
        wr = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
        for aList in aTwoDimensionList:
            wr.writerow(aList)
    csvfile.close()


def main():
    # Testing Out The File Writing
    myList = [["Item 1", "Item 2", "Item 3"],
              ["Item 4", "Item 5", "Item 6"],
              ["Item 7", "Item 8", "Item 9"]]

    writeToFile(myList)

if __name__ == '__main__':
    main()