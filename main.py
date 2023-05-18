import pandas as pd
#import os
import openpyxl
import glob

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)
    total_price_sum=df["total_price"].sum()
    print(total_price_sum)