import pandas as pd
import numpy as np

""" Series from lists """
country = ['India','USA','UK','Nepal']
print(pd.Series(country))

""" Integers """
runs = [11,23,50,69,78,100]
print(pd.Series(runs))

""" Custom Index """
marks = [67,57,85,100]
subjects = ['maths','english','science','hindi']
print(pd.Series(marks))
print(pd.Series(marks, index=subjects))

""" Setting a name """
print(pd.Series(marks,index=subjects,name="xyz's marks"))

""" Series from dict """
marks ={
    'maths': 67,
    'english':57,
    'science':89,
    'hindi':100 
}
marks_series = pd.Series(marks,name="xyz's marks")
print(marks_series)

""" Series Attributes """
## Size
print(marks_series.size)

## dtype
print(marks_series.dtype)

## Name
print(marks_series.name)

## is_unique """IMP"""
print(marks_series.is_unique)

print(pd.Series([1,1,2,3,4,5]).is_unique)

## index ##
