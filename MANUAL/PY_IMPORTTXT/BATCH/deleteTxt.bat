@echo off
echo open 192.168.100.24>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo gisuser>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo gis!1234>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo ls>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo cd /usr/sap/trans/Interface/GIS >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo mdel *.txt >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo bye >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

ftp -i -s:D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

del D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt
pause