#
# Abdurrahmaan Mohabbat
# 09/12/2022
# Frequency Counter Module
#

def frequencies(alist):
    result = {}
    for listobj in alist:
        if str(listobj) in result:
            result[str(listobj)] += 1
        else:
            result[str(listobj)] = 1
    return result
