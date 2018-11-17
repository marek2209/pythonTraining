
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])



def unique_in_order(iterable):
    char_seen = []

    for char in iterable:

        if char not in str(iterable):
            char_seen.append(char)


    print char_seen


#
# If you only want to check for the presence of abc in any string in the list, you could try
#
# some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
# if any("abc" in s for s in some_list):
#     # whatever
# If you really want to get all the items containing abc, use
#
# matching = [s for s in some_list if "abc" in s]



unique_in_order("AAAABBBCCDAABBB")
