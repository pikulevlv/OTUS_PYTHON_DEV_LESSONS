# GEVENT
import gevent.monkey
from urllib.request import urlopen
gevent.monkey.patch_all()
urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def print_head(url):
    print('Starting {}'.format(url))
    data = urlopen(url).read()
    print('{}: {} bytes: {}'.format(url, len(data), data[:100]))

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)

print('*'*50)

# TORNADO
# import tornado.ioloop
# from tornado.httpclient import AsyncHTTPClient
#
# urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']
#
#
# def handle_response(response):
#     if response.error:
#         print("Error:", response.error)
#     else:
#         url = response.request.url
#         data = response.body
#         print('{}: {} bytes: {}'.format(url, len(data), data[:100]))

# http_client = AsyncHTTPClient()
# for url in urls:
#     http_client.fetch(url, handle_response)
#
# tornado.ioloop.IOLoop.instance().start()

import asyncio
import aiohttp

# urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(html[:200])
            print("---"*5)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

print('*'*50)
# MULTIPROCESSING

from multiprocessing import Process
import os, time, datetime, random, tracemalloc

tracemalloc.start()
children = 10    # number of child processes to spawn
maxdelay = 6    # maximum delay in seconds

def status():
    return ('Time: ' +
        str(datetime.datetime.now().time()) +
        '\t Malloc, Peak: ' +
        str(tracemalloc.get_traced_memory()))

def child(num):
    delay = random.randrange(maxdelay)
    print(f"{status()}\t\tProcess {num}, PID: {os.getpid()}, Delay: {delay} seconds...")
    time.sleep(delay)
    print(f"{status()}\t\tProcess {num}: Done.")

if __name__ == '__main__':
    print(f"Parent PID: {os.getpid()}")
    for i in range(children):
        proc = Process(target=child, args=(i,))
        proc.start()
print('*'*50)
# THREADING

from threading import Thread
import os, time, datetime, random, tracemalloc

tracemalloc.start()
children = 4    # number of child threads to spawn
maxdelay = 6    # maximum delay in seconds

def status():
    return ('Time: ' +
        str(datetime.datetime.now().time()) +
        '\t Malloc, Peak: ' +
        str(tracemalloc.get_traced_memory()))

def child(num):
    delay = random.randrange(maxdelay)
    print(f"{status()}\t\tProcess {num}, PID: {os.getpid()}, Delay: {delay} seconds...")
    time.sleep(delay)
    print(f"{status()}\t\tProcess {num}: Done.")

if __name__ == '__main__':
    print(f"Parent PID: {os.getpid()}")
    for i in range(children):
        thr = Thread(target=child, args=(i,))
        thr.start()