# mixing multiple actions at a time
# now we use import threading
from threading import *
# now use Thread in class to make them mix
# run at a time
class hello(Thread):
    def run(self):
        # here we take range because to know the process properly
        for i in range(100):
            print("Hello")
# same as above use same thread and also method name('run')
class hi(Thread):
    def run(self):
        # here we take range because to know the process properly
        for j in range(100):
            print("Hi")
# now create object for them
t1 = hello()
t2 = hi()
# here use start to print the threading
# start to print at a time
t1.start()
t2.start()
