from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(8):
            print("Hello")
            sleep(0.5)
class hi(Thread):
    def run(self):
        for j in range(8):
            print("Hi")
            sleep(0.5)
# now create object for them
t1 = hello()
t2 = hi()

t1.start()
sleep(0.2)
t2.start()
# it prints at last if we use join
# other wise at first only
print("bye")
# now we use t1 and t2 join
t1.join()
t2.join()
# now see it will print at last
print("bye")
