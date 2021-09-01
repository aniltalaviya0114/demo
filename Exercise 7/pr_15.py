import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()



con.commit()
cr.close()