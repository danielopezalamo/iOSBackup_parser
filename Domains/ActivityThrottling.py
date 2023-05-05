PLIST_FILES = ['Library/Preferences/com.apple.coreduetd.plist', 'Library/Preferences/com.apple.contextstored.plist']

import fileParser as fp
from iOSbackup import iOSbackup

def getActivityThrottlingInfo(b: iOSbackup):
    print("------- ACTIVITY THROTTLING -------")
    fp.getPlistFiles(b, PLIST_FILES, "ActivityThrottling")