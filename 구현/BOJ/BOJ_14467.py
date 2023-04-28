# if __name__ == '__main__':

n = int(input())
cow_location = dict()
change_location_num = 0
change_list = []
for _ in range(n):
    change_list.append(tuple(map(int, input().split())))

for change in change_list:
    cow_num, location = change

    cur_location = cow_location.get(cow_num, location)
    # print(cur_location)

    if cur_location != location:
        change_location_num += 1
        cow_location[cow_num] = location
        
    else:
        cow_location[cow_num] = location

# print()
print(change_location_num)


'''
8
10 1
10 0
6 0
2 1
4 1
3 0
4 0
10 1
'''