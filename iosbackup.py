from iOSbackup import iOSbackup
import SeenBluetoothDevices, ActivityThrottling, Media, DiskUsage, AppleCar,\
SafariHistory, ApplicationTraces, Siri, NetworkStatistics, convert_cpbitmap, \
Keyboard, LastLocation, CallHistory

import json

def find_file(b: iOSbackup, name: str):
    files = b.getBackupFilesList()
    my_file = list(filter(lambda x: name in x['name'], files))
    print(my_file)
    #with open('output.json', 'w') as fp:
    #    json.dump(my_file, fp, default=str)
    #for file in my_file:
    #    b.getFileDecryptedCopy(relativePath=file['name'], targetFolder='copied_files')

b = iOSbackup(udid="00008020-001650623A79002E", derivedkey="6a606ae61c7ac05307f91d530454c8f67cc3b8bfdd9d5f8dbc2cd3bd1322c26d")
#find_file(b, 'Library/CallHistoryDB/CallHistoryTemp.storedata')
print('Backup Opened!')

#SafariHistory.getTablesInfo(b)
#ActivityThrottling.getActivityThrottlingInfo(b)
ApplicationTraces.getApplicationTracesInfo(b)
#SeenBluetoothDevices.getSeenBluetoothDevicesInfo(b)
#Siri.getSiriInfo(b)
#SafariHistory.getSafariHistoryInfo(b)
#NetworkStatistics.getNetworkStatisticsInfo(b)
#convert_cpbitmap.convert('copied_files\HomeDomain~Library--SpringBoard--LockBackground.cpbitmap')
#DiskUsage.getDiskUsageInfo(b)
#AppleCar.getAppleCarInfo(b)
#Media.getMediaFolderInfo(b)
#Keyboard.getKeyboardInfo(b)
#LastLocation.getLastLocationInfo(b)
#CallHistory.getCallHistoryInfo(b)








