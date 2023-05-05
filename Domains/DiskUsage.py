PLIST_FILES = [
    'Library/Preferences/com.apple.Preferences.plist'
]

import fileParser as fp
from iOSbackup import iOSbackup

def getDiskUsageInfo(b: iOSbackup):
    print("------- DISK USAGE -------")
    fp.getPlistFiles(b, PLIST_FILES, "DiskUsage")