from iOSbackup import iOSbackup
import pandas as pd
import os

def getMediaFolderInfo(b: iOSbackup):
    print("------- MEDIA -------")
    files = b.getFolderDecryptedCopy(
        'Media/DCIM',
        targetFolder='copied_files/Media'
    )
    media = []
    for subdir, dirs, files in os.walk('copied_files/Media/CameraRollDomain/Media/DCIM'):
        for file in files:
            dir = os.path.join(subdir, file).replace('\\', '/').split('/')[-4:]
            media.append('/'.join(e for e in dir))
    created = []
    last_modified = []
    for file in media:
        file_info = b.getRelativePathDecryptedData(file)
        created.append(file_info[0]['created'].strftime("%d/%m/%Y"))
        last_modified.append(file_info[0]['lastModified'].strftime("%d/%m/%Y"))
    df = pd.DataFrame(
        list(zip(media, created, last_modified)),
        columns =['media', 'created', 'last_modified']
    )
    df.to_csv('parsed_data/Media/media.csv')
    return print("Media info saved...")

