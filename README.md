# iOSBackup_parser
This is an iOSBackup parser that extracts information about the usage of a device and allows you to collect the most useful data for logging and visualising device activity.

## Dependencies

pip install -r requirements.txt

## Usage

### Get list of backups available on your computer
```python
>>> from iOSbackup import iOSbackup
>>> iOSbackup.getDeviceList()
[{
  'udid': '0008020-001650623A79002E',
  'name': 'iPhone de XXXX', 
  'ios': '16.1.1', 
  'serial': 'XXXXXXXXXX', 
  'type': 'iPhone11,8', 
  'encrypted': True, 
  'passcodeSet': True, 
  'date': datetime.datetime(2023, 2, 18, 14, 53, 36, 291249,
  tzinfo=datetime.timezone.utc
 )}]
```

### Open a device backup, in the iOSBackup.py file:

With your password (a slow and compute-intensive task):
```python
>>> b=iOSbackup(
	udid="0008020-001650623A79002E",
	cleartextpassword="mypassword"
)
```
Instead of a clear text password, use a derived key that can be seen into the instantiated object:
```python
>>> b=iOSbackup(
	udid="0008020-001650623A79002E",
	cleartextpassword="mypassword"
)
>>> print(b)
…
decryptionKey: dd6b6123494c5dbdff7804321fe43ffe1babcdb6074014afedc7cb47f351524
…
```
Now we can put the derivedKey in the iOSBackup.py file:
```
  b=iOSbackup(
	udid="0008020-001650623A79002E",
	derivedkey="dd6b6123494c5dbdff7804321fe43ffe1babcdb6074014afedc7cb47f351524"
)
```

Now execute the script to parse the data and generate the .csv files.

