
import pandas as pd
import numpy as np

data= pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'labels': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']})

#######  -  LOC = Accede a Filas y Columnas por Nombres
#######  -  ILOC = Accede a Filas y Columnas por Numeros

### M A P ###  
# METHOD = IS A POWERFUL TOOL BECAUSE CAN           || Map in Python is a function that works as an iterator to return a result after
# CONVERT A CATEGORICAL VALUES INTO CONTINOUS VALUES|| Applying a function to every item of an iterable (tuple, lists, etc.). It is used when
# Applies a function to each single element of      || You want to apply a single transformation function to all the iterable elements.
# the series, but it needs two arguments            || The iterable and function are passed as arguments to the map in Python
                                                
'''data['qualify'] = data['qualify'].map({'yes': 1, 'no': 0})
print(data)'''


### A P P L Y ### 
# METHOD = Apply a function along an axis of the DataFrame.
# Objects passed to the function are Series objects whose index is either the DataFrame’s index (axis=0) or the DataFrame’s columns (axis=1).
# By default (result_type=None), the final return type is inferred from the return type of the applied function.
# Otherwise, it depends on the result_type argument.

# The apply() method allows you to apply a function along one of the axis of the DataFrame, default 0, which is the index (row) axis.

# Pandas.apply allow the users to pass a function and apply it on every single value of the Pandas series. 
# It comes as a huge improvement for the pandas library as this function helps to segregate data according to 
# the conditions required due to which it is efficiently used in data science and machine learning.

'''data['name_len'] = data['name'].apply(len)
print(data.loc[0:4, ['name','name_len']])'''

'''
def get_element(list, position):
    return list[position]
data.name.str.split(',').apply(get_element, position = 0)
'''

### APPLYMAP ### METHOD = It can change the whole DF because it loops through both axis that means it change every/each element of the DF
# and the parameters are passed like in the apply method

'''.apply(float)'''

### L A M B D A ####
# METHOD = A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
# Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the 
# def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 






### F I L T E R ####
# The filter() function takes two arguments: function - a function iterable - an iterable like sets, lists, tuples etc.
# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.


### F O R  LOOPS  IN  ONE  CODE  LINE ####


