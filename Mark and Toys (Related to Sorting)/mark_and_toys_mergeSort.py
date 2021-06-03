# In this problem, i implemented the code by using the merge sort, 
# as you may know the merge sort is one of the fastest and efficient sorting algorithms,
# that has O(n log n) time complexity, space complexity O(n log n). 
# In this, "Mark and Toys" the Complexity Analysis is the same as the usual merge sort which means:
# O(n log n) Time Complexity, Space complexity - O(n log n).  Because n log n + n = 2n log n which means O(n log n) 

# The problem description is: https://www.hackerrank.com/challenges/mark-and-toys/problem
# All test cases passed

# Merge sort algorithm, in order to sort
def merge_sort(lst): 
    if len(lst)<= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        
        sorted_l = []
        left_idx = right_idx = 0
        len_left = len(left)
        len_right = len(right)
        while left_idx < len_left and right_idx < len_right:
            if left[left_idx] < right[right_idx]:
                sorted_l.append(left[left_idx])
                left_idx += 1
            else:
                sorted_l.append(right[right_idx])
                right_idx += 1
        sorted_l += left[left_idx:]
        sorted_l += right[right_idx:] 
        return sorted_l

def maximumToys(prices, k):
    # Write your code here
    la = merge_sort(prices)  # calling merge sort and storing the list into "la" var

    count = 0
    total = 0
    for i in la:
        if i <= k:           # Iterating over the sequence of vals inside of the list, and find the less values than k
            count += 1
            k-= i
        else:
            break
    return count 
