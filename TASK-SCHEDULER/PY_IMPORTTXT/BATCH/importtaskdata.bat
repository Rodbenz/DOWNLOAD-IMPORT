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
@REM echo %foldername%

mkdir D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\DOWNLOADTEXTFILE\download%foldername% 

echo open 192.168.100.24>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo gisuser>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo gis!1234>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo ls>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo cd /usr/sap/trans/Interface/GIS>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo lcd D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\DOWNLOADTEXTFILE\download%foldername%>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo binary>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo prompt>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo mget *.txt>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo bye>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

ftp -s:D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt >>D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\LOGDOWNLOAD\downloadFile_%foldername%.txt

del D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

start call "D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\deleteTxt.bat"

"C:/Users/Administrator/AppData/Local/Programs/Python/Python39/python.exe"  "D:/DOWNLOAD-IMPORT/TASK-SCHEDULER/PY_IMPORTTXT/ReadingFile.py"
@REM "C:\Users\SERVER\AppData\Local\Programs\Python\Python38\python.exe"  "D:/DOWNLOAD-IMPORT/TASK-SCHEDULER/PY_IMPORTTXT/ReadingFile.py"

@REM start call "D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\daleteTxt.bat"

exit
