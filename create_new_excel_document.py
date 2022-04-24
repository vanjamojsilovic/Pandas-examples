# create new excel document

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet["A1"] = "text in a1"
sheet["A2"] = "text in a2"
sheet["A3"] = "text in a3"
workbook.save('created_excel_file.xlsx')
