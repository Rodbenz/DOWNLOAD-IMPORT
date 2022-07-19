import pyodbc
# # Some other example server values are
# # server = 'localhost\sqlexpress' # for a named instance
# # server = 'myserver,port' # to specify an alternate port

server = '192.168.100.230' 
database = 'EXAT_MTN' 
username = 'sa' 
password = 'td@1234' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()



# Sample select query
cursor.execute("SELECT TOP(10) EQUIPMENT_NO, FUNCTIONAL_LOC, ASSET_NO, ASSET_SUBNO, EQUIPMENT_DESC, FUNCTIONAL_DESC, ASSET_DESC, VALID_FROM, VALID_TO, CLASS_TYPE, CLASS_DETAIL, COST_CENTER, COST_CENTER_DESC, MAIN_WORFKCTR, MAIN_WORFKCTR_DESC, CREATE_DTM, CREATE_USER, UPDATE_DTM, UPDATE_USER, EQTYP, EQART, WAERS, INGRP, SERGE, MSGRP, RBNR, ANSDT, ANSWT, HERST, TYPBZ, MAPAR, MGANR_L, GARTX_L, GWLDT_L, INVNR, GROES, BAUJJ, BAUMM, HERLD, STORT, BEBER, STATUS, [DATE], CHASSNO, ENGINNO, [CONTROL], VENDOR_NAME, TELEPHONE, PURCH_MAT, VERSION, INVENNO, OTH1, OTH2, OTH3 FROM EXAT_MTN.dbo.EQUIPMENT_TEST") 
row = cursor.fetchone() 
while row: 
    print(row)
    row = cursor.fetchone()