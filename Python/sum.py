def sum(lst, n):
    sum_total = 0
    for item in lst:
        sum_total += item
    if sum_total == n:
        return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
