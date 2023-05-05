import sqlite3
import pandas as pd
from iOSbackup import iOSbackup
from datetime import datetime
import plistlib, json, os

TIME_COLUMNS = [
    'DATE', 'TIMESTAMP', 'Time', 'timestamp', 'last_seen', 'time',
    'creation_date', 'last_update_date'
]

def databaseConnection(b: iOSbackup, file: str, module: str):
    # Get from file from backup
    file = b.getFileDecryptedCopy(relativePath=file, targetFolder='copied_files/%s' % module)
    # SQLite connection
    con = sqlite3.connect(file['decryptedFilePath'])
    return con.cursor()

def getTables(b: iOSbackup, file: str, module: str):
    cur = databaseConnection(b, file, module)
    res = cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
    tables = []
    for row in res:
        tables.append(row[0])
    return tables

""" def compare_convert_timestamps(df: pd.DataFrame):
    timestamps = df[['ZFIRSTTIMESTAMP', 'ZTIMESTAMP']]
    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix
    eq = []
    for i in range(0, timestamps.shape[0]):
        f_time = df.loc[i, ['ZFIRSTTIMESTAMP']].item()
        l_time = df.loc[i, ['ZTIMESTAMP']].item()
        if f_time == l_time:
            eq.append(1)
        else:
            eq.append(0)
        df.loc[i, ['ZFIRSTTIMESTAMP']] = [datetime.fromtimestamp(f_time) + delta]
        df.loc[i, ['ZTIMESTAMP']] = [datetime.fromtimestamp(l_time) + delta]
    df["ZEQUALTIMESTAMP"] = eq
    return df
 """

def convert_timestamps(df: pd.DataFrame, cols: list):
    convert_columns = []
    for col in cols:
        for t in TIME_COLUMNS:
            if t in col and col not in convert_columns:
                convert_columns.append(col)
    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix
    for i in range(0, df.shape[0]):
        for col in convert_columns:
            l_time = df.loc[i, [col]].item()
            if l_time and not pd.isna(l_time):
                df.loc[i, [col]] = [datetime.fromtimestamp(l_time) + delta]
    return df

def find_files(b: iOSbackup, files: list):
    all_files = b.getBackupFilesList()
    for f in files:
        found_files = list(filter(lambda x: f in x['name'], all_files))
        file_names = [f['name'] for f in found_files]
        return file_names

def getDbFiles(b:iOSbackup, db_files: list, module: str):
    for file in db_files:
        filename = file.split('/')[-1]
        cur = databaseConnection(b, file, module)
        for table in getTables(b, file, module):
            res = cur.execute("""SELECT * FROM %s;""" % table)
            names = [description[0] for description in cur.description]
            # Fetch all in a dataframe and convert to csv
            df = pd.DataFrame(res, columns=names)
            convert_timestamps(df, names)
            if not os.path.exists('csv/%s/%s' % (module, filename)):
                os.mkdir('csv/%s/%s' % (module, filename))
            df.to_csv('csv/%s/%s/%s.csv' % (module, filename, table), index=False)
        print('%s info saved...' % filename)

def getLogFiles(b: iOSbackup, log_files: list, module: str):
    for log_file in log_files:
        filename = log_file.split('/')[-1]
        b.getFolderDecryptedCopy(
            relativePath=log_file,
            targetFolder="copied_files/%s" % module
        )
        print('%s info saved...' % filename)

def getPlistFiles(b:iOSbackup, plist_files: list, module: str):
    for file in plist_files:
        filename = file.split('/')[-1]
        plist_file = b.getFileDecryptedCopy(
            relativePath=file,
            targetFolder="copied_files/%s" % module
        )
        with open(plist_file['decryptedFilePath'], 'rb') as f:
            data = plistlib.load(f)
        f.close()
        
        with open('csv/%s/%s.json' % (module, filename), 'w') as fp:
            json.dump(data, fp, default=str)
        fp.close()
        print('%s info saved...' % filename)
