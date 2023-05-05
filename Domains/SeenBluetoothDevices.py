DB_FILES = [
    'Library/Database/com.apple.MobileBluetooth.ledevices.other.db'
]
PLIST_FILES = [
    'Library/MobileBluetooth/com.apple.MobileBluetooth.ledevices.plist'
]

import fileParser as fp
from iOSbackup import iOSbackup

def getSeenBluetoothDevicesInfo(b: iOSbackup):
    print("------- SEEN BLUETOOTH DEVICES -------")
    fp.getDbFiles(b, DB_FILES, "SeenBluetoothDevices")