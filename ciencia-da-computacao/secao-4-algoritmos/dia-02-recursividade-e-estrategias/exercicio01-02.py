def count_pair(n):  # Não recursivo
    list = []
    for e in range(1, n + 1):
        if e % 2 == 0:
            list.append(e)
    return f"{list} ---> {len(list)}"


def count_pair_rec(n):
    list = []
    if n % 2 == 0:
        list.append(n)
    if n == 1:
        return list
    return count_pair_rec(n - 1) + list


def count_pair_num(n):
    pair = 0
    if n % 2 == 0:
        pair += 1
    if n == 1:
        return pair
    return count_pair_num(n - 1) + pair


print(count_pair_rec(10))
print(count_pair_num(10))
