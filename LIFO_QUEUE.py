#creatin a Lifoqueue stack

from queue import LifoQueue

stack=LifoQueue(maxsize=3)
print("Size of the stack before putting : ",stack.qsize())
print("After putting the items")
stack.put("a")
stack.put("b")
stack.put("c")

#check stack is full

print("stack is full : " ,stack.full())
print("size: ",stack.qsize())

#get enterd items from stack

print("poped Items from stack")
print(stack.get())
print(stack.get())
print(stack.get())

#check stack is empty then make it true

print("stack is empty: ",stack.empty())

#end of code