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
marks_series = pd.Series(marks)
print(marks_series)