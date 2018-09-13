def checkio(data: list) -> list:
    rtrn = list()
    for x in data:
        if data.count(x) > 1:
            rtrn.append(x)
    return rtrn


def tests():
    print(checkio([1, 2, 3, 1, 3]))
    print(checkio([1, 2, 3, 4, 5]))
    print(checkio([5, 5, 5, 5, 5]))
    print(checkio([10, 9, 10, 10, 9, 8]))

tests()
