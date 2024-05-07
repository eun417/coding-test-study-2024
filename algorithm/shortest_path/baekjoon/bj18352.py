# 240507 특정 거리의 도시 찾기(실버2) ✳ 2828ms
def solution() :
  import heapq
  import sys
  input = sys.stdin.readline

  n, m, k, x = map(int, input().split())
  graph = [[] for i in range(n + 1)]
  distance = [int(1e9)] * (n + 1)
  distance[x] = 0  # 출발 도시에서 출발 도시로 가는 최단 거리

  for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append((b, 1))  # a에서 b로 가기 위한 비용 1

  q = []
  heapq.heappush(q, (0, x))

  while q :
    dist, now = heapq.heappop(q)
    for i in graph[now] :
      cost = dist + i[1]

      # 이미 처리된 적 있는 노드 무시
      if distance[now] < dist :
        continue

      # 현재 노드와 연결된 다른 인접한 노드들을 확인
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  # 최단 거리가 k인 도시 번호 리스트
  result = []

  # 결과 출력
  for i in range(n + 1) :
    if distance[i] == k :
      result.append(i)
      print(i)
    else :
      if i == n and len(result) == 0 :
        print(-1)