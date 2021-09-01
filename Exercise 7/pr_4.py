import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute('''create table category(id integer,code integer unique,name varchar(20) not null,primary key(id))''')

con.commit()
cr.close()
con.close()