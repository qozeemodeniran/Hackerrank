# Initialize month variable to be zero
month = 0
# stockPrice = [1, 3, 2, 4, 5]
change = max(stockPrice)

# Create list to hold values
l = []
total_sum = 0
for i in range(len(stockPrice)):
    total_sum += stockPrice[i]

left = 0
left_sum = 0

while (len(stockPrice) > 1):
    left = stockPrice.pop(0)
    l.append(left)

    # Now calculate the average
    left_sum += left
    avg1 = left_sum // len(l)
    avg2 = (total_sum - left_sum) // len(stockPrice)

    if(abs(avg1 - avg2))