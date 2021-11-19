class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def dic(self):
        return len(self._data)

    def is_empty(self):
        return self._data == 0

    def push(self):
        e = input('enter item to push:-- ')
        self._data.append(e)
        return 'you added ', e

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]


s = ArrayStack()
print ('this is the  menu \n 1:add item \n 2:view items \n 3:'
       'remove item \n 4:check if empty')

d = input('enter your choice:-- ')
if d == '1':
    print(s.push())
elif d == '2':
    print(s.is_empty())
elif d == '3':
    print(s.pop())
elif d == '4':
    print(s.is_empty())
else:
    print('enter a valid choice')
