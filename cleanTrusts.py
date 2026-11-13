import pandas as pd
import openpyxl
import csv
import xlrd
from pathlib import Path

#the trusts file is protected so can't read it directly as a pandas dataframe

import win32com.client 
excel = win32com.client.Dispatch('Excel.Application')

filePath = Path("trusts.xls").resolve()
wb = excel.Workbooks.open(str(filePath))

#can't extract the sheet names here, so manually just listing the sheet names
sheets = ['0607', '0708', '0809']
year = 2007

for sheetName in sheets:

    sheet = wb.Worksheets(sheetName)

    df = pd.DataFrame(sheet.usedRange())
    trustNames = df.iloc[4:215,0]
    orgCodes = df.iloc[4:215,1]
    supplies = df.iloc[4:215, 9]
    transport = df.iloc[4:215, 12]
    staffCosts = df.iloc[4:215, 8]
    debt = df.iloc[4:215, 14]
    totalCosts = df.iloc[4:215, 23]
    #print(trustNames)

    entries = pd.DataFrame({
        "name": trustNames.values,
        "orgCode": orgCodes.values,
        "supplies": supplies.values,
        "transport": transport.values,
        "staffCosts" : staffCosts.values,
        "debt" : debt.values,
        "totalCosts" : totalCosts.values
    })

    clean = entries.dropna() #getting rid of empty cells
    clean.to_csv('trusts.csv' , mode = 'a', header=True, index=False)

#print(clean.head())
