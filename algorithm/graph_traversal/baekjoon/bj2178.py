# 240514 미로 탐색(실버1) ✳ 76ms
def solution() :
  import sys
  from collections import deque
  input = sys.stdin.readline

  n, m = map(int, input().split())
  graph = []
  for i in range(n) :
    graph.append(list(input().rstrip()))

  # 숫자로 바꿈
  for i in range(n) :
    for j in range(m) :
      graph[i][j] = int(graph[i][j])

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
      x, y = queue.popleft()
      # 현재 위치에서 상하좌우 확인
      for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        # 위치 벗어나면 무시
        if not (0 <= nx < n and 0 <= ny < m) :
          continue

        # 이동
        if graph[nx][ny] == 1 :
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))

    # 마지막 값 리턴
    return graph[n-1][m-1]
  
  print(bfs(0, 0))