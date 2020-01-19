if __name__ == '__main__':
    def filtered_accumulate(combiner, base, pred, n, term):
        """Return the result of combining the terms in a sequence of N terms
        that satisfy the predicate pred. combiner is a two-argument function.
        If v1, v2, ..., vk are the values in term(1), term(2), ..., term(N)
        that satisfy pred, then the result is
             base combiner v1 combiner v2 ... combiner vk
        (treating combiner as if it were a binary operator, like +). The
        implementation uses accumulate.

        >>> filtered_accumulate(add, 0, lambda x: True, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
        15
        >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
        11
        >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
        9
        >>> filtered_accumulate(mul, 1, greater_than_5, 5, square)  # 1 * 9 * 16 * 25
        3600
        >>> # Do not use while/for loops or recursion
        >>> from construct_check import check
        >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
        ...       ['While', 'For', 'Recursion'])
        True
        """

        def combine_if(x, y)
                if pred(y):
                    return combiner(x, y)
                else:
                    return x

        return accumulate(combine_if, base, n, term)


    def odd(x):
        return x % 2 == 1


    def greater_than_5(x):
        return x > 5