"""
Vector collinear analysis library.
"""
import pandas


def main(dataframe: pandas.DataFrame) -> list:
    columns: pandas.index = dataframe.columns
    result = []
    for index_a in columns:
        for index_b in columns:
            if index_a != index_b:
                vector_a = list(dataframe[index_a])
                vector_b = list(dataframe[index_b])
                if first_condition(vector_a, vector_b):
                    result.append(index_a)
            else:
                pass
    return result


def first_condition(vec_a: list, vec_b: list) -> bool:
    """
    a = n * b.
    """
    if len(vec_a) == len(vec_b):
        factors = []
        for index in range(len(vec_a)):
            try:
                factor = round(vec_a[index] / vec_b[index], 3)
                factors.append(factor)
            except ZeroDivisionError:
                factor = 0
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


if __name__ == '__main__':
    a = [3, 5, 16, 10]
    b = [6, 10, 32, 20]
