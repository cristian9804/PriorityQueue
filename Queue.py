
class ArrayList:
    def __init__(self):
        self.inArray = [0 for i in range(10)]
        self.count = 0
        
    def get(self, i):
        return self.inArray[i]

    def set(self, i, e):
        self.inArray[i] = e

    def length(self):
        return self.count

    def append(self, e):
        self.inArray[self.count] = e
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp()

    def insert(self, i, e):
        for j in range(self.count,i,-1):
            self.inArray[j] = self.inArray[j-1]
        self.inArray[i] = e
        self.count += 1
        if len(self.inArray) == self.count:
            self._resizeUp()
    
    def remove(self, i):
        self.count -= 1
        val = self.inArray[i]
        for j in range(i,self.count):
            self.inArray[j] = self.inArray[j+1]
        return val

    def _resizeUp(self):
        newArray = [0 for i in range(2*len(self.inArray))]
        for j in range(len(self.inArray)):
            newArray[j] = self.inArray[j]
        self.inArray = newArray
        
    def _checkBounds(self, i, hi):  # checks whether i is in [0,hi]
        if i < 0 or i > hi:
            raise Exception("index "+str(i)+" out of bounds!")

class PQElement:
    def __init__(self, v, p):
        self.val = v
        self.priority = p
        
    def __str__(self):
        return "("+str(self.val)+","+str(self.priority)+")"
    
class PQueue():
    def __init__(self):
        self.inList = ArrayList()

    def size(self):
        return self.inList.length()

    def deq(self):
        head = self.inList.length()-1
        return self.inList.remove(head)

    def enq(self,e):
        self.inList.insert(0,e)
        
        
ls7 = PQueue()
for i in range(15):
    ls7.enq(PQElement(i,10-i))
    print(ls7)
    print(ls7.deq(),ls7)

