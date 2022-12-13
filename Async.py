# Process Pooling

def cal_square(num):
    return num * num

nums = [1,2,3,4]

import os
os.cpu_count() # usually return 4 -> 4 cores


os.getpid() # to see which process

from multiprocessing import pool  # make maximum use of all cores 

P = Pool()
# for multiple functions use the starmap function of Pool class
pool.starmap(func, [(a,b), (c,d)...])

result = p.map(cal_square, nums)

p.close()
p.join()

p = Pool(processes=2)

import time

# Concurrent futures model

from concurrent.futures import ThreadPoolExecutor # or ProcessPoolExecutor

def returnTime(n, message):
    time.sleep(n)
    return message

pool = ThreadPoolExecutor(3)

submit = pool.submit(returnTime, 60, "Hello")

submit.done() # False if still running in async

print(submit.result()) # will return after 60 seconds

# Threads vs Processes for Network tasks

from concurrent.futures import as_completed
import urllib.request


urls = ['http://eeerr.com'...]

def url_loader(url, time):
    with urllib.request.urlopen(url, timeout=time) as conn:
        return conn.read() 

def main_processpool():
    start = time.time()

    with ProcessPoolExecutor(max_workers=7) as executor:
        future_to_page = {executor.submit(url_loader, url, 60) : url for url in urls}

        for future in as_completed(future_to_page):
            url = future_to_page[future]
            result = future.result()
            print('%r' % (url))

# Threads vs Processes for CPU Bound tasks

# asyncio module

async def main():
    print('Hello')

func = main()

func










