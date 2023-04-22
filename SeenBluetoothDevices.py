DB_FILES = [
    'Library/Database/com.apple.MobileBluetooth.ledevices.other.db'
]
PLIST_FILES = [
    'Library/MobileBluetooth/com.apple.MobileBluetooth.ledevices.plist'
]

import files_parser as fp
from iOSbackup import iOSbackup

def getSeenBluetoothDevicesInfo(b: iOSbackup):
    fp.getDbFiles(b, DB_FILES, "SeenBluetoothDevices")