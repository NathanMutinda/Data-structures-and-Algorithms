from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def prin(self):
        f = self.container
        print(f)
        return

def reverse_string(val):
        v = Stack()

        for ch in val:
            v.push(ch)

        rstr = ''

        while v.size() != 0:
            rstr += v.pop()

        return rstr



if __name__ == '__main__':

    print(reverse_string("we will conqure covid 19"))










