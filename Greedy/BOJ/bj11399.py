n = int(input())

pi = map(int, input().split())

persons = [(idx, person) for idx, person in enumerate(pi)]

persons = sorted(persons, key=lambda x: x[1])
print(persons)

times = list()
time = 0

for person in persons :
    time += person[1]
    times.append(time)

print(sum(times))




