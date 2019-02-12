def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    else:
        result = base
        for i in range(exp-1):
            result *= base
        return result


print(iterPower(3,3))