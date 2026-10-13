'''Q1. Find the Frequency of Each Word in a Sentence
Write a Python program to count how many times each word appears in a given sentence and store the result in a dictionary.
Example Input:
python is easy and python is powerful
Expected Output:
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}'''
#program
#Q1

def frequency(sen):
    sen=sen.split()
    new_dict={}
    for word in sen:
     count=sen.count(word)
     new_dict[word]=count
    return new_dict


'''Q2. Find the Frequency of Each Character in a Word
Write a Python program to count how many times each character appears in a given word and store the result in a dictionary.
Example Input:
banana
Expected Output:
{'b': 1, 'a': 3, 'n': 2}'''
#program
def freq_ch(word):
   new_dict={}
   for ch in word:
      count=word.count(ch)
      new_dict[ch]=count
   return new_dict

'''Q3. Find the First Non-Repeating Character in a Word
Write a Python program to find the first character that appears only once in a given word. If no such character exists, return None.
Example Input:
swiss
Expected Output:
w'''
#program
def non_repeating(word):
   for ch in word:
      count=word.count(ch)
      if count==1:
         break
   return ch

'''Q4. Check Whether Two Strings Are Anagrams
Write a Python program to check whether two strings are anagrams.
Two strings are anagrams if they contain the same characters with the same frequencies, regardless of their order.
Example Input:
s1 = "listen"
s2 = "silent"
Expected Output:
True
'''
#program
def anagram(s1,s2):
   s1=s1.lower()
   s2=s2.lower()
   if sorted(s1)==sorted(s2) and len(s1)==len(s2):
      return True
   else:
      return False

'''Q5. Find the First Repeating Character in a String
Write a Python program to find the first character whose second occurrence is encountered while reading the string from left to right.
If no character repeats, return None.
Example Input:
programming
Expected Output:
r
'''
#Program
def repeating(word):
   for ch in word:
      count=word.count(ch)
      if count>1:
         break
   return ch

'''Q6. Move All Zeros to the End of a List
Write a Python program to move all zeros to the end of a list while maintaining the original order of non-zero elements.
Example Input:
[0, 3, 0, 1, 2, 0, 4]
Expected Output:
[3, 1, 2, 4, 0, 0, 0]
'''
def zeros(nums):
   zeros=[]
   non_zeros=[]
   for i in nums:
      if i==0:
         zeros.append(i)
      else:
         non_zeros.append(i)
   return  non_zeros + zeros

'''Q7. Find the Second Highest Distinct Number in a List
Write a Python program to find the second-largest distinct number in a given list.
Duplicate values should not be considered separate ranks.
If a second distinct number does not exist, return None.
Example Input:
[10, 20, 40, 30, 40, 20]
Expected Output:
30
'''
#Program
def second_highest(nums):
   highest=0
   second_highest=0
   for i in nums:
      if i>highest:
         second_highest=highest
         highest=i
      elif i>second_highest and highest!=i:
         second_highest=i
   return second_highest

'''Q8. Remove Duplicates Without Changing the Original Order
Write a Python program to remove duplicate elements from a list while preserving the order of their first occurrence.
Example Input:
[4, 2, 4, 5, 2, 7, 5]
Expected Output:
[4, 2, 5, 7]
'''
def duplicates(numbers):
    seen=[]
    dup=[]
    for i in numbers:
        if i not in seen:
            seen.append(i)
        else:
            if i not in dup:
                dup.append(i)
    return seen

'''Q9. Find the Missing Number from 1 to N
Write a Python program to find the missing number in a list containing numbers from 1 to N.
The list contains exactly one missing number, and all remaining numbers appear only once.
Example Input:
nums = [1, 2, 4, 5, 6]
N = 6
Expected Output:
3
'''
#Program
def missing_number(lst):
   for i in range(1,len(lst)):
      if i not in lst:
         return i


'''Q10. Find Two Numbers Whose Sum Equals a Target
Write a Python program to find the first pair of numbers whose sum equals a given target.
Return the pair as a list. If no valid pair exists, return an empty list.
Return the pair whose second element is encountered earliest when scanning the input from left to right. If multiple earlier elements qualify, choose the earliest one.
Example Input:
nums = [2, 7, 11, 15]
target = 9
Expected Output:
[2, 7]
'''
def sum(nums):
   target=9
   for i in range(len(nums)):
      for j in range(i+1,len(nums)):
         num_sum=nums[i]+nums[j]
         if num_sum==target:
            return [nums[i],nums[j]]
   return []

'''Q11. Find the Number Closest to Zero
Write a Python program to find the number closest to zero in a given list.
If two numbers are equally close to zero, return the positive number.
Example Input:
[-8, -3, 2, 5, -2]
Expected Output:
2
'''
def closest_zero(lst):
   nearest_number=float('inf')
   for i in lst:
      if abs(i)<abs(nearest_number):
         nearest_number=i
      elif abs(i)==abs(nearest_number) and i>nearest_number:
         nearest_number=i
   return nearest_number

'''Q12. Find Common Elements Between Two Lists
Write a Python program to find the common elements between two lists.
Each common element should appear only once in the result, maintaining the order of its first occurrence in the first list.
Example Input:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
Expected Output:
[3, 4, 5]
'''
#program
def common_elemnts(lst1,lst2):
   lst1=set(lst1)
   lst2=set(lst2)
   return list(lst1.intersection(lst2))

'''Q13. Rotate a List to the Right by K Positions
Write a Python program to rotate the elements of a list to the right by K positions.
Elements shifted beyond the last position should move to the beginning of the list.
Example Input:
nums = [1, 2, 3, 4, 5]
K = 2
Expected Output:
[4, 5, 1, 2, 3]
'''
def rotate_positions(nums):
   k=2
   for i in nums:
      result=nums[-k:]+nums[:-k]
      return result

'''Q14. Find the Maximum Sum of Two Consecutive Elements
Write a Python program to find the maximum sum of any two consecutive elements in a list.
Assume the list contains at least two elements.
Example Input:
[4, 7, 2, 9, 5]
Expected Output:
14
'''
def maximum_sum(lst):
   max_sum=0
   for i in range(len(lst)-1):
      for j in range(i+1,i+2):
         total=lst[i]+lst[j]
         if total>max_sum:
            max_sum=total
   return max_sum

'''Q15. Find All Pairs of Numbers Whose Sum Equals a Target
Write a Python program to find all unique pairs of numbers whose sum equals a given target.
Each pair should contain two distinct list positions, and duplicate pairs should not be included.
Return each pair in ascending numerical order. Return the list of pairs sorted by their first element. If no valid pairs exist, return an empty list.
Example Input:
nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
Expected Output:
[[1, 8], [2, 7], [4, 5]]
'''
#program
def num_pairs(lst):
   target=9
   pairs=[]
   for i in range(len(lst)):
      for j in range(i+1,len(lst)):
         sum=lst[i]+lst[j]
         if sum==target:
            pairs.append([[lst[i],lst[j]]])
   return pairs
         