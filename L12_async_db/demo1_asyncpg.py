import asyncio
import asyncpg
from datetime import date

async def main():
    # conn = await asyncpg.connect(
    #     user='admin1', password='12345678',
    #     database='demo1', host='127.0.0.1'
    # )
    conn = await asyncpg.connect(
        "postgresql://admin1:12345678@localhost/demo1"
    )
    ## values = await conn.fetch()
    # await conn.execute(
    #     "INSERT INTO users_2(name, birth_date) VALUES($1, $2)",
    #     "John",
    #     date(1972, 3, 15),
    #
    # )
    # await conn.execute(
    #     "INSERT INTO users_2(name, birth_date) VALUES($1, $2)",
    #     "Ann",
    #     date(1972, 3, 5),
    # )
    rows = await conn.fetch("SELECT * FROM users_2;")
    today = date.today()
    for r in rows:
        print(r)
        print(r['name'], today - r['birth_date'])

    john = await conn.fetchrow("SELECT * FROM users_2 WHERE name = $1", "John")
    print(john)
    print(conn)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())