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





















