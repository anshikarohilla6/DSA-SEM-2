class node : 
    def __init__(self,mydata):
        self.data = mydata
        self.address = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insertatfirstposition(self,mydata):
        newnode = node(mydata)
        newnode.address = self.head
        self.head = newnode

    def traversal(self):
        currentnode = self.head
        while currentnode  != none:
            print(currentnode.data, end=" -> ")
            currentnode = currentnode.address 


mylinkedlist = linkedlist()
mylinkedlist.insertatfirstposition(10)
mylinkedlist.insertatfirstposition(20)
mylinkedlist.insertatfirstposition(30)
mylinkedlist.traversal()