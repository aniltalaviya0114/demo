import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''select * from product where sell_price = (select max(sell_price) from product)''')
res = cr.fetchall()
print(res)

con.commit()
cr.close()
con.close()