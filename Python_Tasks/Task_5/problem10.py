#10.Swap Case
#https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    new_word = ""

    for ch in s:
        if ch == ch.lower():
            new_word += ch.upper()
        else:
            new_word += ch.lower()

    return new_word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

