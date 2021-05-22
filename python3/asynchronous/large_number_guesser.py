#!/usr/bin/python3
# guesses a very large number using asyncio
# program is illustrative and not particularly functional or pragmatic
# written by Jordan Linzie


import asyncio
import random
import time

# coroutine makes a guess and if correct returns the guess value
async def make_guess(target):
    guess = random.randint(0, 100000)
    await asyncio.sleep(1)
    #print(f"Guess equals = {guess}")
    if guess == target:
        print(f"Target: {target} has been guessed correctly")
        answer_rocket(guess)
    else:
        pass

# Event loop
async def main(target):
    await asyncio.gather(*(make_guess(target) for i in range(50000))) # given 50,000 tries to guess the number

# display the correctly guess number
def answer_rocket(correctly_guessed_number):
    print(f"The correct number has been guessed. it is: {correctly_guessed_number}")

if __name__ == "__main__":
    target = input("Guess a number between 0 and 100,000: ")
    print("calling main function")
    start = time.perf_counter()
    asyncio.run(main(int(target)))
    end = time.perf_counter() - start
    print(f"program terminated in {end:0.4f} seconds.")












