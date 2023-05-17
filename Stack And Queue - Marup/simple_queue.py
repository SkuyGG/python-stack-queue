from collections import deque

Queue = deque([1,2,3,4,5])
print("Antrian sekarang : ",Queue)

Queue.append(6)
print("Antrian masuk : ",6)
print("Antrian sekarang : ",Queue)

Queue.append(7)
print("Antrian masuk : ",7)
print("Antrian sekarang : ",Queue)

Out = Queue.popleft()
print("Antrian keluar : ",Out)
print("Antrian sekarang : ",Queue)