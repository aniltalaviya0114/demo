import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''update product set sell_price = 200 where id = 1''')
cr.execute('''update product set sell_price = 500 where id = 2''')

con.commit()
cr.close()
con.close()