# guesses a very large number using asyncio

# program still under construction


import asyncio
import random
import time


async def make_guess():
    guess = random.randint(0, 100000)
    await asyncio.sleep(.5)
    return guess



async def main(target):
    guess = None
    while guess != target:
        guess = await asyncio.gather(make_guess())
        print(f"Guess equals = {guess}")



if __name__ == "__main__":
    target = input("Guess a number between 0 and 100,000")
    print("calling main function")
    main(target)
    print("program ended")












