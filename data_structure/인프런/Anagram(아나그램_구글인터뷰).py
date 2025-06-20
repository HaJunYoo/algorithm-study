'''
word1 = input()
word2 = input()

# 문자열을 forloop 돌면서 딕셔너리 val 값을 증가시킬 것
word1_uq = list(set(list(word1)))
word2_uq = list(set(list(word2)))

word1_dict = dict()
word2_dict = dict()

for elem in word1_uq:
    word1_dict[elem] = 0

for elem in word2_uq:
    word2_dict[elem] = 0

for key in word1:
    word1_dict[key] += 1

for key in word2:
    word2_dict[key] += 1

if word1_dict == word2_dict:
    print('YES')
else :
    print('NO')

'''

a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")