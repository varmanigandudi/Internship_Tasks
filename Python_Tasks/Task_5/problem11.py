#11.Text Wrap
#https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    new_lst = ""
    for i in range(0, len(string), max_width):
        new_lst += string[i:i + max_width] + "\n"

    return new_lst.rstrip("\n")
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
