PLIST_FILES = ['Library/Preferences/com.apple.Maps.plist']

import fileParser as fp
from iOSbackup import iOSbackup

def getLastLocationInfo(b: iOSbackup):
    print("------- LAST LOCATION -------")
    fp.getPlistFiles(b, PLIST_FILES, "LastLocation")