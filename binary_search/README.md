# 이진 탐색 Binary Search

![스크린샷 2022-05-20 오후 6.06.12.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3b41ca57-c756-4889-ab4b-66975012cd36/스크린샷_2022-05-20_오후_6.06.12.png)

1. 첫번째 방법은 처음부터 끝까지 하나씩 살펴보면서 보는 방법 → 선형 탐색
2. 탐색 범위에 포함되지 않는 내용인 절반 씩 날릴 수 있게 된다
    1. romeo와 juliet은 r로 시작하기 때문에 반절인 y ~ z는 날려버린다
    2. 이렇게 절반 씩 재귀 방식으로 날리면 언젠가 타겟(줄리오와 로미엣)을 찾는다

**예시**

- 술게임 Up & Down
    - 타겟 번호을 맞출 때까지 예상되는 번호를 불러 타겟 번호가 예상 번호보다 위에 있는지 아래에 있는지 답변을 이끌어내어 up an down 방식으로 탐색 범위를 점점 좁혀간다

- 탐색 전에 반드시 정렬이 되어 있어야 한다
    - 정렬이 되어 있다는 전제 하에 반을 배제 하고 탐색을 진행할 수 있는 것
- 살펴보는 범위를 절반씩 줄여가면서 답을 찾는다

- 정렬 O(NlogN) + 이진탐색 O(logN) → 결과적으로 O(NlogN)
    - 이진 탐색은 정확하게 말하면 O($log_2{N)}$
- 미리 정렬되어 들어오면 이진탐색만 하면 되므로 O(logN)
- 하지만 선형 탐색의 경우 O(N) ⇒ 경우에 따라서는 이진 탐색보다 선형 탐색이 더 좋을 때가 있다
    - 어떤 일차원 배열 내의 원소를 찾는다 ⇒ 원소를 찾는 행위를 한 번만 하고 끝나는 경우 ⇒ 선형 탐색이 유리
    - 하지만 원소를 여러 번(N번) 찾아야할 경우(탐색을 여러 번 해야할 경우)
        - 선형 탐색 ⇒ N * O(N) → O(N^2)
        - 이진 탐색 ⇒ NlogN(정렬) + N번 * logN(이진 탐색) ⇒ O(NlogN)

### 라이브러리

### [Python] bisect_left/right

![스크린샷 2022-05-23 오후 7.26.21.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4985ae1d-3b7c-4319-b89a-43801b5dae11/스크린샷_2022-05-23_오후_7.26.21.png)

```python
from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
# 4 - 2 = 2
three = bisect_right(v, 3) - bisect_left(v, 3)
# 0
four = bisect_right(v, 4) - bisect_left(v, 4)
# 7 - 4 = 3
six = bisect_right(v, 6) - bisect_left(v, 6)

# bisect_right(v, num)는 target num의 바로 오른쪽에 있는 값의 인덱스 반환
# bisect_left(v, num)는 target num의 바로 가장 왼쪽에 있는 값의 인덱스 반환 
```

### Parametric Search

> **매개변수 탐색**
> 

- 최적화 문제를 결정 문제로 바꿔서 이진탐색으로 푸는 방법이다
- 최적화 문제 Optimization Problem
    - 문제 상황을 만족하는 변수의 최솟값, 최댓값을 구하는 문제
- 결정 문제 Decision Problem
    - Yes / No Problem
    
    Q.수강생들의 외모값과 커플/솔로여부가 주어진다。
    커플들은 솔로들보다 외모값이높다。외모값이 최소 몇 이상일 때부터 커플인가？
    
    선형 탐색의 경우 → 앞에서부터 하나씩 True인 값을 찾아가면서 인덱스 4의 True를 만난 후 6을 반환
    
    
    이진 탐색
    
    가운데 →  W모 회원:  True : 6
    
    왼쪽에서 가운데 → Y모 회원 : False : 5
    
    W모 회원과 Y모 회원의 절반 ⇒ K모 회원 : True : 6 
    
    → False 다음으로 나온 최초의 True 값이 6
    
    ⇒ 고로 답은 6
    
    ### Parmetric Search
    
    - 매개변수가 주어지면  `True` or `False`가 결정되어야 한다
    - 가능한 해의 영역이 `연속적`이어야 한다
    - 범위를 반씩 줄여가면서 가운데 값이 True인지 False 인지 구한다
    - 이진 탐색과 똑같은 원리
        
        
    
    [[boj.kr](http://boj.kr) 2512](https://www.notion.so/boj-kr-2512-935ac9b1a2514bd8bdeb7c497039e55b)