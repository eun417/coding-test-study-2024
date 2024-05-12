# 240512 N과 M (2)(실버3) 🅾 44ms
def solution() :
  n, m = map(int, input().split())
  arr = []

  def back(c) :
    if len(arr) == m  :
      print(" ".join(map(str, arr)))
      return

    for i in range(c, n + 1) :
      if i not in arr:
        arr.append(i)
        back(c)
        arr.pop()
      c += 1

  back(1)