# Read excel files
import pandas as pd
import numpy as np
import glob
from remove_characters import remove_characters
# read the files, with different sheets
# pd.read_excel takes 1 mandatory parameter ie the name and location of the spreadsheet
# sheet_name[what sheet to read] and parse_dates=[0] {takes in the column number as array}
# a list of columns that should be read as dates are optional
all_data = pd.DataFrame()
# read all files in a folder with similar naming ie banda1.xlsx, banda2.xlsx ..
for f in glob.glob('MBUYA*.xlsx'):
    # read the files using read_excel
    df = pd.read_excel(f)
    # lets see the results
    #print(df)
    # try to remove * characters from the data frame
    remove_characters(df)
    # lets see the results
    #print(df)
    # use append function to append files
    all_data = all_data.append(df, ignore_index=True)
# write the combined data into one file
writer = pd.ExcelWriter('myCollected_mbuya.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1')
writer.save()
#banda_supply = pd.read_excel("BANDA_16_17_18.xlsx", sheet_name="Sheet1")
# try printing the data frame
#print(banda_supply)
