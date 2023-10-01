import pymysql

#connection to all databases

db = pymysql.connect()

#preparint cursor object

cursor = db.cursor()

#opening particular database
cursor.execute('use python_class')

#SQL command
sql = "UPDATE EMPLYEE SET AGE = AGE + 1 \
                WHERE SEX = '%c'"%('M')
try:
    #excute sql in database
    cursor.execute(sql)
    #commit your data into database
    db.commit()
    print('Your data is successfully updated')

except:
    #rolling back when error occurs
    db.rollback()
    print('Your data is not updated')

#dicontinuing with the server

db.close()
