# 240513 돌 게임(실버5) 🅾 44ms
def solution1() :
  n = int(input())
  if n % 2 == 0 :
    print('CY')
  else : 
    print('SK')

def solution2() :
  N = int(input())

  # dp = [0 for i in range(N)]
  # dp = [0] * N
  dp = [0] * (1000 + 1)

  dp[1] = 1
  dp[2] = 2
  dp[3] = 1

  for n in range(4, N+1):
      dp[n] = min(dp[n-1], dp[n-3]) + 1

  if dp[N] % 2 == 1:
      print('SK')
  else:
      print('CY')