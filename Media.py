from iOSbackup import iOSbackup

def getMediaFolderInfo(b: iOSbackup):
    b.getFolderDecryptedCopy(
        'Library/Keyboard',
        targetFolder='copied_files/find'
    )

def test(b: iOSbackup):
    files = b.getBackupFilesList()
    my_file = list(filter(lambda x: '9009.JPG' in x['name'], files))
    for file in my_file:
        print(file['file'].decode('utf-8'))
