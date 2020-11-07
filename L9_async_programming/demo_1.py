import asyncio #asynchronous input-output
import aiohttp # pip3 install aiohttp
import logging
from loguru import logger # pip3 install loguru
from time import sleep


def foo_sync():
    logger.info("foo_sync start")
    sleep(0.1)
    logger.info("foo_sync finish")

def bar_sync():
    logger.info("bar_sync start")
    sleep(0.1)
    logger.info("bar_sync finish")

# logging.info("Hello")
# logging.warning("Hello there!")

def run_sync():
    logger.info("Start sync")
    foo_sync()
    bar_sync()

async def foo():
    logger.info("async foo starting")
    await asyncio.sleep(1.1)
    logger.info("async foo finishing")
    return 3

async def bar():
    logger.info("async bar starting")
    await asyncio.sleep(1.1)
    logger.info("async bar finishing")
    return 7

async def run_async():
    res_foo = await foo()
    logger.info("res_foo {}", res_foo)
    res_bar = await bar()
    logger.info("res_bar {}", res_bar)

def run_main_async():
    logger.info("Starting main")
    # loop = asyncio.get_event_loop()
    # loop
    # asyncio.run(run_async())
    coros = [
        foo(),
        bar(),
    ]
    coro = asyncio.wait(coros)
    asyncio.run(coro) # асинхронный код в синхронной функции
    logger.info("Finishing main")
# API
# api.ipify.org/?format=json
# ip-api.com/json

if __name__=='__main__':
    # run_sync()
    # print(foo())
    run_main_async()
    asyncio.run(run_async())