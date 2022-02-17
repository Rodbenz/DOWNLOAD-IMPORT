import os
from config.sql_server_conn import sql_conn
import requests
import  threading
import json

def getQueName() : 
    q = False
    response = requests.get("http://localhost:8090/api/common/getAllStatusId").json()
    data = response
    for i in data :
        # print(i['STATUS'])
        q = i['STATUS']
    return q

def _beginWork() :		
    q = getQueName()
    if q == 'N' :
        # UPDATE SATATUS D

        url = "http://localhost:8090/api/common/updateSatatus"
        payload = json.dumps({
        "status": "D"
        })
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        os.system("D:\DOWNLOAD-IMPORT\MANUAL\PY_IMPORTTXT\BATCH\START-UP.bat")
    if(q == 'C'):
        print('รอดำเนินการ')
    elif(q == 'D'):
        print('กำลังดำเนินการ')
    elif(q == 'N'):
        print('เริ่มดำเนินการ')

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

setInterval(_beginWork,3)