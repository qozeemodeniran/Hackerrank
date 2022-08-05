def myArray(*arr):
    rows, cols = (1, 1)
    myArr = [[arr] * cols] * rows
    count_1 = myArr.count(1)
    print(type(myArr))
    # print(count_1)
myArray(1,1,2,3,3)
