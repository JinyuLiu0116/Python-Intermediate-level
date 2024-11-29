#Node class is responsible for storing
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
#a container class
class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        pass

    def __contains__(self):
        pass

    def __len__(self):
        pass

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    def prepend(self, value):
        pass

    def insrt(self, value, index):
        pass

    def delete(self, value):
        pass

    def pop(self, index):
        pass

    def get(self, index):
        pass

    def print(self):
        pass


if __name__ == "__main__":
    pass