# import os
# import psycopg2


# conn =  psycopg2.connect(
#     host=" 0.0.0.0",
#     database="postgres",
#     # user=os.environ['postgres'],
#     password=os.environ['root']
# )


# cur = conn.cursor()


# cur.execute('DROP TABLE IF EXISTS books;')
# cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
#             'title varchar (150) NOT NULL,'
#             'author varchar (50) NOT NULL,'
#             'pages_num integer NOT NULL,'
#             'review text,'
#             'date_added date DEFAULT CURRENT_TIMESTAMP);'
# )


# conn.commit()

# cur.close()
# conn.close()