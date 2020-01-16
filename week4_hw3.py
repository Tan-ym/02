HW_SOURCE_FILE = 'hw03.py'

if __name__ == '__main__':


#############
# Questions #
#############

def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if n == 0:
        return 0
    else:
        return num_sevens(n // 10) + (lambda k: 1 if n % 10 == 7 else 0)(n)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    """
    def helper(result, i, direction):
        """
                Keep track of the current value of the sequence.
                :param result: the current value of the sequence
                :param i: counter
                :param direction: determines the current value plus or minus one
         """    
        if i % 7 == 0 or num_sevens(i) >= 1:
            return helper(result - direction, i + 1, -direction)
        else:
            return helper(result + direction, i + 1, direction)
    return helper(1, 1, 1)
    return pingpong(n)
    """
    def direction(n):
        """ Determines the current value plus or minus one. """
        if n < 7:
           return 1
        elif n % 7 == 0 or num_sevens(n) > 1:
          return -1 * direction(n - 1)
        return direction(n - 1)
    if n <= 7:
        return n
    return direction(n) + pingpong(n - 1)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    
    """
    def top_coins_size(i):
        """ Find the maximum size of the coins. """
        if i > amount:
            i = i // 2
        return top_coins_size(i * 2)
        """

    def helper(amount, s):
        """
                Keep track of the partitions of the denomination of the coins.
                :param amount: the sum of the values of the coins
                :param s: the smallest size of the coins
         """
        if amount == 0:
            return 1
        elif amount < s:
            return 0
        else:
            return helper(amount - s, s) + helper(amount, s * 2)
        return helper(amount, 1)

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    if not lst is None:
        return []
    else type(lst) == list:
        return flatten(lst)

###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 0:
        print_move(start, end)
    else:
        remainder = 2 * 3 - start - end
        print_move(start, remainder)
        move_stack(n - 1, start, remainder)
        print_move(remainder, end)

from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    #return lambda n, f: n if n == 1 else f(n,mul(f, sub(n, 1)))
    def fact(x):
        """Return the value of an expression that computes factorial."""
        if x == 1:
            return x
        return fact(x-1) * x



