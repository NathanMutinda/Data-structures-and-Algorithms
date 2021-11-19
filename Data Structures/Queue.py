import time
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()


    def enque(self, value):
        self.buffer.appendleft(value)

    def deque(self):
        self.buffer.pop()
        return

    def is_empty(self):
        return  len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


def place_order(order):
    t = Queue()
    for i in order:
        time.sleep(0.5)
        t.enque(i)

    print(t.buffer)
    return

def serve_order():
    t = Queue()
    time.sleep(0.5)
    y = t.deque()
    print(y)

    return



pq = Queue()

pq.enque({
    'company': 'wallmart',
    'time stamp': '15 april, 11.01 am',
    'price': 131.10
})

pq.enque({
        'company': 'wallmart',
        'time stamp': '15 april, 11.02 am',
        'price': 132.10

})
pq.enque({
    'company': 'wallmart',
    'time stamp': '15 april, 11.03 am',
    'price': 135.10

})


oder = ["pizza", 'samosa', "wings"]
place_order(oder)
serve_order()


#y = pq.size()
#p = pq.deque()
#print(p)

#print(y)
