class Queue:
    def __init__(self, capacity):
        self.front_index = -1
        self.rear_index = -1
        self.capacity = capacity
        self.queueArray = [None] * capacity

    def enqueue(self, data):
        if self.rear_index == self.capacity - 1:
            print("Queue overflow")
            return
        
        if self.rear_index == -1:
            self.front_index = 0
            self.rear_index = 0
            self.queueArray[self.rear_index] = data
            return

        self.rear_index += 1
        self.queueArray[self.rear_index] = data

    def dequeue(self):
        if self.front_index == -1 and self.rear_index == -1:
            print("Queue underflow")
            return

        if self.front_index == self.rear_index:
            mydata = self.queueArray[self.front_index]
            self.front_index = -1
            self.rear_index = -1
            return mydata
        
        mydata = self.queueArray[self.front_index]
        self.front_index += 1
        return mydata
    
    def isEmpty(self):
        return self.front_index == -1
    
    def isFull(self):
        return self.rear_index == self.capacity - 1
    
    def getFront(self):
        if self.front_index == -1:
            return None
        return self.queueArray[self.front_index]
    
    def getRear(self):
        if self.rear_index == -1:
            return None
        return self.queueArray[self.rear_index]


# Create queue with capacity 5
myQueue = Queue(5)

print(myQueue.isEmpty())  # True
print(myQueue.isFull())   # False

myQueue.enqueue(10)
myQueue.enqueue(12)
myQueue.enqueue(13)
myQueue.enqueue(14)
myQueue.enqueue(9)
myQueue.enqueue(8)  # Overflow

print("dequeue data:", myQueue.dequeue())
print("dequeue data:", myQueue.dequeue())
print("dequeue data:", myQueue.dequeue())
print("dequeue data:", myQueue.dequeue())
print("dequeue data:", myQueue.dequeue())
print("dequeue data:", myQueue.dequeue())  # Underflow