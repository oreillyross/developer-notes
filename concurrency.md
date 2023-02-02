# Concurrency

### Types

1. Multithreading
2. Multiprocessing

Working with multiple tasks that need to run

Sequential execution

### Multithreading

Multiple tasks carried out concurrently by the same process
Only one thread worked on at a time
Share the same context

Suitable for I/O tasks, database and file systems
Network tasks

### Multiprocessing

Solves limitation of single process
Two processes run a sequential plan
Processes running in parallel
Can make use of CPU cores

Ideal for CPU bound tasks, image processing, numerical operations

### Concurrent programming differences between

1. Multithreading - Threads share CPU core, lightweight, switching is quick
Python interpreter runs on a single thread using a global interpreter lock (GIL)
Threads share compute time
Threads are better for I/O operations

Multiple threads cannot speed up processing in CPU bound tasks

Processes get around GIL, Can use multiple cores, suitable to CPU bound tasks, sharing data is complicated with multi processes

switching between processes is relatively slow

#### Challenges with concurrent programming

concurrent execution, Race condition - systems behaviour dependant on sequence or timing of other uncontrollable factors

To overcome this race condition problem, use synchornization locks

Synchronization locks - Threads should synchornize their actions
Lock a resource while using it

In python can use locks and re-entrant locks

#### Semaphores

An object which restricts number of tasks using a resource
Keeps a counter, and manages how many tasks are using the resource

### Synchronization using events 

Allow you to wait for an event or state

use the wait() function or check_status() 

Use a timeout to prevent infinite waiting

Use condition objects to include  a lock for a resource
The first task notifies of its release

### Deadlocks

State where every process is wiating for every other process, like a traffic jam.
Four conditions need to be met
1. Mutual Exclusion
2. Hold and Wait
3. No preemption
4 circular wait

#### Data Structures for Concurrent tasks

1. The producer-consumer problem
2. producers and consumers run in seperate threads
3. Python includes thread safe queue DS, put and get functions

* queue
* lifoqueue (stack)
* priorityqueue

All are synchoronized, thread safe

inter-process communication

Queue 
Pipe (optimised queue DS)
highly optimized for two-way communcation

## Thread and Process pool

1. Create a new thread for each new task, very memory intensive
2. Slow things down if the number of tasks is large
3. Make use of Pools
4. Create four different workers, limited to say 4
5. 7 different tasks need to run, 4 run, 3 wait, can jump
6. Pools in python
7. thread and processes pools can be created
8. process pool size is defaulted to number of CPU cores










