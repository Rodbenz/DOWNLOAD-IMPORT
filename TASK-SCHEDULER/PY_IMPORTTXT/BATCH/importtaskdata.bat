@echo off
@REM set CUR_YYYY=%date:~10,4%
@REM set CUR_MM=%date:~4,2%
@REM set CUR_DD=%date:~7,2%
@REM set CUR_HH=%time:~0,2%
@REM if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)
@REM set CUR_NN=%time:~3,2%
@REM set CUR_SS=%time:~6,2%
@REM set CUR_MS=%time:~9,2%
@REM set foldername=%CUR_YYYY%%CUR_MM%%CUR_DD%%CUR_HH%%CUR_NN%
@REM echo %foldername%

@REM mkdir D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\DOWNLOADTEXTFILE\download%foldername% 

@REM echo open 192.168.100.24>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo gisuser>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo gis!1234>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo ls>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo cd /usr/sap/trans/Interface/GIS>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo lcd D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\DOWNLOADTEXTFILE\download%foldername%>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo binary>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo prompt>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo mget *.txt>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM echo bye>> D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM ftp -s:D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt >>D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\LOGDOWNLOAD\downloadfille%foldername%.txt

@REM del D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\ftpgetscript.txt

@REM "C:/Users/Administrator/AppData/Local/Programs/Python/Python39/python.exe"  "D:/DOWNLOAD-IMPORT/TASK-SCHEDULER/PY_IMPORTTXT/ReadingFile.py"
"C:\Users\SERVER\AppData\Local\Programs\Python\Python38\python.exe"  "D:/DOWNLOAD-IMPORT/TASK-SCHEDULER/PY_IMPORTTXT/ReadingFile.py"

@REM start call "D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\BATCH\daleteTxt.bat"

exit
