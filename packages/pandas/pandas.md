Reference:
- https://pandas.pydata.org/

Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.

Pandas (Python Data Analysis Library) is not precisely a machine learning library, but it is widely used in the machine learning community. It boasts many benefits, most of which are related to the fact that in pandas, your data has labels. In other words, your data is tabular. You can do many SQL-like operations on it or some linear algebraic ones, like let’s say, using NumPy. The labels and data come in an R-style data frame, which makes it easier to get into for developers familiar with that language. Another benefit of pandas is its good I/O capabilities – data can be easily pulled into (and extracted from) your pandas data frame.

Its main (and best) use case is data wrangling (sometimes referred to as data munging), that is processing and transforming raw data from one format into another for analytical purposes.


Pandas is built on the NumPy library and written in languages like Python, Cython, and C. In Pandas, we can import data from various file formats like JSON, SQL, Microsoft Excel, etc.

``` python
# Importing pandas library
import pandas as pd

# Creating and initializing a nested list
age = [['Aman', 95.5, "Male"], ['Sunny', 65.7, "Female"],
       ['Monty', 85.1, "Male"], ['toni', 75.4, "Male"]]

# Creating a pandas dataframe
df = pd.DataFrame(age, columns=['Name', 'Marks', 'Gender'])

# Printing dataframe
df
```

output

```
    Name    Marks    Gender
0    Aman    95.5    Male
1    Sunny    65.7    Female
2    Monty    85.1    Male
3    toni    75.4    Male
```


# Pandas vs NumPy  
| **Pandas**                                                                          | **NumPy** |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | 
| When we have to work on **Tabular data**, we prefer the pandas module.                 | When we have to work on **Numerical data**, we prefer the NumPy module.             |
| The powerful tools of pandas are **DataFrame and Series.**                             | Whereas the powerful tool of NumPy is **Arrays.**                                   |
| Pandas consume **more** **memory**.                                                    | Numpy is **memory efficient.**                                                      |
| Pandas have a better performance when the number of rows is **500K or more.**          | Numpy has a better performance when number of rows is **50K or less.**              |
| Indexing of the Pandas series is **very slow** as compared to Numpy arrays.            | Indexing of Numpy arrays is **very fast.**<br>                                      |
| Pandas have a 2D table object called **DataFrame.**                                    | Numpy is capable of providing **multi-dimensional arrays.**                         |
| It was developed by **Wes McKinney** and was released in **2008**.                     | It was developed by **Travis Oliphant** and was released in **2005.**               |
| It is used in a lot of organizations like Kaidee, Trivago, Abeja Inc., and a lot more. | It is being used in organizations like Walmart Tokopedia, Instacart, and many more. |
| It has a higher industry application.                                                  | It has a lower industry application.                                                |