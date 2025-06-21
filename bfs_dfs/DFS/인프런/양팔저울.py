import sys
sys.stdin = open('in5.txt', 'r')

candid = []
# index 0부터 시작
def dfs(index, w_s):
    method = (+1, -1, 0)

    if index == len(weights):
        if w_s <= 0:
            return
        else:
            if w_s not in candid:
                candid.append(w_s)
            return

    for m in method:
        n_s = w_s + (m * weights[index])
        dfs(index + 1, n_s)


if __name__ == "__main__":
    k = int(input())
    weights = list(map(int, input().split()))

    dfs(0, 0)
    candid = list(set(candid))
    # candid.sort()
    # print(candid)
    print(sum(weights) - len(candid))

