PLIST_FILES = [
    'Library/Preferences/com.apple.Preferences.plist'
]

import files_parser as fp
from iOSbackup import iOSbackup

def getDiskUsageInfo(b: iOSbackup):
    fp.getPlistFiles(b, PLIST_FILES, "DiskUsage")