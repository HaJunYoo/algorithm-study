import heapq
from collections import deque


def multiply_minus(num):
    return -1 * num


def make_max_heap(heap):
    temp = [-num for num in heap]
    heapq.heapify(temp)
    heapq.heappop(temp)
    return list(map(multiply_minus, temp))


def make_min_heap(heap):
    heapq.heapify(heap)
    heapq.heappop(heap)
    return list(heap)


def return_min(heap):
    heapq.heapify(heap)
    return heapq.heappop(heap)


def return_max(heap):
    temp = [-num for num in heap]
    heapq.heapify(temp)
    return -1 * heapq.heappop(temp)


def solution(operations):
    heap = []
    operations = deque(operations)
    while operations:
        # print(heap)
        op = operations.popleft()
        if op.startswith('I'):
            heap.append(int(op.split(' ')[-1]))
        else:
            if not heap:
                # print('heap empty')
                continue
            if int(op.split(' ')[-1]) > 0:
                heap = make_max_heap(heap)
            elif int(op.split(' ')[-1]) <= 0:
                heap = make_min_heap(heap)
            else:
                continue

    if heap:
        return [return_max(heap), return_min(heap)]
    else:
        return [0, 0]