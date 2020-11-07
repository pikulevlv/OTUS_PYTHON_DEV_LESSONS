import psycopg2
from const import PASSWORD

# create a connection
conn = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "demo1",
    user = "admin1",
    password = PASSWORD,
)
print(conn)
# create a cursor
cur = conn.cursor()
print(cur)
cur.execute("DROP TABLE users ;")
# create a table
cur.execute("""CREATE TABLE users 
                    (id serial 
                        constraint users_pk
                            primary key, 
                    username varchar not null, 
                    full_name varchar default '' not null 
                    );""")
# cur.execute("DROP TABLE users ;")
cur.execute("INSERT INTO users (username) VALUES ('admin');")
cur.execute("INSERT INTO users (username, full_name) VALUES ('sam', 'sam mattews');")
cur.execute("INSERT INTO users (id, username, full_name) VALUES (7, 'john', 'gault');")
# make a query
res = cur.execute("SELECT * FROM users")
print(res)

users = cur.fetchall()
print(users)
for user in users:
    print(f"User #{user[0]} {user[1]} {user[2]}")

# print(res)
#make a commit (necessary!)
# print(conn.commit())
conn.commit()

# close connection
conn.close()