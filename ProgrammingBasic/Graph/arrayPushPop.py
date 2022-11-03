queue = [0]

queue.append(1)
queue.append(2)
queue.append(3)

print(queue[0])
print(queue.pop(0))
print(queue.pop(-1))

print(queue.pop())

print(queue)


print (1 in (1,3))


array = [0,1,2,3,4,5]

print('range')

for item in range(1,len(array)):
    print(item)