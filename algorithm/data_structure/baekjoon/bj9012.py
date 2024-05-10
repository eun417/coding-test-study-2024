# 240510 괄호(실버4) ❎ 
def solution1() :
  t = int(input())
  for _ in range(t) :
    s = input()
    while '()' in s :
      s  = s.replace('()', '')
    if len(s) == 0 :
      print('YES')
    else :
      print('NO')

# Stack
def solution2() :
  t = int(input())
  for _ in range(t):
      stk = []
      s = input()
      isVPS = True

      for ch in s:
          if ch == '(':
              stk.append('(')
          if ch == ')':
              if stk:
                  stk.pop()
              elif not stk:
                  isVPS = False
                  break
      if not stk and isVPS:
          print('YES')
      elif stk or not isVPS:
          print('NO')