from queue import Queue, LifoQueue

q = Queue()
for i in range(5):
	q.put(i)

while not q.empty():
	print(q.get())

print('------')

qq = LifoQueue()
for i in range(6,10):
	qq.put(i)
while not qq.empty():
	print(qq.get())