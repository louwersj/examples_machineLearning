
# WIP -- DO NOT USE

import pandas as pd
import cx_Oracle



orclUserName='pandas_test'
orclPassword='pandas_test'
orclHost = '192.168.33.10'
orclPort = '1521'
orclServiceName= 'pdb1'

dsn = cx_Oracle.makedsn(host=orclHost,port=orclPort,sid=None,service_name=orclServiceName)


connection = cx_Oracle.connect(user=orclUserName, password=orclPassword, dsn= dsn ,encoding = "UTF-8", nencoding = "UTF-8")


query = """select empno from emp"""

df_ora = pd.read_sql(query, con=connection)

print (df_ora.head())

