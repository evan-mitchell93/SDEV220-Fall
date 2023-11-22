def test_my_func(opt):
    """
    >>> (0 <= test_my_func(0) < 1)
    True
    >>> x = test_my_func(1)
    >>> int(x) == x
    True
    """
    print(vars())
    import my_mod
    if opt == 0:
        return my_mod.my_num()
    else:
        return my_mod.my_int()

if __name__ == "__main__":
    import doctest
    doctest.testmod()