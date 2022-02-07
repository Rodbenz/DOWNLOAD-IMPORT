import os
from config.sql_server_conn import sql_conn
import requests
import  threading

def getQueName() : 
    # sqlConn = sql_conn("SELECT STATUS FROM EXAT_GIS_TEST.dbo.INSERSAP_STATUS WHERE STATUS_SEQ = 1")
    # data = sqlConn.OutPut()
    q = False
    # for col,val in data.iteritems() :
    #     #print (val[0])  
    #     q = val[0]
    response = requests.get("http://localhost:8090/api/common/getAllStatusId").json()
    data = response
    for i in data :
        # print(i['STATUS'])
        q = i['STATUS']
        return q


# print(getQueName())
def _beginWork() :		
    q = getQueName()
    if q == 'N' :
        # UPDATE SATATUS D
        sqlConn = sql_conn("UPDATE EXAT_GIS_TEST.dbo.INSERSAP_STATUS SET STATUS = 'C' WHERE STATUS_SEQ = 1")
        data = sqlConn.Update()
        os.system("D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\startup.bat")
    print(q)

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

setInterval(_beginWork,5)