@echo off
set CUR_YYYY=%date:~10,4%
set CUR_MM=%date:~4,2%
set CUR_DD=%date:~7,2%
set CUR_HH=%time:~0,2%
if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)
set CUR_NN=%time:~3,2%
set CUR_SS=%time:~6,2%
set CUR_MS=%time:~9,2%
set foldername=%CUR_YYYY%%CUR_MM%%CUR_DD%%CUR_HH%%CUR_NN%

echo open 192.168.100.24>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo gisuser>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo gis!1234>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo ls>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo cd /usr/sap/trans/Interface/GIS >> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo mdel *.txt >> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo bye >> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

ftp -i -s:D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt >> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\LOGDELETE_FTP\deleteFile_%foldername%.txt

del D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpdelscript.txt

exit