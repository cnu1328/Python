import pymysql
#connecting to the databsaes

db = pymysql.connect()

#preparing a cursor object using cursor() mehtod

cursor = db.cursor()

#opening particular database

cursor.execute('use python_class')

#prepare SQL query a record from the database

sql = 'SELECT * FROM EMPLYEE \
        WHERE INCOME > %d '%(1000)

try:
    #execute the SQL command
    cursor.execute(sql)

    #Fench all the rows in list of lists

    results = cursor.fetchall()

    for i in results:
        fname = i[0]
        lname = i[1]
        age   = i[2]
        sex   = i[3]
        income= i[4]

        print('\n''fname = %s,lname = %s,age = %d,sex = %s,income = %d'%\
              (fname,lname,age,sex,income))
    print('\n')

except:
    print('Error: unable to fecth data')

#disconnect from the server
db.close()

