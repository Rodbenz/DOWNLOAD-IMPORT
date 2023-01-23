@echo off
set CUR_YYYY=%date:~10,4%
set CUR_MM=%date:~4,2%
set CUR_DD=%date:~7,2%
set CUR_HH=%time:~0,2%
if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)
set CUR_NN=%time:~3,2%
set CUR_SS=%time:~6,2%
set CUR_MS=%time:~9,2%
set foldername=%CUR_YYYY%%CUR_MM%%CUR_DD%%CUR_HH%%CUR_NN%%CUR_SS%
set mainFolder=%CUR_YYYY%%CUR_MM%%CUR_DD%%CUR_HH%%CUR_NN%%CUR_SS%


mkdir D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\DOWNLOADTEXTFILE\%mainFolder%\LOG
mkdir D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\DOWNLOADTEXTFILE\%mainFolder%\DOWNLOAD

echo START WORK %CUR_YYYY%-%CUR_MM%-%CUR_DD% %CUR_HH%:%CUR_NN%:%CUR_SS% >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo open 192.168.100.24>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo gisuser>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo gis!1234>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo ls>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo cd /usr/sap/trans/Interface/GIS>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo lcd D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\DOWNLOADTEXTFILE\%mainFolder%\DOWNLOAD >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo binary>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo prompt>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo mget *.txt>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

echo bye>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt

ftp -s:D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\DOWNLOADTEXTFILE\%mainFolder%\LOG\%foldername%_LOG_DOWNLOAD.txt

del D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpgetscript.txt 

@REM -------------------------------------------------------------DELETE--------------------------------------------------------------
echo START WORK %CUR_YYYY%-%CUR_MM%-%CUR_DD% %CUR_HH%:%CUR_NN%:%CUR_SS% >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

@REM echo open 192.168.100.25>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo open 192.168.100.24>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo gisuser>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo gis!1234>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo ls>> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo cd /usr/sap/trans/Interface/GIS >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo mdel *.txt >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

echo bye >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt

ftp -i -s:D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt >> D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\DOWNLOADTEXTFILE\%mainFolder%\LOG\%foldername%_LOG_DELETE.txt

del D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\ftpdelscript.txt
@REM ------------------------------------------------------------INSERT---------------------------------------------------------------
@REM start call "D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\DELETETXT.bat"

"C:/Users/Administrator/AppData/Local/Programs/Python/Python39/python.exe"  "D:/DOWNLOAD-IMPORT/MANUAL/PY_IMPORTTXT/ReadingFile.py"
@REM "C:/Users/SERVER/AppData/Local/Programs/Python/Python38/python.exe"  "D:/DOWNLOAD-IMPORT/MANUAL/PY_IMPORTTXT/ReadingFile.py"

"C:/Users/Administrator/AppData/Local/Programs/Python/Python39/python.exe"  "D:/DOWNLOAD-IMPORT/MANUAL/PY_IMPORTTXT/updateStatus.py"

@REM pause
exit

