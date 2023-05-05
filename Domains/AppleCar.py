PLIST_FILES = [
    'Library/Preferences/com.apple.carplay.plist'
]

import fileParser as fp
from iOSbackup import iOSbackup

def getAppleCarInfo(b: iOSbackup):
    print("------- APPLE CAR -------")
    fp.getPlistFiles(b, PLIST_FILES, "AppleCar")