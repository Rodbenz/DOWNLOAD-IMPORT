from config.sql_server_conn import sql_conn

def _updateStatus():
    sqlConn = sql_conn("UPDATE EXAT_GIS_TEST.dbo.INSERSAP_STATUS SET STATUS = 'C' WHERE STATUS_SEQ = 1") #insert successfully
    data = sqlConn.Update()
    print(data)


_updateStatus()