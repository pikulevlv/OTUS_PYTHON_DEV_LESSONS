from asyncpgsa import pg
import asyncio
from sqlalchemy import MetaData, Table, Column, Integer, String, Date

metadata = MetaData()

users_table = Table(
    "users_2",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("birth_date", Date, nullable=False),
)

def left_pad(text, min_lenght):
    while len(text) < min_lenght:
        text = " " * (min_lenght - len(text)) + text
    return text

async def main():
    await pg.init(
        "postgresql://admin1:12345678@localhost/demo1"
        # host=HOST,
        # port=PORT,
        # database=DB_NAME,
        # user=USER,
        # # loop=loop,
        # password=PASS,
        # min_size=5,
        # max_size=10
    )
    # users_query = users_table.select("SELECT * FROM users_2;")
    users_query = users_table.select()
    results = await pg.query(users_query)
    for ind, row in enumerate(results):
        if ind == 0:
            print(" | ".join([left_pad(name,16) for name in row.keys()]))
        print(" | ".join([left_pad(str(value), 16) for value in row.values()]))
        # for value in row.values():
        #
        # print(row)
    print('---'*3)
    ann = await pg.fetchrow(users_query.where(users_table.c.name == "Ann"))
    print(ann)

if __name__ == '__main__':
    asyncio.run(main())