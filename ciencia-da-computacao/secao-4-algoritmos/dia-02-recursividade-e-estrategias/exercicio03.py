def max_div_comum(n1, n2):
    div = 2
    while n1 > div < n2:
        if n1 % div == 0 and n2 % div == 0:
            return div * max_div_comum(n1 / div, n2 / div)
        else:
            div += 1
    return 1


print(max_div_comum(30, 24))


def max_div_comm(n1, n2):  # 1 1
    result = 1
    x1 = n1
    x2 = n2
    div = 2
    while x1 > 1:
        if x1 % div == 0:
            x1 = x1 / div
            if x2 % div == 0:
                x2 = x2 / div
                result *= div
        else:
            div += 1
    return result


# print(max_div_comm(30, 24))
