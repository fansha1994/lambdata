""" lambda - collection of data science helper functions
"""


import pandas as pd
import numpy as np


TEST = pd.DataFrame(np.ones(10))


def df_cleaner(df):
    """clean a dataframe!"""
    pass # TODO - implement

def is_null(df):
    isnull = df.is_null.any(axis=1).sum()
    return print('There is {is_null} values in this DataSet')


def tts(X,y):
    # import libraries that i need 
    from sklearn.model_selection import train_test_split
    #build the code
    tts = train_test_split(X,y)
    return tts