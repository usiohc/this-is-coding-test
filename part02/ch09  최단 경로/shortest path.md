# 최단 경로 (Shortest Path)
### 가장 짧은 경로를 찾는 알고리즘

한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우, 모든 지점에서 다른 모든 지점까지의 최단 겨올를 모두 구해야 하는 경우 등 사례에 맞는 알고리즘이 정립되어 있음.

최단 경로 문제는 보통 그래프를 이용해 표현, 각 지점은 그래프에서 **노드**로 표현되고 지점간 연결된 도로는 **간선**으로 표현

보통 테스트에서는 최단거리만 출력하는 문제가 많음


## 다익스트라, 플로이드 워셜만 다룸

<br>

## 다익스트라 최단 경로 알고리즘

그래프에서 여러개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘


음의 간선이 없을때 정삭적으로 동작
음의 간선이란, 0보다 작은 값을 가지는 간선을 의미하는데 현실 세계의 길은 음의 간선으로 표현되지 않으므로 실제 GPS 소프트웨어의 기본 알고리즘으로 채택되곤 한다.

기본적으로 그리디 알고리즘으로 분류 되는데 매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복하기 때문이다.

1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3과 4를 반복

'각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장하며 리스트를 계혹 갱신한다는 특징이 있음

매번 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인함

현재 처리하고 있는 노드와 인접한 노드로 도달하는 더짧은 경로를 찾으면 '더 짧은 경로도 있었네?' 라고 판단하며 갱신하는 것임

<br>


#### 9-1 간단한 다익스트라 알고리즘 소스코드

    import sys
    input = sys.stdin.readline
    INF = int(1e9)

    # 노드의 개수, 간선의 개수
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF] * (n+1)

    for _ in range(m):
        a,b,c = map(int, input().split())
        # a번 노드에서 b번으로 가는 비용이 c
        graph[a].append((b, c))

    # 방문하지 않은 노드 중에서 가장 최단거리가 짦은 노드의 번호를 반환
    def get_smallest_node():
        min_value = INF
        index = 0 # 최단 거리가 짧은 노드의 번호를 반환
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                main_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        # 시작 노드 초기화
        distance[start] = 0
        visited[start] = True
        for i in graph[start]:
            distance[j[0]] = j[1]
        
        # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        for i in range(n-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
            now = get_smallest_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    #시작 
    dijkstra(start)

    for i in range(1, n+1):
        # 도달할 수 없는 경우, 무한(INF)라고 출력
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])



간단한 다익스트라 알고리즘은 **O(V<sup>2</sup>)** 의 시간복잡도를 가짐

총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색 해야 함.
최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 해결 가능하지만 10,000를 넘어간다면 해결하기 어려움.

#

## 개선된 다익스트라 알고리즘

개선된 알고리즘은 최악의 경우에도 시간 복잡도 **O(E log V)**를 보장한다.
v는 노드의 개수이고 E는 간선의 개수이다

간단한 다익스트라 알고리즘은 '최단 거리가 가장 짧은 노드'를 찾기 위해서 매번 최단 거리 테이블을 선형적으로 탐색해야 했는데,
이 과정에서만 O(V)의 시간이 걸렸다.

하지만 선형적으로 찾는 것이 아니라 더욱더 빠르게 찾을 수 있다면 시간 복잡도를 더 줄일 수 있을 것이다.

개선된 다익스트라 알고리즘에서는 **힙 (Heap)** 자료구조를 사용한다.

힙 자료구조를 이용하게 되면 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

이 과정에서 선형 시간이 아닌 로그 시간이 걸린다.
N = 1,000,000일 떄, log<sub>2</sub>N이 약 20인 것을 감안하면 속도가 획기적으로 빨라지는 것임을 이해할 수 있다.

### 힙 (Heap)

힙 자료구조는 우선순위 큐 (Priority Queue)를 구현하기 위하여 사용하는 자료구조 중 하나이다.

ch 05에서 DFS, BFS를 공부할 때 스택과 큐의 원리에 대해 공부했는데, 큐는 선입 선출의 데이터를 삭제했지만 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제 한다는 점이 특징이다. 

스택, 큐, 우선순위 큐 자료구조를 비교한 내용은 다음과 같다.

|자료구조| 추출되는 데이터|
|--------|---------|
|스택(Stack)| 가장 나중에 삽입된 데이터|
|큐(Queue)| 가장 먼저 삽입된 데이터|
|우선순위 큐(Priority Queue)| 가장 우선순위가 높은 데이터|

이러한 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 떄 사용한다.

또한 우선순위 큐를 구현할 떄는 내부적으로 최소 힙 혹은 최대 힙을 이용한다.

최소힙을 이용하는 경우 '값이 낮은 데이터가 먼저 삭제', 최대 힙을 이용하는 경우 '값이 큰 데이터가 먼저 삭제'

heapq는 기본적으로 최소 힙 구조를 이용하는데 우선순위에 해당하는 값에 - 음수 부호를 붙여서 넣으면 최대 힙으로 사용 가능하다.

| 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
|---|---|---|
| 리스트 | O(1) | O(N) |
| 힙 | O(log N) | O(log N) |

데이터릐 개수가  N개일 때, 힙 자료구조에 N개의 데이터를 모두 넣은 뒤에 다시 모든 데이터를 꺼낸다고 가정.

삽입할 때는 N번 반복 O(N log N), 삭제할 때에도 N 번 반복 O(N log N)     
따라서 O(N log N)이 될 것이다.

<br>

#### 9-2 개선된 다익스트라 알고리즘 소스코드

    import heapq
    import sys
    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heapqpush(q, (cost, i[0]))

    dijkstra(start)

    for i in range(1, n+1):
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])

개선도니 다익스트라 알고리즘의 시간 복잡도는 O(E log V)로 훨씬 빠르다.

한번 처리된 노드는 더이상 처리되지 않는다. 다시 말해서 노드를 하나씩 꺼내 검사하는 반복문은 노드의 개수 V 이상의 횟수로는 반복되지 않는다.      
또한 V번 반복될 때 마다 각각 자신과 연결된 간선들을 모두 확인한다. 따라서 '현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드을을 확인; 하는 총 횟수는 총 최대 간선의 개수 (E) 만큼 연산이 수행될 수 있다.


<br>

---

## 플로이드 워셜 알고리즘










