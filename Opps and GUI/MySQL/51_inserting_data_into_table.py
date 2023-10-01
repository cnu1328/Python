import pymysql

#connecting to the databases
db = pymysql.connect()

#preparing a cursore object using cursor(0 method
cursor = db.cursor()

#opening a database where i can insert my values

cursor.execute('use python_class')

#table values
sql = '''INSERT INTO EMPLYEE (FIRST_NAME,LAST_NAME,
        AGE,SEX,INCOME)VALUES ('Dharpally','Srinivas',18,'M',100000) '''

try:
    #Execute the sql command
    cursor.execute(sql)

    #commit your changes in database

    db.commit()

    print('Your data is commited to database')

except:

    #Rollback in case there is any error
    db.rollback()

    print('Your data is rollbacked because of an error')

db.close()
