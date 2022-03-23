print("Phone Tree")
Phone_queue = []
# Enqueue the following numbers to the Phone_queue
# 535-1332, 132-3452, 123-1989, 208-456-9856
Phone_queue.append('535-1332')
Phone_queue.append('132-3452')
Phone_queue.append('123-1989')
Phone_queue.append('208-456-9856')
# Display the current queue
print("Total Phone Queue:")
print(Phone_queue)
# Dequeue the numbers ensuring that they are 
# dequeued in the order recieved, printing the
# item dequeued each time.
result = Phone_queue.pop()
print(result)
result = Phone_queue.pop()
print(result)
result = Phone_queue.pop()
print(result)
result = Phone_queue.pop()
print(result)