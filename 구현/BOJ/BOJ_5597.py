student = [False]*31

for _ in range(28):
    idx = int(input())
    student[idx] = True

n_sub = []
for i in range(1, 31):
    if not student[i]:
        n_sub.append(i)

n_sub.sort()
# print(n_sub)
for elem in n_sub:
    print(elem)