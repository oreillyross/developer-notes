# Creating a thread

# https://www.anaconda includes all of jupyter notebook and libraries and python 3.7

import threading

from pprint import pprint

def new_func():
  pprint(threading.active.count())
  pprint(threading.enumerate()) # list of current threads running
  pprint(threading.current_thread())
   
new_func()


def func1():
  print("Hello from func")

x = threading.Thread(target = func1)
x.start()

# Naming and joining threads

import time

def sleeping_func():
  time.sleep(2)
  print("Hello from sleeping")
  
x = threading.Thread(target = sleeping_func)

x.start()

x.join() # synchronize the main thread so it gets called first and then the main thread

# Deriving the thread class

threading.current_thread.getName()

# passing args to thread instantiation

thread = threading.Thread(target=calc_square, args=(n, )) # note the trailing comma
thread.start()
thread.join()

class DerivedThread(threading.Thread):
  # override the run function
  def run(self):
    
 obj = DerivedThread()
obj.start()

# Running Threads concurrently

time.sleep(1)
time.time() # to get the time

# Use start and join 

t1.start()
t1.join()

# Race conditions and locks
import threading

amount = 0

def deposit(dep_amount, dep_lock):
  global amount
  for i in range(dep_amount):
    
    dep_lock.acquire()
    # this is a shared resource needs protecting
    amount += 1
    dep_lock.release()
    

 def two_deposit_threads(dep_amount):
  
  lock = threading.Lock()
  
  t1 = threading.Thread(target=dep_amount, lock)
  t2 = threading.Thread(target=dep_amount, lock)
  
  t1.start()
  t2.start()
  
  t1.join()
  t2.join()
  
  two_deposit_threads(100000)
  
  print("{0}".format(amount))
  
  lock.acquire(timeout=3) # to ensure it eventually releases lock
  
  threading.RLock() # reentrant lock on same thread prevents error
  
  # Avoiding a deadlock
  
  lock_one.acquire()
  # do something
  lock_one.release()
  
  # do the other work for second lock
  
  # Semaphores 
  
  # any thread can call acquire() or release()
  
  semaphore = threading.Semaphore(value=3) # serves as a counter, oldest sync mechanism around, total of three threads can get access to a resource
  semaphore.acquire()
  semaphore._value
  semaphore.release()
  
  # restricts the amount of parallelism
  semaphore.acquire() # decrements counter, if its at 0 no thread can acquire the resource
  
  semaphore.release() # increments counter
  
  threading.BoundedSempahore(3) # use this to set an upper bound on number of resource usage
  
  # Events are a good way for threads to communicate with each other
  
  event = threading.Event()
  event.set()
  event.clear()
  event.is_set()
  event.wait()
  
  # Condition object slightly more involed than event object
  
  import random
  condition = threading.Condition()
  
  container = []
  
  counter = 1
  
  more_to_come = True
  
  def produce():
    global container
    global conunter
    ...
    
    time.sleep(random.randrange(2,5))
    
    condition.aquire()
    
    condition.notify_all()
    
    def consume():
      condition.aquire()
      condition.wait()
      
      time.sleep(random.random())
      print("aquired by ...
      condition.release()
            

            
  
  
  
  
  
  
  
  
  
  




