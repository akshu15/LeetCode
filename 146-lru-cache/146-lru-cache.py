
from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)    #once function called move the key to end (recently used)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val                   #inserts at end
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)      #pop top item   (LRU)
                
#Top-> LRU
#bottom-> recently used
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#if no key-> -1  ---------same
#value---------same
#initialize with +ve capacity ----------any constraints(min and max)
#update if exists else add it to cache
#if if exceeds the capacity -> remove LRU key


#Approach:-

#Dictionary:- key-value entry
#get:- If the value exits in the dictionary. If it does then I will just fetch it from there
#put:- If while getting the value its not there in dict, then add it over there. Else if it does then update it

#Capacity exceeded:-adding an element in the values part of the dictionary

#dict={
# key: [value, lruVal]
# }

# lruVal:- initially=0
#     comparing- compare with other key's lruVal and pop the least one's key












