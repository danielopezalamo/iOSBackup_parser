PLIST_FILES = [
    'Library/Preferences/com.apple.CommCenter.counts.plist'
]

import fileParser as fp
from iOSbackup import iOSbackup

def getNetworkStatisticsInfo(b: iOSbackup):
    print("------- NETWORK STATISTICS -------")
    fp.getPlistFiles(b, PLIST_FILES, "NetworkStatistics")