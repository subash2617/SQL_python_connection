import psycopg2 as pg2
# To connect the database
conn = pg2.connect(database='dvdrental', user='postgres',password='password')
cur = conn.cursor()
cur.execute('SELECT * FROM payment')
total = 0
""" To fetch the data's use 
fetchone to get the first table value
fetchmany to get the selected no of values eg: fetchmany(5) get the 5 values
fetchall to get all the values"""
for i in cur.fetchall():
    total += 1
    print(i)
print('Total values in the Database are :',total)
# To close the connection
conn.close()