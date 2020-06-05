# This script separates multiple excel sheets in a single files
# author: Haron Gichuhi #gichuhiaaron@gmail.com # 2 june 2020
import os, collections, csv
import pandas as pd
import numpy as np
from os.path import basename

# create an empty data frame array
all_data = pd.DataFrame()
# define the file path of the excel files
file = "banda1.xlsx"
# check the number of sheets
number_of_sheets = 3
for i in range(1, number_of_sheets+1):
    #omit the header column
    data = pd.read_excel(file, sheet_name='Sheet'+str(i))
    df.append(data, ignore_index=True)
# save the sheets into one files
output_file = "merged_banda1.xlsx"
df = pd.concat(df)
df.to_excel(output_file)
