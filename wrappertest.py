import asyncio

def decor(func):
    ab = 2

    async def wrapper(*args, **kwargs):
        print(ab)
        await func(*args, **kwargs)
        return True
    return wrapper

@decor
async def summ (a, b):
    print(a + b)


async def runit():
    print(await summ(2,2))

asyncio.run(runit())


