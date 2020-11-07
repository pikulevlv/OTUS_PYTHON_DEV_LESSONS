from tortoise import Tortoise,run_async, fields
from tortoise.models import Model
import asyncio

class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

async def init():

    await Tortoise.init(
        db_url='postgres://admin1:12345678@localhost/demo1',
        modules={'models': ['__main__']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

async def main():
    await init()
    tournament = Tournament(name='New Tournament')
    await tournament.save()
    await Tournament.create(name='Another Tournament')
    tour = await Tournament.filter(name__contains='Another').first()
    print(tour.name, tour.id)

if __name__ == '__main__':
    # asyncio.run(init())
    run_async(main)