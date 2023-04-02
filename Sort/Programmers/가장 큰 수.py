# from itertools import permutations
# numbers = [3, 300, 310, 340, 370, 5, 9]
#
# arr = []
# num_list = []
# for num in numbers:
#     temp = str(num)
#     arr.append(temp)
#     num_list.append(temp[0])
#
# print(arr)
#
# num_list = set(num_list)
# num_list = list(num_list)
#
# num_dict = dict()
#
# for num in num_list:
#     num_dict[num] = []
#
# print(num_dict)
#
# for elem in arr:
#     temp = elem[0]
#     num_dict[temp].append(elem)
#
# print(num_dict)
# ans = []
# for key, value in num_dict.items():
#     array = value
#     array.sort(key=lambda x: (x[::-1]), reverse=True)
#     # for comb in permutations(array, len(array)):
#     #     new = list(comb)
#     #     new = ''.join(new)
#     #     comb_list.append(int(new))
#     print(array)
#     new = ''.join(array)
#     # temp = max(comb_list)
#     ans.append(new)
#
# print(ans)
#
# for idx, a in enumerate(ans):
#     ans[idx] = str(a)
#
# ans.sort(key = lambda x: (int(x[0])), reverse=True)
# print(ans)
# ans = ''.join(ans)
# print(ans)
#
list = [3,300,31,387]
list.sort(key= lambda x: (str(x)*3)[:4], reverse=True)
print(list)

