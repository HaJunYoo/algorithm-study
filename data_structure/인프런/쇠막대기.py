string = input()

stack = list()

res = 0

for i in string :
    if i == "(" :
        stack.append(i)

    else :
        if i == ")" :
            stack.pop()
            res += len(stack)
        else :
            stack.pop()
            res+=1

print(res)