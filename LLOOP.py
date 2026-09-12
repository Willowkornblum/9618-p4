#linked lists object orientated proggraming 
from importlib import machinery
from importlib import machinery
class node:
    def __init__ (self,data):
        self.data = data
        self.next = None    #next is the next pointer

class LL:
    def __init__ (self):
        self.head = None
#[0,1,2,3,4]
#[A,B,C,D,E]
#[2,4,1,3,None]
    def display (self):
        current = self.head
        while (current != None):
            print (current.data,end=" --> ")
            current = current.next
        print ("none")

    def search (self,item):
        current = self.head
        position = 0
        while (current != None):
            if (current.data == item):
                return position
            current = current.next
            position += 1
        return -1

    def insert_beginning(self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_end(self,data):
        newnode=node(data)
        if (self.head == None):
            self.head = newnode
            return              # doesnt return just stops the next part from running
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newnode 

    def insert_position(self,data,position):
        newnode = node(data)
        if (position == 0):
            newnode.next = self.head
            self.head = newnode
            return
        current = self.head
        for i in range (position-1):
            current = current.next
        newnode.next = current.next
        current.next = newnode

    def deletion_beginning (self):
        if (self.head == None):
            return
        self.head = self.head.next

    def deletion_end(self):
        if (self.head == None):
            return 
        if (self.head.next == None):
            self.head = None
            return 
        current = self.head
        while (current.next.next != None):
            current = current.next
        current.next = None

    def delete_item(self,data):
        if (self.head == None):
            return 
        if (self.head.data == data):
            self.head = None
            return 
        current = self.head
        while (current.next != None):
            if (current.next.data == data):
                current.next = current.next.next
                return
            current = current.next


myLL = LL()
myLL.insert_beginning('C')
myLL.insert_beginning('B')
myLL.insert_beginning('A')
myLL.insert_end('D')
myLL.insert_position('F',2)
myLL.deletion_beginning()
myLL.deletion_end()
myLL.delete_item('F')
myLL.display()

