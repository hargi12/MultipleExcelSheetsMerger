# Author: Gichuhi Haron | gichuhiaaron [at] gmail.com
# use this script to clean your data. You can adapt it to any data column
import pandas as pd
import numpy as np

def remove_characters(df):
    # define the column to sanitize
    column_to_sanitize = ["CONTACT"]
    # print out the column #CONTACT
    #print(column_to_sanitize)
    df = df.replace({' -':''}, inplace = True, regex=True)
