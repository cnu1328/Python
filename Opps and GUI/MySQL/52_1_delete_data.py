import pymysql

#connecting to the data base
db = pymysql.connect()

#preparing a cursor
cursor = db.cursor()
#connecting to the particular database
cursor.execute('use python_class')

sql = 'DELETE FROM EMPLYEE \
             WHERE AGE > %d'%(18)
try:
    #Execute
    cursor.execute(sql)
    #commit
    db.commit()
    print('your data is deleted')
except:
    #rollback
    db.rollback()
    print('your data is not deleted')

#disconnect from server
db.close()
