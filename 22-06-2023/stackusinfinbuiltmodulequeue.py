from queue import LifoQueue
s=LifoQueue(maxsize=3)#maxsize used to restrict size
print(s.qsize())#qsize used to find current size
s.put('a')
s.put('b')
s.put('c')
print(s.full())#used to find whether stack is full or not
print(s.qsize())
print(s.get())#used to pop
print(s.get())
print(s.get())
print(s.empty())#used to find whether stack is empty
