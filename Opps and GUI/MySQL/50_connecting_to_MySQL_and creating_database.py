'''import pymysql

#creatin a database

db = pymysql.connect()



cursor = db.cursor()


cursor.execute('CREATE DATABASE python_class')

print('Database is successfully created ')

db.close()










import pymysql

db = pymysql.connect()

cursor = db.cursor()

cursor.execute('CREATE DATABASE srinu_no_1 ')

print('creating database successfully completed')

db.close()'''


import pymysql


db = pymysql.connect()

cursor = db.cursor()

cursor.execute('SELECT VERSION()')

data = cursor.fetchone()

print('database version : %s '% data)

db.close()





































