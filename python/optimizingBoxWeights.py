"""
-----Steps to solution-----
NB: If we sort the array, the subset A with maximal total weight is the shortest trailing subarray with sum greater than
    half of the total sum
1. Sort the array
2. Divide the array into two unequal lengths array, where "items in A < items in B"
3. Get the right elements of A, where sum(A) > sum(B): Remember the following points:
    - A and B does not have any item in common
    - The union of A and B must to euql to the original array
4. Return A with the maximal sum
"""

def myfunction(numbers = []):

    print("Sorted array: ", numbers)

    sum_of_array = sum(numbers)
    print("Divide the sum of array by 2 to get the possible values of the element for A: ", sum_of_array / 2)

#     The above line gives us an insight of possible values for A
#     [5,6] => sum = 11 or [6,7] => sum = 13. Hence, B could be either [2,3,7]=> sum=12 or [2,3,5]=> sum=10
#     We can conclude that the correct elements for A is [6, 7] as this is the only condition that meets the
#     requirements stated above

    print("A: ", numbers[3:])

numbers = [3, 7, 5, 6, 2]
numbers.sort()

myfunction(numbers)