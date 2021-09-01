import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''alter table product add column category_id integer,add foreign key(category_id) references category(id)''')

con.commit()
cr.close()
con.close()