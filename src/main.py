#Got to Read an Excel file
import pandas as pd
import openpyxl

dataframe = pd.read_excel('../Resources/OEC2021_-_School_Record_Book_.xlsx')
print(dataframe)