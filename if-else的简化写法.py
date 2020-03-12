def isLen_1(strString):
    return True if len(strString) > 6 else False


def isLen_2(strString):
    if len(strString) > 6:
        return True
    else:
        return False


def isLen_3(strString):
    # 这里注意false和true的位置
    return [False, True][len(strString) > 6]
