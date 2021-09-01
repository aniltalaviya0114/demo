import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''update product set cost_price = 90 where id = 1''')
cr.execute('''update product set cost_price = 85 where id = 2''')
cr.execute('''update product set cost_price = 25 where id = 3''')

con.commit()
cr.close()
con.close()