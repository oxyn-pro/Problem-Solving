# The difficulty of the problem is EASY
# Link to the problem: https://www.hackerrank.com/challenges/migratory-birds/problem
# All test cases passed

def catAndMouse(catA, catB, MouseC):
    resA = abs(catA - MouseC)
    resB = abs(catB - MouseC)
    if resA < resB:
        return "Cat A"
    elif resA > resB :
        return "Cat B"
    else:
        return "Mouse C"
      
      
 
