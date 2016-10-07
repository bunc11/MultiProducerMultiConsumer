from threading import Thread
from queue import Queue
from random import random
from time import sleep
import sys


class Producer(Thread):
    def __init__(self, q, identity):
        Thread.__init__(self)
        self.q = q
        self.id = identity

    def run(self):

        while True:
            rand = random()
            self.q.put(rand)
            sys.stdout.write("Producer " + str(self.id) +  " is putting " + str(rand) + "\n")
            sleep(rand*2)


class Consumer(Thread):
    def __init__(self, q, identity):
        Thread.__init__(self)
        self.q = q
        self.id = identity

    def run(self):

        while True:

            rand = self.q.get()
            sys.stdout.write("Consumer " + str(self.id) + " has taken " + str(rand) + "\n")
            sleep(rand*3)


def main():

    queue = Queue()

    p1 = Producer(queue, 1)
    p2 = Producer(queue, 2)

    c1 = Consumer(queue, 1)
    c2 = Consumer(queue, 2)

    p1.start()
    p2.start()

    c1.start()
    c2.start()

if __name__ == '__main__':
    main()


