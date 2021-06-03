# There is a second way to solve the same problem using a quicksort algorithm.
# The problem with using quicksort in this task is that it is less efficient than the merge sort algorithm,
# which means that its time complexity changes depending on the specific size / length of the input, whereas in merge sort it remains the same (or constant).

def quick_sort(prices):
    if len(prices) <= 1:
        return prices
    else:
        pivot = prices[0]
        low = []
        great = []
        for i in prices[1:]:
            if i < pivot:
                low.append(i)
            elif i > pivot:
                great.append(i)
        return quick_sort(low) + [pivot] + quick_sort(great)
      
def maximumToys(prices, k):
    # Write your code here
    la = merge_sort(prices)

    count = 0
    total = 0
    for i in la:
        if i <= k:
            count += 1
            k-= i
        else:
            break
    return count 
