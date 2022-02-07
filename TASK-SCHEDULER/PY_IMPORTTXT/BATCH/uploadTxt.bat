@echo off
echo open 192.168.100.24>> D:\py_importTxt\ftpuploadscript.txt

echo gisuser>> D:\py_importTxt\ftpuploadscript.txt

echo gis!1234>> D:\py_importTxt\ftpuploadscript.txt

echo ls>> D:\py_importTxt\ftpuploadscript.txt

echo cd /usr/sap/trans/Interface/GIS >> D:\py_importTxt\ftpuploadscript.txt

echo lcd D:\py_importTxt\DownloadTextFile\download202202015353 >> D:\py_importTxt\ftpuploadscript.txt

echo mput *.txt >> D:\py_importTxt\ftpuploadscript.txt

echo bye >> D:\py_importTxt\ftpuploadscript.txt

ftp -i -s:D:\py_importTxt\ftpuploadscript.txt

del D:\py_importTxt\ftpuploadscript.txt
pause