from openpyxl import load_workbook


workbook = load_workbook("created_excel_file.xlsx")
sheet = workbook.active
sheet["A1"] = "Changed_text"
workbook.save("created_excel_file_result.xlsx")
