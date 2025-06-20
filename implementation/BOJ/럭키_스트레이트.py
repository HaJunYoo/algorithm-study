
if __name__ == '__main__':
    n = int(input())
    string_arr = list(int(num) for num in str(n))
    length = len(string_arr)
    # print(string_arr[:length//2])
    # print(string_arr[length//2:])
    arr1 = string_arr[:length//2]
    arr2 = string_arr[length//2:]
    
    if sum(arr1) == sum(arr2):
        print("LUCKY")
    else:
        print("READY")
    