def isAllNums(s):
    if len(s) == 0:
        return True
    else:
        if s[0].isdigit():
            return isAllNums(s[1:])
        else:
            return False


def isAllNumsPositive(lst):
    if len(lst) == 0:
        return True
    else:
        lastIdx = len(lst) - 1
        if lst[lastIdx] > 0:
            lst.pop()
            return isAllNumsPositive(lst)
        else:
            return False
