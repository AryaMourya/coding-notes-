import pandas as pd
import numpy as np

""" Series from lists """
country = ['India','USA','UK','Nepal']
print(pd.Series(country))

""" Integers """
runs = [11,23,50,69,78,100]
runs_series = pd.Series(runs)

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
print(marks_series.index)

print(runs_series.index)

print(type(runs_series.index))

## values ##
print(marks_series.values)

""" Series using read_csv """

## with one col
 
df = pd.read_csv(r'c:\Users\lenovo\coding-notes-\python notes\cvs-file\subs.csv')
print(type(df))
print(df)
subs=pd.read_csv(r'c:\Users\lenovo\coding-notes-\python notes\cvs-file\subs.csv').squeeze("columns")
print(type(subs))
print(subs)

## with 2 cols
second = pd.read_csv(r'C:\Users\lenovo\coding-notes-\python notes\cvs-file\kohli_ipl.csv')
print(second)
second_runs = pd.read_csv(r'C:\Users\lenovo\coding-notes-\python notes\cvs-file\kohli_ipl.csv',index_col='match_no').squeeze('columns')
print(second_runs)

movies = pd.read_csv(r'C:\Users\lenovo\coding-notes-\python notes\cvs-file\bollywood.csv')
print(movies)
movies_1 = pd.read_csv(r'C:\Users\lenovo\coding-notes-\python notes\cvs-file\bollywood.csv',index_col='movie').squeeze('columns')
print(movies_1)