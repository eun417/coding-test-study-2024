# 240504 로프(실버4) 🅾 124ms
def solution() :
  import sys
  input = sys.stdin.readline

  n = int(input())  # 로프 개수
  rw = []
  for _ in range(n) :
    rw.append(int(input()))  # 각 로프의 최대 중량
  rw.sort()  # 정렬

  # 임의로 로프를 골라서 사용할 수 있으므로 
  # 각각의 값 비교해서 최대 중량 알아냄
  w = []
  for i in range(n) :
    w.append(rw[i] * (n-i))
  
  print(max(w))