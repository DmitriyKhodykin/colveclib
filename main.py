"""
Vector analysis library.
ColVec - class for removing collinear vectors from features.
"""
import pandas


class ColVec:

    toy_set = pandas.DataFrame({
        'Year': [2016, 2017, 2018, 2019, 2020],
        'HarvestArea': [2000, 2000, 2000, 2000, 2000],
        'Harvest': [1000, 1000, 1100, 1200, 1200],
        'Yield': [50, 50, 55, 60, 60]
    })

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def main(self) -> pandas.DataFrame:
        """
        Remove collinear vectors and return non-collinear features.
        :return: outgoing dataframe
        """
        columns: list = list(self.dataframe.columns)
        collinear_vectors_name: list = []
        for index_a in columns:
            for index_b in columns:
                if index_a != index_b:  # Only unique pairs
                    vector_a = list(self.dataframe[index_a])
                    vector_b = list(self.dataframe[index_b])

                    # Сollinearity check
                    if self.first_condition(vector_a, vector_b):
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
        non_collinear_dataframe = self.dataframe[columns]
        print('(Matrix) Rank:', len(non_collinear_dataframe.columns))
        print(non_collinear_dataframe)
        return non_collinear_dataframe

    def first_condition(self, vec_a: list, vec_b: list) -> bool:
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
    pass
