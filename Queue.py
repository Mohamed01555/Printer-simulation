class Queue:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0
    
    def enqueue(self,item):
        self.list.insert(0,item)    
        
    def dequeue(self):
        return self.list.pop()
        
    def size(self):
        return len(self.list)
