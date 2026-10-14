#Find the Runner-Up Score!
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maximum=float('-inf')
    second_maximum=float('-inf')
    for i in arr:
        if i>maximum:
            second_maximum=maximum
            maximum=i
        elif i>second_maximum and maximum!=i:
            second_maximum=i
    print(second_maximum)
