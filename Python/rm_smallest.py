def rm_smallest(d):
    dict_vals = set()
    first_time = True
    smallest_term = 0
    for key in d:
        dict_vals.add(d[key])
    for element in dict_vals:
        if first_time == True:
            smallest_term = element
            first_time = False
        elif element < smallest_term:
            smallest_term = element
    for value in d:
        if d[value] == smallest_term:
            d.pop(value)
            return d
    return d;

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
