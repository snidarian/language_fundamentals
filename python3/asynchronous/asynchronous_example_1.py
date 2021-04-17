#!/usr/bin/python3


import asyncio

loop = asyncio.get_event_loop()



@asyncio.coroutine
def hello():
    print('Hello')
    yield from asyncio.sleep(3)
    print('World')


if __name__=='__main__':
    loop.run_until_complete(hello())









