import os
import pyodbc
import pandas as pd
import json
from dotenv import load_dotenv


class sql_conn(object):
    def __init__(self, query):
        load_dotenv()
        server = os.getenv('SERVER')
        database = os.getenv('DATABASE')
        username = os.getenv('USER')
        password = os.getenv('PASS')
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = self.conn.cursor()
        self.query = query


    def OutPut(self):
        if self.query == "":
            return 'No query.'
        else:
            data_value = pd.read_sql_query(self.query, self.conn,)
            self.conn.close()
            return data_value

    def OutPutParameter(self, changwat_code, amphur_code, tambon_code):
        if self.query == "":
            return 'No query.'
        else:
            # data_value = pd.read_sql_query(self.query, self.conn, params={changwat_code, amphur_code, tambon_code})
            # self.conn.close()
            # return data_value
            data_value = self.cursor.execute(self.query, changwat_code, amphur_code, tambon_code)
            # self.cursor.commit()
            # self.conn.close()
            return json.dumps(data_value)

    def Update(self):
        if self.query == "":
            return 'No query.'
        else:
            count = self.cursor.execute(self.query).rowcount
            self.cursor.commit()
            self.conn.close()
            return 'Rows updated: ' + str(count)

    def Insert(self, changwat_code, amphur_code, tambon_name):
        if self.query == "":
            return 'No query.'
        else:
            count = self.cursor.execute(self.query, changwat_code, amphur_code, tambon_name).rowcount
            self.cursor.commit()
            self.conn.close()
            return 'Rows inserted: ' + str(count)

    def Delete(self):
        if self.query == "":
            return 'No query.'
        else:
            count = self.cursor.execute(self.query).rowcount
            self.cursor.commit()
            self.conn.close()
            return 'Rows deleted: ' + str(count)

    def Exec_(self):
        if self.query == "":
            return 'No query.'
        else:
            try:
                count = self.cursor.execute(self.query).rowcount
                self.cursor.commit()
                return count
            except(pyodbc.Error, pyodbc.Warning) as e:
                return e

            finally:
                self.conn.close()
