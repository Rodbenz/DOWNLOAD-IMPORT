from config.sql_server_conn import sql_conn
import json
import requests

def _updateStatus():
    # sqlConn = sql_conn("UPDATE EXAT_GIS_TEST.dbo.INSERSAP_STATUS SET STATUS = 'C' WHERE STATUS_SEQ = 1") #insert successfully
    # data = sqlConn.Update()
    # print(data)
    url = "http://localhost:8090/api/common/updateSatatus"
    payload = json.dumps({
    "status": "C"
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


_updateStatus()