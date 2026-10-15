#13.Nested Lists
#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students=[]
    lowest=float('inf')
    second_lowest=float('inf')
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        if score < lowest:
            second_lowest = lowest
            lowest = score
        elif lowest < score < second_lowest:
            second_lowest = score
    names = sorted(s[0] for s in students if s[1] == second_lowest)
    for n in names:
        print(n)

