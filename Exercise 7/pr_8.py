import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''select * from product''')
res = cr.fetchall()
print("FIRST PRODUCT :",res[0])

con.commit()
cr.close()
con.close()