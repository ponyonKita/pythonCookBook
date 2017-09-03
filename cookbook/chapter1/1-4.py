

# N아이템의 최대 혹은 최소값 찾기

import heapq

nums = [1,38, 2, 23, 7, -4, 18, 23, 37, 2]
print(heapq.nlargest(1, nums)) # 앞의 숫자는 갯수
print(heapq.nsmallest(2, nums))

print(list(nums))
# 제일 첫번째 요소가 제일 작음
print(heapq.heapify(nums))
# 작은순서되로 pop 기능
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))
portfolio = [
    {'name':'IBM', 'shares':100, 'price':91.1},
{'name':'AAPL', 'shares':50, 'price':543.3},
{'name':'FB', 'shares':200, 'price':21.9},
{'name':'HPQ', 'shares':35, 'price':31.75},
{'name':'YHOO', 'shares':45, 'price':16.35}
]

cheap = heapq.nsmallest(1, portfolio, key=lambda s:s['price'])
expencive = heapq.nlargest(1, portfolio, key=lambda s:s['price'])
print(cheap)
print(expencive)