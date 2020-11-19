def is_len_1(mstr):
    return True if len(mstr) > 6 else False


def is_len_2(mstr):
    if len(mstr) > 6:
        return True
    else:
        return False


def is_len_3(mstr):
    # 这里注意false和true的位置
    return [False, True][len(mstr) > 6]
