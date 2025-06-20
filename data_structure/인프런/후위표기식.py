operator = ("+", "-", "*", "/")
close = ("(", ")" )

num = input()

n = len(num)

print(num)
answer = ''
stack = list()
for elem in num:
    if elem.isdecimal():
        answer += elem

    else :
        if elem == "(" :
            stack.append(elem)
        elif elem == "*" or elem == "/" :
            while stack and (stack[-1] == "*" or stack[-1] == "/") :
                answer += stack.pop()
            stack.append(elem)
        elif elem =="+" or elem == "-" :
            while stack and stack[-1]!="(" :
                answer += stack.pop()
            stack.append(elem)

        elif elem ==")" :
            while stack and stack[-1] != "(" :
                answer += stack.pop()

            stack.pop()

while stack :
    answer += stack.pop()

print(answer)