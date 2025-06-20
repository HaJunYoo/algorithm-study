string = input()

stack = list()

operator = ('+', '-', '*', '/', '(', ')')


def operation(elem, num1, num2):
    result = 0

    if elem == '+' :
        result = num1 + num2
    elif elem == '-' :
        result = num1 - num2
    elif elem == '*' :
        result = num1 * num2
    elif elem == '/' :
        result = num1 // num2

    return result


for elem in string :
    if elem.isdecimal() :
        stack.append(int(elem))

    if (elem in operator) and (len(stack) > 1) :
        num2 = stack.pop()
        num1 = stack.pop()

        # operator 변환해주는 함수가 있다면 좋을텐데
        number = operation(elem, num1, num2)
        stack.append(number)

# 남아있는 stack 원소를 print 한다
print(stack[0])


