import queue

q = queue.Queue()

q.queue

for i in range(7):
    q.put(i)

q.queue # deque([0,1,2,3,4,5,6])
q.get() # 0
q.empty() # False

# Queue class is thread safe
# no need to use Semaphores, Locks, Events, Conditions
# Including LifoQueue for Stack based

q = queue.LifoQueue()

for i in range(7):
    q.put(i)

# deque([0,1,2,3,4,5,6])

q.get() # 6
q.empty() # False

q = queue.PriorityQueue()

#
import threading
import random

# Creating processes

import time
import os
from multiprocessing import Process, current_process

def square(number):
    time.sleep(1)
    result = number * number
    process_id = os.getpid()

for i in range(3):
    process = Process(target=square, args = (number,))
    # OR do this
    process_id = current_process().pid
    process_name = current_process().name
    process.start()

process.join()

# NB to note global variables or resources are much more easily shared amongst Threads than between Processes, 
# Processes often keep their own state.

# Sharing data between processes

import multiprocessing

result = []

num_list = [1,2,3,4]

# pass in the shared resource into the function by reference. 
# create the shared array resource
result = multiprocessing.Array('i', 4)
square_sum = multiprocessing.Value('i')

# ctypes must be the same

# sharing using the Manager class , server process manager

with multiprocessing.Manager() as manager:

    manager.list([])
    # all shared lists declared within with block its shared,

# Synchronizing Concurrent processes with Locks

import multiprocessing

deposit_with_mp(balance, amount, lock):
    lock.aquire
    # do somethings
    lock.release()

withdraw_with_mp(balance, amount):

balance = multiprocessing.Value('i', 600)
lock = multiprocessing.Lock()

# pass in the lock to each function needing access to the shared resource

q = multiprocessing.Queue()

d =multiprocessing.Process(target=deposit_with_mp)

def sender(connection, greets):
    for greet in greets:
        connection.send(greet)
    connection.close()

def recipient(connection):
    while True:
        greet = connection.recv()
        if greet == "STOP":
            break
        print(greet)

msgs = ["Hello, "Hola", Good Day", "STOP"]

sending_pipe, receiving_pipe = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=sender, args=(sending_pipe, msgs))
p2 = multiprocessing.Process(target=recipient, args(receiving_pipe))

p1.start()
p2.start()
p1.join()
p2.join()

# for two way communication use two pipes in different directions













