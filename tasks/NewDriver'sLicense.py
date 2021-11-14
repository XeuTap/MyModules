def timetowait(queue, target, agents):
    order_time = 20
    while len(queue) >= agents:
        for visitor in range(1, agents+1):
            if queue_list.pop(0) == target:
                return order_time
        order_time += 20
    return order_time


target = 'Eric'
agents = 2
queue = 'Adam Caroline Rebecca Frank'
queue_list = queue.split(' ')
queue_list.append(target)
queue_list.sort()
answ = timetowait(queue_list, target, agents)
print(answ)