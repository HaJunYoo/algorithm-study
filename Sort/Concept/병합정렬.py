def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2
        Dsort(lt, mid)  # 왼쪽 정렬
        Dsort(mid + 1, rt)  # 오른쪽 정렬
        p1 = lt
        p2 = mid + 1
        tmp = []
        # 합치는 부분
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
            # 왼쪽 파트가 남았을 때 tmp 리스트에 왼쪽 파트를 추가
        if p1 <= mid: tmp = tmp + arr[p1:mid + 1]
        # 오른쪽 파트가 남았을 때, tmp 리스트에 오른 쪽 파트를 추가
        if p2 < rt: tmp = tmp + arr[p2:rt + 1]
        # tmp를 arr에 복사 붙여넣기
        for i in range(len(tmp)):
            arr[lt + i] = tmp[i]


if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before sort : ", end='')
    print(arr)
    Dsort(0, 7)
    print()
    print("After sort : ", end='')
    print(arr)
