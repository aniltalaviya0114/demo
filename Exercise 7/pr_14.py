import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''select product.id,product.name,product.cost_price,product.sell_price,category.code,category.name from product inner join category on category.id = product.category_id''')
res = cr.fetchall()
print("PRODUCT JOIN :",res)

con.commit()
cr.close()
con.close()