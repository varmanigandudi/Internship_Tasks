#problem14:Set .add()
#https://www.hackerrank.com/challenges/py-set-add/problem

n=int(input())
set1=set()
for i in range(n):
    country=input( )
    set1.add(country)
print(len(set1))
