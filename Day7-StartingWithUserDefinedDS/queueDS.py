from collections import deque 
# Queue using list 
queue = ["Amar", "Akbar", "Anthony"] 
queue.append("Ram") 
queue.append("Iqbal") 
print(queue) 
  
# Removes the first item 
print(queue.pop(0)) 
print(queue) 
  
# Removes the first item 
print(queue.pop(0)) 
print(queue) 

# Queue using deque 
queue = deque(["Ram", "Tarun", "Asif", "John"]) 
print(queue) 
queue.append("Akbar") 
print(queue) 
queue.append("Birbal") 
print(queue) 
print(queue.popleft())                  
print(queue.popleft())                  
print(queue) 