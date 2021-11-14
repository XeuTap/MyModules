import time
from threading import Thread, Timer
import asyncio
import functools


def remembertime():
    start = time.gmtime()
    time.sleep(5)
    print('gotovo')
    print(time.process_time())


class CustomThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_running = True

    def run(self):
        while self.is_running:
            time.sleep(5)

    def terminate(self):
        self.is_running = False

thread = CustomThread(daemon=True)
thread.start()  # Запускаем thread
thread.terminate()  # Останавливаем thread



class BackgroundTimer(Thread):
    def run(self):
        while 1:
            time.sleep(10)
            return self.result(self.arg)

    def someth(self, _arg):
        self.arg = _arg

    async def result(self, arg):
        print(arg)


def delayedrun(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        if 'delay' not in kwargs:
            kwargs['delay'] = 5
        await asyncio.sleep(kwargs['delay'])
        print('111')
    return wrapper

async def somefunc(count):
    print(count)

async def delayed(func, *args, delay=5):
    await asyncio.sleep(delay)
    asyncio.create_task(func(*args))

async def antoherfunc():
    print('ya')

async def main():
    print('Начало блока')
  #  asyncio.create_task(delayed(somefunc, 5,  delay=5))
  #  await asyncio.wait_for(somefunc(5), timeout=10)
    print('Конец блока')
    await antoherfunc()
    while True:
        await asyncio.sleep(1)



loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except KeyboardInterrupt:
    pass
    # cancel all tasks lingering
finally:
    loop.close()
