# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#
# If the input array is empty or null, return an empty array.
#
# Example
#
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].



arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arrInfo =[]
def count_positives_sum_negatives(arr):
    negativesSum = 0
    zeroSum = sum(x == 0 for x in arr)
    if len(arr) == 0:
        return arrInfo
    for element in arr:
        if element < 0 :
            negativesSum = negativesSum + element

    positivesSum = sum(x > 0 for x in arr)

    if positivesSum > 0:
        arrInfo.append(positivesSum)
        arrInfo.append(negativesSum)


    return arrInfo

count_positives_sum_negatives(arr)



