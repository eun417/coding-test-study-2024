# 240502 DFS와 BFS(실버2) ✳ 72ms
def solution() :
  import sys
  from collections import deque

  input = sys.stdin.readline
  
  n, m, v = map(int, input().split())  # n:정점 개수, m:간선 개수, v:시작 번호
  
  # 그래프
  graph = [[] for i in range(n + 1)]  
  
  for _ in range(m) :
    a, b = map(int, input().split())
    # 양방향 간선 처리
    graph[a].append(b)
    graph[b].append(a)
  
  # 정렬
  for i in graph :
    i.sort()
  
  def dfs(graph, v, visited) :
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')  # 방문한 순서대로 노드 출력
  
    for i in graph[v] :
      if not visited[i] :
        dfs(graph, i, visited)
  
  def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
      num = queue.popleft()
      print(num, end=' ')
  
      # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[num] :
        if not visited[i] :
          queue.append(i)
          visited[i] = True

  #함수 호출
  visited = [False] * (n+1)
  dfs(graph, v, visited)
  print()
  visited = [False] * (n+1)
  bfs(graph, v, visited)