# In this problem, i implemented the code by using the slicing technique
# it has O(n^2) time complexity, it is not the fastest algorithm to work with 2d arrays (aka matrices), but can still work quite efficiently with large datasets.

# The problem description is: https://www.hackerrank.com/challenges/2d-array/problem
# All test cases passed

emp = []
for i in range(6):
    usIn = list(map(int, input().split()))
    emp.append(usIn)

def hourglassSum(emp):
    a = len(emp)
    b = len(emp)
    ma =-1000000
    len_emp = len(emp)
    if a < 3 and b < 3:
        return -1
    for i in range(0, a - 2):
        for j in range(0, b - 2):
            suma = (emp[i][j] + emp[i][j+1] + emp[i][j+2]) + (emp[i + 1][j+1]) + (emp[i+2][j] + emp[i+2][j+1] + emp[i+2][j+2])

            if suma  > ma:
                ma = suma
            else:
                continue
    return ma
  
# Check Statement:
#   Input: 
#   1 1 1 0 0 0
#   0 1 0 0 0 0
#   1 1 1 0 0 0
#   0 0 2 4 4 0
#   0 0 0 2 0 0
#   0 0 1 2 4 0

# Output should be:
# 19
