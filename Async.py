# A very good parallel execution strategy for downloading multiple files at once.

template_url =   "https://api.worldbank.org/v2/en/indicator/{resource}?downloadformat=csv"
urls = [template_url.format(resource="SP.POP.TOTL"), template_url.format(resource="NY.GDP.MKTP.CD"), template_url.format(resource='EN.POP.DNST')]

# This is the helper download function
import requests
def download_file(url):
    response = requests.get(url)
    if 'content-disposition' in response.headers:
        content_disposition = response.headers['content-disposition']
        filename = content_disposition.split("filename=")[1]
    else:
        filename = url.split('/')[-1]
    with open(filename, mode="wb") as file:
        file.write(response.content)
    print(f"Downloaded file {filename}")

# Where the Magic happens with the downloads in parallel
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    executor.map(download_file, urls)
        

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

type(func) # coroutine

import asyncio

loop = asyncio.get_event_loop()

loop.run_until_complete(main())

loop.close()

# To run asyncio.run asynchronously

async def main():
    
    task_1 = asyncio.create_task(greeting("Hello"))
    await task_1
    # ... add as many tasks
    # or us the below to pass multiple funcs
    await asyncio.gather(...func1, func2, etc)











