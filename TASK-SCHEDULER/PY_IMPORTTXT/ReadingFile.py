# file Ojects

from cmath import pi
from dataclasses import replace
from email import header
import glob
import os
import datetime
from config.sql_server_conn import sql_conn

pathFile = 'D://DOWNLOAD-IMPORT/TASK-SCHEDULER/PY_IMPORTTXT\LOGINSERTTXT/'
header_name = "log file ตรวจสอบการนำเข้าข้อมูลจากไฟล์ Text ==>"
dont = ".............................................................................................................................................................................................................................................................................................................\n"
summarize = "สรุปการนำเข้า\n"
yesimport = "นำเข้าทั้งหมด ==>"
cannot = "นำเข้าไม่ได้ไม่ได้ ==>"
errorDatabass = ""
i=0



def get_value_textfileEQUIPMENT(file):
    # tz = pytz.timezone('UTC')
    newdate = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = str.format('logFile_EQUIPMENT'+str(newdate)+'.txt')
    countEq = 0
    summarCountEq = ""
    f = open(file, 'r', encoding="utf8")
    s=f.readlines()
    if not os.path.isdir(pathFile) :
        os.makedirs(pathFile)
    with open(pathFile + filename, "a+") as f : 
        f.write(header_name + file + "\n" + dont)  
        for col in s:
            array_text = col.split("|")
            number_pite = len(array_text)
            if number_pite == 54:
                EQUIPMENT_NO=array_text[0]
                FUNCTIONAL_LOC=array_text[1]
                ASSET_NO=array_text[2]
                ASSET_SUBNO=array_text[3]
                EQUIPMENT_DESC=array_text[4]
                FUNCTIONAL_DESC=array_text[5]
                ASSET_DESC=array_text[6]
                VALID_FROM=array_text[7]
                VALID_TO=array_text[8]
                CLASS_TYPE=array_text[9]
                CLASS_DETAIL=array_text[10]
                COST_CENTER=array_text[11]
                COST_CENTER_DESC=array_text[12]
                MAIN_WORFKCTR=array_text[13]
                MAIN_WORFKCTR_DESC=array_text[14]
                CREATE_DTM=array_text[15]
                CREATE_USER=array_text[16]
                UPDATE_DTM=array_text[17]
                UPDATE_USER=array_text[18]
                EQTYP=array_text[19]
                EQART=array_text[20]
                WAERS=array_text[21]
                INGRP=array_text[22]
                SERGE=array_text[23]
                MSGRP=array_text[24]
                RBNR=array_text[25]
                ANSDT=array_text[26]
                ANSWT=array_text[27]
                HERST=array_text[28]
                TYPBZ=array_text[29]
                MAPAR=array_text[30]
                MGANR_L=array_text[31]
                GARTX_L=array_text[32]
                GWLDT_L=array_text[33]
                INVNR=array_text[34]
                GROES=array_text[35]
                BAUJJ=array_text[36]
                BAUMM=array_text[37]
                HERLD=array_text[38]
                STORT=array_text[39]
                BEBER=array_text[40]
                STATUS=array_text[41]
                DATE=array_text[42]
                CHASSNO=array_text[43]
                ENGINNO=array_text[44]
                CONTROL=array_text[45]
                VENDOR_NAME=array_text[46]
                TELEPHONE=array_text[47]
                PURCH_MAT=array_text[48]
                VERSION=array_text[49]
                INVENNO=array_text[50]
                OTH1=array_text[51]
                OTH2=array_text[52]
                OTH3=array_text[53]
                sqlConn = sql_conn("EXEC EXAT_GIS.dbo.[INSERT_BR_FROM_SAP_EQUIPMENT]"+ "'"+EQUIPMENT_NO+"','"+FUNCTIONAL_LOC+"','"+ASSET_NO+"','"+ASSET_SUBNO+"','"+EQUIPMENT_DESC+"','"+FUNCTIONAL_DESC+"','"+ASSET_DESC+"','"+VALID_FROM+"','"+VALID_TO+"','"+CLASS_TYPE+"','"+CLASS_DETAIL+"','"+COST_CENTER+"','"+COST_CENTER_DESC+"','"+MAIN_WORFKCTR+"','"+MAIN_WORFKCTR_DESC+"','"+CREATE_DTM+"','"+CREATE_USER+"','"+UPDATE_DTM+"','"+UPDATE_USER+"','"+EQTYP+"','"+EQART+"','"+WAERS+"','"+INGRP+"','"+SERGE+"','"+MSGRP+"','"+RBNR+"','"+ANSDT+"','"+ANSWT+"','"+HERST+"','"+TYPBZ+"','"+MAPAR+"','"+MGANR_L+"','"+GARTX_L+"','"+GWLDT_L+"','"+INVNR+"','"+GROES+"','"+BAUJJ+"','"+BAUMM+"','"+HERLD+"','"+STORT+"','"+BEBER+"','"+STATUS+"','"+DATE+"','"+CHASSNO+"','"+ENGINNO+"','"+CONTROL+"','"+VENDOR_NAME+"','"+TELEPHONE+"','"+PURCH_MAT+"','"+VERSION+"','"+INVENNO+"','"+OTH1+"','"+OTH2+"','"+OTH3.replace("\n","")+"'")
                data = sqlConn.Exec_()
                if data == 1:
                    countEq = countEq + data
                    print(+countEq)
                    summarCountEq = countEq
                    f.write("successfully "+str(date)+"==>"+col)   
                else:
                    print(data)
                    errorDatabass = data
                # print(array_text)
            else:
                ++i
                f.write("Error "+str(date)+"==>"+col)
                pass 
        f.write(dont + summarize + yesimport + str(summarCountEq) + "\n")
        f.write(cannot + str(i))
        f.close()
            
       


def get_value_textfileNOTIFICATION(file):
    newdate = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = str.format('logFile_NOTIFICATION'+str(newdate)+'.txt')
    countNoTi = 0
    summarCount = ""
    f = open(file, 'r', encoding="utf8")
    s=f.readlines()
    if not os.path.isdir(pathFile) :
        os.makedirs(pathFile)
    filetxt = open(pathFile+filename, "a+" , encoding="utf8", errors='ignore')
    filetxt.write(header_name + file + "\n" + dont)  
    for col in s:
        array_text = col.split("|")
        number_pite = len(array_text)
        if number_pite == 25:
            QMNUM=array_text[0]
            QMART=array_text[1]
            QMTXT=array_text[2]
            ARTPR=array_text[3]
            PRIOK=array_text[4]
            PRIORITY=array_text[5]
            MZEIT=array_text[6]
            QMDAT=array_text[7]
            QMNAM=array_text[8]
            AUFNR=array_text[9]
            KTEXT=array_text[10]
            TPLNR=array_text[11]
            PLTXT=array_text[12]
            EQUNR=array_text[13]
            EQKTX=array_text[14]
            INGRP=array_text[15]
            INNAM=array_text[16]
            PARNR=array_text[17]
            ABNAME=array_text[18]
            STATUS=array_text[19]
            NOTI_LONG_TEXT=array_text[20]
            ERNAM=array_text[21]
            ERDAT=array_text[22]
            AENAM=array_text[23]
            AEDAT=array_text[24]

            sqlConn = sql_conn("EXEC EXAT_GIS.dbo.[INSERT_BR_FROM_SAP_NOTI]"+ "'"+QMNUM+"','"+QMART+"','"+QMTXT+"','"+ARTPR+"','"+PRIOK+"','"+PRIORITY+"','"+MZEIT+"','"+QMDAT+"','"+QMNAM+"','"+AUFNR+"','"+KTEXT+"','"+TPLNR+"','"+PLTXT+"','"+EQUNR+"','"+EQKTX+"','"+INGRP+"','"+INNAM+"','"+PARNR+"','"+ABNAME+"','"+STATUS+"','"+NOTI_LONG_TEXT+"','"+ERNAM+"','"+ERDAT+"','"+AENAM+"','"+AEDAT.replace("\n","")+"'")
            data = sqlConn.Exec_()
            if data == 1:
                countNoTi = countNoTi + data
                print(countNoTi)
                summarCount = countNoTi
                filetxt.write("successfully "+str(date)+"==>"+col)    
            else:
                print(data)
                errorDatabass = data
            # print(array_text)
        else:
            ++i
            filetxt.write("Error "+str(date)+"==>"+col)
    # filetxt.write(dont + errorDatabass + "\n")
    filetxt.write(dont + summarize + yesimport + str(summarCount) + "\n")
    filetxt.write(cannot + str(i))
    filetxt.close()
            


def get_value_textfileWORK_ORDER(file):
    newdate = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = str.format('logFile_WORK_ORDER'+str(newdate)+'.txt')
    countWo = 0
    summarCountWo = ""
    f = open(file, 'r', encoding="utf8")
    s=f.readlines()
    if not os.path.isdir(pathFile) :
        os.makedirs(pathFile)
    filetxt = open(pathFile+filename, "a+" , encoding="utf8", errors='ignore')
    filetxt.write(header_name + file + "\n" + dont)
    for col in s:
        array_text = col.split("|")
        number_pite = len(array_text)
        # print(number_pite)
        if number_pite == 29:
            AUART=array_text[0]
            AUFNR=array_text[1]
            TPLNR=array_text[2]
            PLTXT=array_text[3]
            EQUNR=array_text[4]
            EQKTX=array_text[5]
            KTEXT=array_text[6]
            INGRP=array_text[7]
            INNAM=array_text[8]
            PARNR=array_text[9]
            ABNAME=array_text[10]
            Q_ERDAT=array_text[11]
            STATUS=array_text[12]
            STATUS_DATE=array_text[13]
            GSTRP=array_text[14]
            GLTRP=array_text[15]
            GSTRI=array_text[16]
            GETRI=array_text[17]
            TOTAL_COST=array_text[18]
            LABOR_COST=array_text[19]
            MAT_COST=array_text[20]
            OTH_COST=array_text[21]
            PO_COST=array_text[22]
            EXT_SERVICES=array_text[23]
            WAERS=array_text[24]
            ERNAM=array_text[25]
            ERDAT=array_text[26]
            AENAM=array_text[27]
            AEDAT=array_text[28]
            # print("'"+AUART+"','"+AUFNR+"','"+TPLNR+"','"+PLTXT+"','"+EQUNR+"','"+EQKTX+"','"+KTEXT+"','"+INGRP+"','"+INNAM+"','"+PARNR+"','"+ABNAME+"','"+Q_ERDAT+"','"+STATUS+"','"+STATUS_DATE+"','"+GSTRP+"','"+GLTRP+"','"+GSTRI+"','"+GETRI+"','"+TOTAL_COST+"','"+LABOR_COST+"','"+MAT_COST+"','"+OTH_COST+"','"+PO_COST+"','"+EXT_SERVICES+"','"+WAERS+"','"+ERNAM+"','"+ERDAT+"','"+AENAM+"','"+AEDAT+"'")
            sqlConn = sql_conn("EXEC EXAT_GIS.dbo.[INSERT_BR_FROM_SAP_WORK_ORDER]"+ "'"+AUART+"','"+AUFNR+"','"+TPLNR+"','"+PLTXT+"','"+EQUNR+"','"+EQKTX+"','"+KTEXT+"','"+INGRP+"','"+INNAM+"','"+PARNR+"','"+ABNAME+"','"+Q_ERDAT+"','"+STATUS+"','"+STATUS_DATE+"','"+GSTRP+"','"+GLTRP+"','"+GSTRI+"','"+GETRI+"','"+TOTAL_COST+"','"+LABOR_COST+"','"+MAT_COST+"','"+OTH_COST+"','"+PO_COST+"','"+EXT_SERVICES+"','"+WAERS+"','"+ERNAM+"','"+ERDAT+"','"+AENAM+"','"+AEDAT.replace("\n","")+"'" )
            data = sqlConn.Exec_()
            if data == 1:
                countWo = countWo + data
                print(countWo)
                summarCountWo = countWo
                filetxt.write("successfully "+str(date)+"==>"+col)   
            else:
                print(data)
                errorDatabass = data
            # print(array_text)
        else:
            ++i
            filetxt.write("Error "+str(date)+"==>"+col)
    filetxt.write(dont + summarize + yesimport + str(summarCountWo) + "\n")
    filetxt.write(cannot + str(i))
    filetxt.close()


# list_of_files = glob.glob('D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\DOWNLOADTEXTFILE\*') # * means all if need specific format then *.csv
# latest_file = max(list_of_files, key=os.path.getctime)
# # print(latest_file)
# folder = latest_file
folder = 'D:\DOWNLOAD-IMPORT\TASK-SCHEDULER\PY_IMPORTTXT\DOWNLOADTEXTFILE\download202202031027'
txtName = os.listdir(folder)
# print(txtName)
for file in txtName:
    if file.endswith(".txt"):
        txtfile = os.path.join(folder,file)
        txtstr = txtfile.replace("\\","/")
        filenamex = os.path.join(file)
        name = filenamex.split(".")
        # print(txtstr)
        if "EQUIPMENT" in name[0]:
            print('EQUIPMENT'+txtstr)
            get_value_textfileEQUIPMENT(txtstr)
            print("\n")
        elif "NOTIFICATION" in name[0]:
            print('NOTIFICATION'+txtstr)
            get_value_textfileNOTIFICATION(txtstr)
            print("\n")
        elif "WORK_ORDER" in name[0]:
            print('WORK_ORDER'+txtstr)
            get_value_textfileWORK_ORDER(txtstr)
            print("\n")
        else:
            print("NO Table")
            print("\n")
        

            