from iOSbackup import iOSbackup
from Domains import SeenBluetoothDevices, ActivityThrottling, Media, DiskUsage, AppleCar,\
SafariHistory, ApplicationTraces, Siri, NetworkStatistics, \
Keyboard, LastLocation, CallHistory

import json

def find_file(b: iOSbackup, name: str):
    files = b.getFolderDecryptedCopy(
        'Media/DCIM',
        targetFolder='copied_files/find'
    )
    my_file = list(filter(lambda x: name in x['name'], files))
    print(my_file)

# Introduce your backup serial id and you cleartext/derived key
b = iOSbackup(udid="00008020-001650623A79002E", derivedkey="6a606ae61c7ac05307f91d530454c8f67cc3b8bfdd9d5f8dbc2cd3bd1322c26d")
print('Backup Opened!')

#find_file(b, 'Media/DCIM')

# Data extraction and parsing
SafariHistory.getSafariHistoryInfo(b)
ActivityThrottling.getActivityThrottlingInfo(b)
ApplicationTraces.getApplicationTracesInfo(b)
SeenBluetoothDevices.getSeenBluetoothDevicesInfo(b)
Siri.getSiriInfo(b)
SafariHistory.getSafariHistoryInfo(b)
NetworkStatistics.getNetworkStatisticsInfo(b)
DiskUsage.getDiskUsageInfo(b)
AppleCar.getAppleCarInfo(b)
Media.getMediaFolderInfo(b)
Keyboard.getKeyboardInfo(b)
LastLocation.getLastLocationInfo(b)
CallHistory.getCallHistoryInfo(b)








