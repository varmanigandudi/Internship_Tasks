#12.Capitalize!
#https://www.hackerrank.com/challenges/capitalize/problem



def solve(s):
    s1=s.title().strip()
    return s1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
