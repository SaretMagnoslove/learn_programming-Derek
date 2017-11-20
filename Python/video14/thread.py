import threading
import time
import random


def executeThread(i):

    # strftime or string formatted time allows you to
    # define how the time is displayed.
    # You could include the date with
    # strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # Print when the thread went to sleep
    print("Thread {} sleeps at {}".format(i,
                                          time.strftime("%H:%M:%S", time.gmtime())))

    # Generate a random sleep period of between 1 and
    # 5 seconds
    randSleepTime = random.randint(1, 5)

    # Pauses execution of code in this function for
    # a few seconds
    time.sleep(randSleepTime)

    # Print out info after the sleep time
    print("Thread {} stops sleeping at {}".format(i,
                                                  time.strftime("%H:%M:%S", time.gmtime())))


for i in range(10):

    # Each time through the loop a Thread object is created
    # You pass it the function to execute and any
    # arguments to pass to that method
    # The arguments passed must be a sequence which
    # is why we need the comma with 1 argument
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    # Display active threads
    # The extra 1 is this for loop executing in the main
    # thread
    print("Active Threads :", threading.activeCount())

    # Returns a list of all active thread objects
    print("Thread Objects :", threading.enumerate())

    
