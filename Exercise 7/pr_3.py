import psycopg2
con = psycopg2.connect(database='employee',user='tus',password='tus')
cr = con.cursor()

cr.execute(''' create sequence seq_id start with 1 increment 1; ''')
cr.execute('''create table product(id integer default nextval('seq_id'),name varchar(20) not null,cost_price integer,sell_price integer,primary key(id), check(sell_price>cost_price)) ''')

con.commit()
cr.close()
con.close()