# Test.assert_equals(get_middle("test"),"es")
# Test.assert_equals(get_middle("testing"),"t")
# Test.assert_equals(get_middle("middle"),"dd")
# Test.assert_equals(get_middle("A"),"A")
# Test.assert_equals(get_middle("of"),"of")


stringToGetMiddle = "test"

def get_middle(stringToGetMiddle):
    stringList = list(stringToGetMiddle)
    listCount = stringList.__len__()

    if (listCount % 2 != 0):
        print stringList[listCount/2]
    else:
        print stringList[(listCount/2) - 1] + stringList[listCount/2]

get_middle(stringToGetMiddle)



