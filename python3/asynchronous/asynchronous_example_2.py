#!/usr/bin/python3


import asyncio

loop = asyncio.get_event_loop()


async def hello():
    print('Hello')
    await asyncio.sleep(3)
    print('World')


if __name__=='__main__':
    for iteration in range(2):
        loop.run_until_complete(hello())











