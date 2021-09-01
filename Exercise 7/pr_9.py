import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''select * from product order by cost_price''')
res = cr.fetchall()
print("PRODUCT ORDER BY :",res)

con.commit()
cr.close()
con.close()