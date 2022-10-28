class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__self(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "insert new element as the head of the LinedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the fist(head) element in the LinkedList as return it"
        if self.head:
            deleted_head = self.head
            self.head = self.head.next
            return deleted_head

class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
    
    def pop(self):
        "Pop (remove) the first element off the the stack and return it"
        return self.ll.delete_first()


# Test cases

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


# Start setting up a Stack
stack = Stack(e1)


# Test stack functionality

stack.push(e2)
stack.push(e3)

print("Should be 3: ", stack.pop().value)
print("Should be 2: ", stack.pop().value)
print("Should be 1: ", stack.pop().value)

stack.push(e4)


print("Should be 4: ", stack.pop().value)