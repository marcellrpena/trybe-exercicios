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
    new_list = count_pair_rec(n - 1) + list
    return new_list


print(count_pair_rec(10))
