class DLNode:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.head = DLNode(0, 0)
        self.tail = DLNode(0, 2)

    def get(self, key: int) -> int:
        if key in self.hashMap:    #list has the node already
            node = self.hashMap[key]
            
                                #remove the node from the list
            node.prev.next = node.next
            node.next.prev = node.prev 
            
            self.head.next.prev = node
            node.next = self.head.next

            self.head.next = node
            node.prev = self.head

            del self.hashMap[key]  #delete to update the old node value in hashMap
            self.hashMap[key] = node
            return self.hashMap[key].value
        return (-1)

    def put(self, key: int, value: int) -> None:
        
        #initially head's next points to tail and tail's prev points to head
        if self.head.next == None:
            self.head.next = self.tail
            self.tail.prev = self.head   
        
        if key in self.hashMap:    #list has the node already
            node = self.hashMap[key]
            node.value = value     #update the value
            
                                #remove the node from the list
            node.prev.next = node.next
            node.next.prev = node.prev 
            
            del self.hashMap[key]  #delete to update the old node value in hashMap
            
        else:
            
            node = DLNode(key, value)  #new Node
            
            if len(self.hashMap.items()) == self.capacity:                                
                                           #delete lru node and add the new node at the start
                lastKey = self.tail.prev.key
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                
                del self.hashMap[lastKey]
                
                
        self.head.next.prev = node
        node.next = self.head.next
        
        self.head.next = node
        node.prev = self.head

                
        self.hashMap[key] = node
        # print(node.value)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)