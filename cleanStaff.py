import pandas as pd
import openpyxl
import csv

file = pd.ExcelFile('nhsStaff.xlsx')
sheetNames = file.sheet_names
headers = True

for sheet in sheetNames:
    print(sheet)
    df = pd.read_excel(file, sheet)
    regionName = df.iloc[4,0]
    dates = df.iloc[5, 2:82]
    dateVals = dates.astype(str).str.split("-")
    years = dateVals.str[0]
    months = dateVals.str[1]
    print(years)
    headcounts = df.iloc[7, 2:82]
    doctors = df.iloc[11, 2:82]
    studentDoctors = df.iloc[17, 2:82]
    nurses = df.iloc[24, 2:82]
    ambulance = df.iloc[26, 2:82]
    infrastructure = df.iloc[34, 2:82]


    clean = pd.DataFrame({
        "regionName" : regionName,
        "year": years.values,
        "month": months.values,
        "total_staff": headcounts.values,
        "doctors": doctors.values,
        "studentDoctors": studentDoctors.values,
        "nurses": nurses.values,
        "ambulanceStaff": ambulance.values,
        "infrastructure": infrastructure.values
    })
    print(clean.head())
    clean.to_csv('regional.csv' , mode = 'a', header=headers, index=False)
    headers = False #headers were being added in everytime I added a sheet in, so turned them off after the first sheet so it would turn to one table
