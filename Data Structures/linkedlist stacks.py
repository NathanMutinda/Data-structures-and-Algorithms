class Empty(Exception):
    pass


class LinkedStack:
    class Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        value = self.head.element
        self.head = self.head.next
        self.size = self.size - 1
        return value

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self.head.element

    def display(self):
        temp = self.head
        while temp:
            print(temp.element, end='-->')
            temp = temp.next
            print()


l = LinkedStack()
l.push(10)
l.push(20)
l.push(30)
l.push(40)
l.push(50)
l.display()
print('popped:  ', l.pop())

print('top element is:  ', l.top())
l.pop()
l.display()
l.is_empty()
l.pop()
l.pop()
l.display()


