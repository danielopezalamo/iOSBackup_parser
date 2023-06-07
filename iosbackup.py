from pathlib import Path
import sys, os, _winapi, json
from iOSbackup import iOSbackup
from domains import SeenBluetoothDevices, ActivityThrottling, Media, DiskUsage, AppleCar,\
SafariHistory, ApplicationTraces, Siri, NetworkStatistics, \
Keyboard, LastLocation, CallHistory

def link_backup():
    src_name = Path(r"%s" % sys.argv[1]).name
    if not os.path.exists(r"C:\Users\%s\AppData\Roaming\Apple Computer\MobileSync\Backup\%s" % (sys.argv[4], src_name)):
        src_dir = sys.argv[3]
        dst_dir = "C:/Users/Daniel/AppData/Roaming/Apple Computer/MobileSync/Backup/%s" % src_name
        src_dir = os.path.normpath(os.path.realpath(src_dir))
        dst_dir = os.path.normpath(os.path.realpath(dst_dir))
        _winapi.CreateJunction(src_dir, dst_dir)

def find_file(b: iOSbackup, name: str):
    files = b.getFolderDecryptedCopy(
        'Media/DCIM',
        targetFolder='copied_files/find'
    )
    my_file = list(filter(lambda x: name in x['name'], files))
    print(my_file)

def main():
    # If backup has been imported manually, a symlink is created.
    if sys.argv[3]:
        link_backup()
    
    # Backup Opening with udid and derivedKey
    try:
        b = iOSbackup(udid="%s" % sys.argv[1], derivedkey="%s" %sys.argv[2])
        print('Backup Opened!')
    except ValueError:
        print("Something went wrong... Please check all the inserted parameters!")

    #find_file(b, 'Media/DCIM')

if __name__ == "__main__":
    main()