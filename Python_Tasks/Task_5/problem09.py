#9.Word Order
#https://www.hackerrank.com/challenges/word-order/problem
num=int(input())
new_dict={}
for i in range(num):
    word=input()
    if word not in new_dict:
        new_dict[word]=1
    else:
        new_dict[word]+=1
print(len(new_dict))
for i in new_dict.values():
    print(i,end=" ")

