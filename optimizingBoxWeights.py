from itertools import accumulate

def minimalHeaviestSet(arr):

    split_length = [2, 3]

    splitted = [arr[x-y: x] for x, y in zip(
        accumulate(split_length), split_length)]

    print(splitted)

numbers = [3, 7, 5, 6, 2]

minimalHeaviestSet(numbers)