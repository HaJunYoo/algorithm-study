
if __name__ == '__main__':
    string = input()

    res = 1
    string_list = list(string)
    if len(list(set(string))) == 1:
        print(0)
        # print(set(string))

    else:
        for i in range(len(string)-1):
            if string[i] != string[i+1]:
                res+=1
        
        res //= 2
        print(res)
        
    