# Author: Gichuhi Haron | gichuhiaaron [at] gmail.com
# This scripts renames excel worksheets according to your set headers
# for later merging of individual files
# import pandas and numpy
import pandas as pd
import numpy as np
import glob

# read the files, with different sheets
# pd.read_excel takes 1 mandatory parameter ie the name and location of the spreadsheet
# sheet_name[what sheet to read] and parse_dates=[0] {takes in the column number as array}
# a list of columns that should be read as dates are optional
all_data = pd.DataFrame()
# read all files in a folder with similar naming ie banda1.xlsx, banda2.xlsx ..
for f in glob.glob('test*.xlsx'):
    # read the files using read_excel
    df = pd.read_excel(f)
    # delete the auto assigned using index # ID
    df = df.drop(df.columns[0], axis=1)
    # remove all empty columns
    df.drop(df.iloc[9:])
    # lets rename
    df.columns = ['FULL NAMES', 'CONTACT','NIN', 'OCCUPATION','SUB-COUNTY', 'PARISH','VILLAGE', 'HOUSE SIZE', 'ENTERED BY']
    # lets see the results
    print(df)
    # use append function to append files
    all_data = all_data.append(df, ignore_index=True)
# write the combined data into one file
writer = pd.ExcelWriter('renamed.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1')
writer.save()
