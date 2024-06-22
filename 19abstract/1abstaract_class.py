from abc import ABC , abstractmethod

class computer:
    @abstractmethod
    def procces(Abc):
        pass
class laptop(computer):
    def procces(self):
        print("its lap")
        
# class whiteboard(computer):
#     def write(self):
#         print("its write")

class programmer:
    def work(self,com):
        print("its pro")
        com.procces()

lap = laptop()
# wri = whiteboard()
pro = programmer()
# pro.work(wri)
pro.work(lap)
lap.procces()
