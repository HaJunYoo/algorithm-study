'''
## [문제]
각 자리가 숫자(0부터 9)로만 이루어진 string S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0 + 2) x 9) x 8) x 4) = 576입니다.
또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

- 입력
첫째 줄에 여러 개의 숫자로 구성된 하나의 string S가 주어집니다. (1 <= S의 길이 <= 20)

- 출력
첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.
```python
예제 입력 1

02984

예제 출력 1

576
```
'''

## DFS 방식의 brute_force

string = input()
num_list = [int(x) for x in string]
print(num_list)
n = len(num_list)

max_num = 0

def dfs(num, sum):

    global max_num
    # print(f'{num}, {sum}')

    # 인덱스 끝에 도달했을 때
    if num == n-1:
        if max_num < sum :
            max_num = sum
            print(f'경우의 수 : {sum}')

    else :
        temp = num_list[num+1]
        # 만약 두 수 중에서 하나라도 1보다 작거나 같다면 더하기 수행
        if temp <= 1 or num_list[num] <= 1:
            # 더한다
            dfs(num + 1, sum + temp)

        else :
            # 곱한다
            dfs(num+1, sum * temp)
            # 더한다
            dfs(num+1, sum + temp)


dfs(0, num_list[0])
print(max_num)


########## 단순 그리디 풀이

string = input()
num_list = [int(x) for x in string]
print(num_list)
n = len(num_list)

max_num = 0

def dfs(num, sum):

    global max_num
    # print(f'{num}, {sum}')

    # 인덱스 끝에 도달했을 때
    if num == n-1:
        if max_num < sum :
            max_num = sum
            print(f'경우의 수 : {sum}')

    else :
        temp = num_list[num+1]
        # 만약 두 수 중에서 하나라도 1보다 작거나 같다면 더하기 수행
        if temp <= 1 or num_list[num] <= 1:
            # 곱한다
            dfs(num + 1, sum + temp)

        else :
            # 곱한다
            dfs(num+1, sum * temp)
            # 더한다
            dfs(num+1, sum + temp)


dfs(0, num_list[0])
print(max_num)