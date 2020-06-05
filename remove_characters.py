import pandas as pd
import numpy as np

def remove_characters(df):
    # define the column to sanitize
    column_to_sanitize = ["CONTACT"]
    # print out the column #CONTACT
    #print(column_to_sanitize)
    df = df.replace({' -':''}, inplace = True, regex=True)
