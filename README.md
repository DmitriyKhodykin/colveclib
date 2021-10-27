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

Output:
```
Collinear vectors are: ['Harvest', 'Yield']
(Matrix) Rank: 3

Year  HarvestArea  Harvest
0  2016         2000     1000
1  2017         2000     1000
2  2018         2000     1100
3  2019         2000     1200
4  2020         2000     1200
```