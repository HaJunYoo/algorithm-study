
if __name__ == '__main__':
    sent = input()
    
    res = 0
    
    stack = list()
    stack.append('+')
    number = list()
   
    temp = []
    for elem in sent:
        if elem in ['+', '-']:
            number.append(int(''.join(temp)))
            stack.append(elem)
            temp = []
        else:
            temp.append(elem)
    else:
        number.append(int(''.join(temp)))
        
    # print(stack)
    # print(number)
    
    temp = 0
    res = 0
    while stack:
        # print(res)
        cal = stack.pop()
        
        if cal == '+':
            num = number.pop()
            temp += num
            
            # print('temp:',temp)
        else:
            num = number.pop()
            temp += num
            res -= temp
            temp = 0
    

    if temp > 0:
        res += temp
    
    print(res)
            
            
            