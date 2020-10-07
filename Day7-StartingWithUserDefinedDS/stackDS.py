from collections import deque 
# stack using list 
stack = ["Amar", "Akbar", "Anthony"] 
stack.append("Ram") 
stack.append("Iqbal") 
print(stack) 

# Removes the last item 
print(stack.pop()) 
print(stack) 
  
# Removes the last item 
print(stack.pop())   
print(stack) 

# Stack using deque 
queue = deque(["Ram", "Tarun", "Asif", "John"]) 
print(queue) 
queue.append("Akbar") 
print(queue) 
queue.append("Birbal") 
print(queue) 
print(queue.pop())                  
print(queue.pop())                  
print(queue) 