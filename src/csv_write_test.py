import csv

"""
This program writes a string to a CSV file, 
"""

def writeToFile( aTwoDimensionList ):
    with open("examplefile.csv", "wb") as csvfile:
        wr = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
        for aList in aTwoDimensionList:
            wr.writerow(aList)
    csvfile.close()

        #wr.writerow(['Item 1', 'Item 2', 'Item 3'])
        #wr.writerow(['Item 1', 'Item 2', 'Item 3'])


def main():
    myList = [["Item 1", "Item 2", "Item 3"],
              ["Item 4", "Item 5", "Item 6"],
              ["Item 7", "Item 8", "Item 9"]]

    writeToFile(myList)

if __name__ == '__main__':
    main()