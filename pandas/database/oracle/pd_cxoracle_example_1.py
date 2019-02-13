
__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    This example shows how to load a dataset into a pandas DataFrame by executing a SQL query against an Oracle 
    database. The connection to the Oracle database uses the Python cx_Oracle extension developed by Oracle.
'''

import pandas as pd
import cx_Oracle

# set the needed variables to make life more easy.
orclUserName = 'pandas_test'
orclPassword = 'pandas_test'
orclHost = '192.168.33.10'
orclPort = '1521'
orclServiceName = 'pdb1'


# set the dsn, using the variables set before
dsn = cx_Oracle.makedsn(host=orclHost,
                        port=orclPort,
                        sid=None,
                        service_name=orclServiceName
                       )

# set the connection, using the dsn and variables set before
connection = cx_Oracle.connect(user=orclUserName,
                               password=orclPassword,
                               dsn=dsn,
                               encoding="UTF-8",
                               nencoding="UTF-8"
                              )

# define a SQL query to be executed against the database
query = """SELECT
                 EMPNO employee_number,
                 ENAME employee_name,
                 JOB employee_role,
                 MGR employee_manager,
                 HIREDATE employee_hiredate,
                 SAL employee_salary,
                 DEPTNO employee_department
           FROM 
               emp"""

# create a pandas DataFrame and use read_sql()
df_ora = pd.read_sql(query, con=connection)

# show the DataFrame head to proof we have received the data
print (df_ora.head())

