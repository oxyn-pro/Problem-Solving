# This question was asked in Google coding interview.

# I found 2 ways of solving it:

# 1 way:
# O(n^2) Time Complexity - squared. 
# All test cases passed

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
k = int(input())

def sum_of_two(lst1, lst2):
    """Add two nums from two arrays so that sum of two must
       be equal to required number"""
    for i in lst1:
        for j in lst2:
            if i + j == k:
                print(True)
sum_of_two(lst1, lst2)
# It has pretty bad optimization, it means that we can optimize ever more


# 2 way:
# O(n) Time Complexity - linear. 
# All test cases passed

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
k = int(input())

def sum_of_two(lst1, lst2):
    """Add two nums from two arrays so that sum of two must
       be equal to required number"""
    nums = []
    for i in lst1:
        nums.append(k-i)
    
    for j in lst2:
        if j in nums:
            print(True)
sum_of_two(lst1, lst2)
# it is more or less optimized
