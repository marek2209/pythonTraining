#For example, if this array were passed as an argument:

#["Telescopes", "Glasses", "Eyes", "Monocles"]
#Your function would return the following array:

#["Eyes", "Glasses", "Monocles", "Telescopes"]
#All of the strings in the array passed to your function will be different lengths,
# so you will not have to decide how to order multiple strings of the same length.


arr = ["Telescopes", "Glasses", "Eyes", "Monocles"]
arrSorted = []

def sort_by_length(arr):
    arrSorted = sorted(arr, key=len)
    return arrSorted

sort_by_length(arr)
