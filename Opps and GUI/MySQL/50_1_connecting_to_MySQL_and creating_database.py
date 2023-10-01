#How to create a table in particular database

import pymysql

db = pymysql.connect()


cursor = db.cursor()

cursor.execute('use python_class')

cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

#Create a table as per requirement

sql = '''CREATE TABLE EMPLYEE (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)'''

cursor.execute(sql)

db.close()
