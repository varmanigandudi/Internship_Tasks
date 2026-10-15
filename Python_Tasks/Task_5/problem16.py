#16.Collections.Counter()
#https://www.hackerrank.com/challenges/collections-counter/problem



from collections import Counter

x = int(input())                        # number of shoes
sizes = Counter(map(int, input().split()))
n = int(input())                        # number of customers

total = 0
for _ in range(n):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        total += price
        sizes[size] -= 1

print(total)
