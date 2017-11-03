import threading
import random
import time


class costumClass(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        getTime(self.name)
        print('Thread', self.name, 'Exectution ends')


def getTime(name):
    print("Thread {} sleeps at {}".format(name,
                                          time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)


thread1 = costumClass('1')
thread2 = costumClass('2')

thread1.start()
thread2.start()

print('Thread1 is alive',thread1.is_alive())
print('Thread2 is alive',thread2.is_alive())

print('Thread1 name is',thread1.getName())
print('Thread2 name is',thread2.getName())

thread1.join()
thread2.join()

print('Exectution ends')