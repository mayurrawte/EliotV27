import threading
import time


class ThreadingExample(object):

    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
        self.counter = 1
    def run(self):
        counter = 1
        while True:
            f = open('sample.txt','w')
            counter+=1
            f.write(str(counter))
            f.close()
            print('Doing something imporant in the background')
            time.sleep(self.interval)

example = ThreadingExample()
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')