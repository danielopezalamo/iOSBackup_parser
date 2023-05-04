PLIST_FILES = ['Library/Preferences/com.apple.Maps.plist']

import files_parser as fp
from iOSbackup import iOSbackup

def getLastLocationInfo(b: iOSbackup):
    fp.getPlistFiles(b, PLIST_FILES, "LastLocation")