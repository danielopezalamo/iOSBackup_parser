PLIST_FILES = [
    'Library/Preferences/com.apple.carplay.plist'
]

import files_parser as fp
from iOSbackup import iOSbackup

def getAppleCarInfo(b: iOSbackup):
    fp.getPlistFiles(b, PLIST_FILES, "AppleCar")