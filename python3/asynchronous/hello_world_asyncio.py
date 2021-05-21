#!/usr/bin/python3
# doc-file demonstrating and explaining the use of python3's asyncio module/package

import asyncio

# A function that you introduce with 'async def function()' is a 'coroutine'
async def count(number):
    print("part one of coroutine " + str(number))
    # The keyword 'await' passes function control back to the event loop
    await asyncio.sleep(1) # note that time.sleep is a blocking function call while asyncio.sleep() is not
    print("part two of coroutine " + str(number))


async def main():
    await asyncio.gather(count(1), count(2), count(3), count(4))


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")








