#!/usr/bin/python3

import asyncio

async def find_divisibles(inrange, div_by):
    print(f"finding numbers in range {inrange} divisible by {div_by}")
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
    print(f"Done with numbers in range {inrange} divisible by {div_by}")
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(40912353, 12355))
    divs2 = loop.create_task(find_divisibles(3423533, 1346))
    divs3 = loop.create_task(find_divisibles(12435, 142))
    await asyncio.wait([divs1, divs2, divs3])


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except:
        print("error")
    finally:
        loop.close()






