"""
Vector collinear analysis library.
"""
import pandas


def main(data: pandas.DataFrame) -> pandas.DataFrame:
    """
    Remove collinear vectors and return non-collinear features.
    :param data: incoming dataset
    :return: outgoing dataset
    """
    columns: list = list(data.columns)
    collinear_vectors_name: list = []
    for index_a in columns:
        for index_b in columns:
            if index_a != index_b:  # Only unique pairs
                vector_a = list(data[index_a])
                vector_b = list(data[index_b])

                # Сollinearity check
                if first_condition(vector_a, vector_b):
                    collinear_vectors_name.append(index_a)
            else:
                pass

    print('Collinear vectors are:', collinear_vectors_name)

    # Remove unnecessary vectors from the list
    non_collinear_vector = collinear_vectors_name[0]
    for vector in collinear_vectors_name:
        columns.remove(vector)
    columns.append(non_collinear_vector)

    # Filter out non-collinear features
    non_collinear_dataframe = data[columns]
    print('(Matrix) Rank:', len(non_collinear_dataframe.columns))
    print(non_collinear_dataframe)
    return non_collinear_dataframe


def first_condition(vec_a: list, vec_b: list) -> bool:
    """
    Collinearity check: vec(a) = n * vec(b).
    :param vec_a: list with n elements
    :param vec_b: list with n elements
    :return: True - lists are collinear
    """
    # Element-wise division of vector coordinates
    if len(vec_a) == len(vec_b):
        factors = []
        for index in range(len(vec_a)):
            try:
                factor = round(vec_a[index] / vec_b[index], 2)
                factors.append(factor)
            except ZeroDivisionError:
                factor = 0
                factors.append(factor)
        # If the ratio of the coordinates is the same - True
        if factors.count(factors[0]) == len(factors):
            return True
        else:
            return False
    else:
        print('Size of vector a is not equal to the '
              'size of vector b')
        return False


if __name__ == '__main__':
    dataframe = pandas.DataFrame({
        'distance': [100, 120, 200, 250, 400],
        'mean_speed': [50, 50, 45, 48, 42],
        'truck_type': [1, 0, 1, 1, 0],
        'consumption': [10, 11, 20, 25, 39],
        'cost': [20, 22, 40, 50, 78]
    })
    main(dataframe)
