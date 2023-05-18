import pandas as pd
#import os
import openpyxl
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)
    total_price_sum=df["total_price"].sum()
    print(total_price_sum)
    pdf= FPDF(orientation="P", unit= "mm", format="A4")
    pdf.add_page()
    filename=Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice No.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")
