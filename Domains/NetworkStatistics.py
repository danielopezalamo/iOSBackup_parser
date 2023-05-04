PLIST_FILES = [
    'Library/Preferences/com.apple.CommCenter.counts.plist'
]

import files_parser as fp
from iOSbackup import iOSbackup

def getNetworkStatisticsInfo(b: iOSbackup):
    fp.getPlistFiles(b, PLIST_FILES, "NetworkStatistics")