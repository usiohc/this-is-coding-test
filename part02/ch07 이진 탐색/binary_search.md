# 이진 탐색
### 범위를 반씩 좁혀가는 탐색

<br>

## 순차 탐색
#### 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인

보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.    
리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소를 찾을 수 있다는 장점이 있다.

    def sequential_search(n, target, array):
        for i in range(n):
        if array[i] == target:
            return i + 1
    
    print('생성할 원소 개수, 찾을 문자열을 입력')
    input_data = input().split()
    n = int(input_data[0])
    target = input_data[1]

    print("앞서 적은 원소 개수 만큼 문자열을 입력")
    array = input().split()

    print(sequential_search(n, target, array))


### 순차 탐색의 시간 복잡도

문자열이 몇 번째 데이터인지 출력해주는데, 순차 탐색은 정렬 여부와 상관없이 가장 앞의 원소부터 하나씩 확인한다.    
따라서 데이터의 개수가 N개일 때 최대 N번의 비교 연산이 필요하므로 순차 탐색의 최악의 경우 시간 복잡도는 O(N)이다.


<br>

## 이진 탐색 : 반으로 쪼개면서 탐색하기
#### 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.    
데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 특징이 있다.    

이진 탐색을 구현하는 방법에는 2가지가 있는데 하나는 재귀 함수를 이용하는 방법이고, 다른 하나는 반복문을 이용하는 방법이 있다.


#### 재귀 함수 소스코드

    def binary_search(array, target, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        # 찾은 경우
        if array[mid] == target:
            return mid
        # mid 보다 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            return binary_search(array, target, start, mid-1)
        # 큰 경우 오른쪽 확인
        else:
            return binary_search(array, target, mid+1, end)
        
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, n-1)
    if result == None:
        print('원소가 존재하지 않습니다.')
    else:
        print(result + 1)

<br>

#### 반복문 소스코드

    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2

            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return None

    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, n - 1)
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)

<br>

### 이진 탐색 시간 복잡도

코딩 테스트의 이진 탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많음.    
따라서 탐색 범위가 2,000만을 넘어가면 이진 탐색으로 접근해봐야함.    
처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 **O(log N)** 의 속도를 내는 알고리즘을 떠올려야 함

<br>

## 이진 탐색 트리

트리 자료구조 중에서 가장 간단한 형태가 이진 탐색 트리이다.    
이진 탐색 트리란 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조

- 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드

위 조건이 성립한다면 이진 탐색 트리라고 할 수 있다.


#

### 부품 찾기

재귀 함수를 사용 안하고 반복문으로 해결함    
간단하게 검색하고자 하는 리스트를 sort해주면 입력값마다 이진 탐색을 진행하게 했음

