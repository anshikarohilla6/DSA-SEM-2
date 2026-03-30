class Node:
    def __init__(self,myData):
        self.prev = None
        self.Data = myData
        self.next = None

class DoublyLinkedList:
    def ___init__(self):
        self.head = None
        
        def insertAtFirstPosition(self,data):
            newNode = Node(data)
            if self.head == None:
                self.head = newNode
                return
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

    def traversal(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data, end="->")
            currentNode = currentNode.next

dll = DoublyLinkedList()
dll.insertAtFirstPosition("ashu")
dll.insertAtFirstPosition("bhoomi")
dll.insertAtFirstPosition("nikki")
dll.insertAtFirstPosition("riya")
dll.traversal()


#insertion at last position


def insertAtLast (self,data):
    newNode = Node (data)
    if self.head == None:
        self.head = newNode
    else :
        curNode = self.head
        while curNode != curNode.next:
            curNode= curNode.next

        curNode.next = newNode
        newNode.prev = curNode


  #insertion at any position
   
def insertAtAnyPosition (self,data,pos):
    if pos < 0:
        return
    elif pos == 0:
        self.insertAtAnyPosition(data)
    else:
        newNode = Node (data)
        CurNode = self.head
        for i in range (pos -1)
        CurNode = curNode.next
        





    
