#using _thread module

import _thread
import time

#define a function for the thread

def print_time(threadName,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count += 1
        print('%s : %s \n'%(threadName, time.ctime(time.time())))


#create two threads as follows

try:
    _thread.start_new_thread(print_time,('thread-1',2))
    _thread.start_new_thread(print_time,('thread-2',3))

except:
    print('Error: unable to start thread')

while 1:
    pass
