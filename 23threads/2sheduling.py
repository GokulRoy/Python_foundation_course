# for scheduling we use slepp to wait the code while executing continously
# we need to import sleep from time
from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(8):
            print("Hello")
            # we use sleep for 1sec and continue
            sleep(0.5)
class hi(Thread):
    def run(self):
        for j in range(8):
            print("Hi")
            # we use sleep for 1sec and continue
            sleep(0.5)
# now create object for them
t1 = hello()
t2 = hi()
# here use start to print the threading
# start to print at a time but here also colision happens
t1.start()
# to avoid we use sleep
sleep(0.2)
t2.start()
