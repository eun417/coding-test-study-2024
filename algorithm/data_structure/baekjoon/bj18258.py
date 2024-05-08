# 240508 큐 2(실버4) 🅾 1784ms
def solution() :
  from collections import deque
  import sys
  input = sys.stdin.readline
  
  n = int(input())  # 명령의 수
  
  queue = deque()
  for i in range(n) :
    c = input().split()
    s = c[0]
    
    if s == 'push' :
      queue.append(int(c[1]))
    elif s == 'pop' :
      if queue :
        print(queue.popleft())
      else :
        print(-1)
    elif s == 'size' :
      print(len(queue))
    elif s == 'empty' :
      if queue :
        print(0)
      else :
        print(1)
    elif s == 'front' :
      if queue : 
        print(queue[0])
      else :
        print(-1)
    elif s == 'back' :
      if queue :
        print(queue[-1])
      else :
        print(-1)