# colvec - Vector analysis library

ColVec - class for removing collinear vectors from features.

```
toy_set = pandas.DataFrame({
    'Year': [2016, 2017, 2018, 2019, 2020],
    'HarvestArea': [2000, 2000, 2000, 2000, 2000],
    'Harvest': [1000, 1000, 1100, 1200, 1200],
    'Yield': [50, 50, 55, 60, 60]
})

col_vec = ColVec(toy_set)
non_col_vec_dataframe = col_vec.drop_collinear_vectors()
```