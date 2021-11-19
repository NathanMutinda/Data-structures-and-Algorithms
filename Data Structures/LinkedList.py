class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head


        llstr = ''

        while itr:
            llstr += str(itr.data) + '----->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0

        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_value_after(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    """
    def insert_after_value(self, data_after, data_to_insert):
        if data_after < -1 or data_after > self.get_length() + 1:
            raise Exception("invalid value")
        if data_after == -1:
            self.insert_at_begining(data_to_insert)

        count = 0
        itr = self.head
        while itr:
            if count == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
"""


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_values(["Bananas", "mango", "grapes", "orange"])
    ll.insert_at_begining("popo")
    ll.insert_at_end('kiki')
    # ll.print()
    print('###########')
    ll.get_length()

    # ll.print()

    # print('################$$$')
    # ll.insert_value_after("grapes", "fitz")

    ll.print()
    # print("length:", ll.get_length())

