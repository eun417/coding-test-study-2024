# 240504 알바생 강호(실버4) 🅾 96ms
def solution() :
  import sys
  input = sys.stdin.readline

  n = int(input())  # 사람 수
  t = []
  for _ in range(n) :
    t.append(int(input()))  # 팁
  t.sort(reverse=True)  # 정렬

  result = 0
  for i in range(n) :
    tmp = t[i] - i
    if tmp > 0 :  # 양수만 포함
      result += tmp

  print(result)