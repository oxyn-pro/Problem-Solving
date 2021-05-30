# In this problem, i implemented the code by using the merge sort, 
# as you may know the merge sort is one of the fastest and efficient sorting algorithms,
# that has O(n log n) time complexity, space complexity O(n log n). 
# In this, Merge-Sort Inversion Counter, the Complexity Analysis is the same as the usual merge sort which means:
# O(n log n) Time Complexity, Space complexity - O(n log n). 

def countInversions(arr):            
    total_inv = 0     # Var to count the inversions
    if len(arr) <= 1:     # Creating a Base-case in order to check the list length (the eventually stop the recursive call)
        return arr, 0         
    else:
        mid = int(len(arr) / 2)   # Getting the middle val in order to recursively loop

        left, left_inv = countInversions(arr[:mid])      # Assigning both vals to variables
        right, right_inv = countInversions(arr[mid:])
        
        left_idx = 0
        right_idx = 0
        sorted_l = []
        len_left = len(left)
        len_right = len(right)
        
        while left_idx < len_left and right_idx < len_right:      #Check in order to loop through the len of the list/array 
            if left[left_idx] <= right[right_idx]:
                sorted_l.append(left[left_idx])
                left_idx += 1
            else:
                sorted_l.append(right[right_idx])
                right_idx += 1
                total_inv += len_left - left_idx
                

        sorted_l += left[left_idx:]       # Concatinating left vals (from merge sort) to the list 
        sorted_l += right[right_idx:]
        
        return sorted_l, total_inv + left_inv + right_inv   # Returning sorted list/array along with total number of inversions

# Check statement: 

# if __name__ == "__main__":                         
#     print(countInversions(arr))
