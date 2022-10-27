# Implementation of a linked list

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        # Gets an element from a particular position
        
        current = self.head
        countPosition = 1

        while current:
            if(countPosition == position):
                return current
            countPosition += 1
            current = current.next
        return None
    
    def insert(self, new_element, position):
        # inserts new node to a given location

        current = self.head

        if position < 1: return
        if position == 1:
            new_element = current.next
            current = new_element
        else:
            while(position != 1):
                position -=1
                if(position == 1):
                    new_element.next = current.next
                    current.next = new_element
                    return
                else:
                    current = current.next
                    if current == None:
                        break
        
        if position != 1:
            print("position out of range")
            return
    
    def delete(self, value):
        # deletes the first node with the given value

        # if linked list is empty
        if self.head == None:
            return
        
        current = self.head

        # if it is te first value
        if(current.value == value):
            self.head == current.next
            return
        
        while current:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

        print('value not found')
        pass


    def print_linked_list(self):
        listToPrint=[]
        current = self.head
        while current:
            listToPrint.append(current.value)
            current = current.next
        print(listToPrint)



# Tests

# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)


# Set up a LinkedList

linkList = LinkedList(e1)
linkList.append(e2)
linkList.append(e3)
linkList.append(e4)
linkList.append(e5)

linkList.print_linked_list()

# Test get_position
print("Should print 3: ", linkList.get_position(3).value)
print("Should print 3: ", linkList.head.next.next.value)
print("Should print 4: ", linkList.get_position(4).value)

# Test delete
linkList.delete(1)
print("-------------")
linkList.print_linked_list()
print("Should print 2: ", linkList.get_position(1).value)
print("Should print 3: ", linkList.get_position(2).value)



