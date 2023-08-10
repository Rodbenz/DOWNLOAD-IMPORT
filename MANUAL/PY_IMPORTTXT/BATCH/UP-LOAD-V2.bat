@echo off
echo open 192.168.100.24>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

echo gisuser>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

echo gis!1234>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

echo ls>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

echo cd /usr/sap/trans/Interface/GIS >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

echo lcd D:\DOWNLOAD-IMPORT\BACKUP\UPLOAD-V2 >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

echo mput *.txt >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

echo bye >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

ftp -i -s:D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt

del D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpuploadscript.txt
pause