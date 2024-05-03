# 240503 숫자 카드(실버5) 🅾 1876ms
def solution() :
  def binary_search(array, target) :
    start = 0
    end = n - 1

    while start <= end :
      mid = (start + end) // 2

      if array[mid] == target :
        return mid
      elif array[mid] > target :
        end = mid - 1
      else :
        start = mid + 1
    return None
  
  import sys
  input = sys.stdin.readline

  # 숫자 카드
  n = int(input())  
  n_card = list(map(int, input().split()))
  n_card.sort()  # 정렬
  
  # 정수
  m = int(input())  
  m_num = list(map(int, input().split()))

  for i in m_num :
    result = binary_search(n_card, i)
    if result == None :
      print(0, end=' ')
    else :
      print(1, end=' ')