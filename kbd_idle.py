import time
import asyncio
import aiofiles
import signal


t = time.time()
t_max = 150
idle = False

def read_state():
    with open('/sys/class/leds/asus::kbd_backlight/brightness', 'r') as f:
        return(f.read())

def turn(s=0):
    with open('/sys/class/leds/asus::kbd_backlight/brightness', 'w') as f:
        f.write(str(s))

state = read_state()

async def get_input(path, n):
    global t, idle, state
    while True:
        async with aiofiles.open(path, 'rb') as f:
            byte = await f.read(n)
            t = time.time()
            if idle:
                idle = False
                turn(state)
    asyncio.get_event_loop().stop()

async def set_idle():
    global t, idle, state
    while True:
        await asyncio.sleep(1)
        if time.time()-t > t_max and not idle:
            idle = True
            state = read_state()
            turn()
    asyncio.get_event_loop().stop()

def main():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(get_input('/dev/input/event3', 16))
    asyncio.ensure_future(get_input('/dev/input/mice', 3))
    asyncio.ensure_future(set_idle())
    loop.run_forever()
    loop.close()

if __name__ == '__main__':
    main()
