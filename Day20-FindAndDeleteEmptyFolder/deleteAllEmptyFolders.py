import os
import win32api
import numpy as np
selecteddir = ""
def ipfromuser():
    i = 1
    global selecteddir
    msg = "Folllowing drives are available to process:"
    drives = win32api.GetLogicalDriveStrings()
    dirName = np.array(drives.split('\000')[:-1])
    for eachd in dirName:
        msg = msg + " Enter "+ str(i) +" for " + eachd
        i += 1
    msg = msg + " ::"
    while True:
        ipt = int(input(msg))
        if ipt > 0 and (ipt <= i + 1):
            selecteddir = str(dirName[ipt - 1])
            break
        else:
            pass
    # return selecteddir        


def main():
    global selecteddir
    ipfromuser()
    
if __name__ == '__main__':
    main()