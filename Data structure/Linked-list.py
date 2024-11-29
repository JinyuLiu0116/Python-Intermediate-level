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
    #O(n) linear time, linear run time complexity
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)
    #O(1) constant time
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    def insrt(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node
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