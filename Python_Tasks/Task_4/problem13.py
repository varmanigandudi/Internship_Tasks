#problem12:Symmetric Difference
https://www.hackerrank.com/challenges/symmetric-difference/problem

m=int(input())
set1=set(map(int,input().split()))
n=int(input())
set2=set(map(int,input().split()))
result=sorted(set1^set2)
print(*result,sep='\n')
