"""
Vector collinear analysis library.
"""


def first_condition(vec_a: list, vec_b: list) -> bool:
    """
    a = n * b.
    """
    if len(vec_a) == len(vec_b):
        factors = []
        for index in range(len(vec_a)):
            factor = vec_a[index] / vec_b[index]
            factors.append(factor)
        if factors.count(factors[0]) == len(factors):
            print('Vectors are collinear')
            return True
        else:
            print('Vectors are not collinear')
            return False
    else:
        print('Size of vector a is not equal to the '
              'size of vector b')
        return False


def second_condition() -> bool:
    """
    ax/bx == ay/by.
    """
    pass


def third_condition() -> bool:
    """
    vec(a*b) == vec(0).
    """
    pass


if __name__ == '__main__':
    a = [3, 5, 16, 21]
    b = [6, 10, 32, 42]
    first_condition(a, b)
