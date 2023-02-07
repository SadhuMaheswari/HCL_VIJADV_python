from openpyxl import workbook
wb=workbook()
sheet=wb.active
sheet.title="Hcl"
sheet["A1"].value=10
sheet["B2"].value="test"
sheet.cell(row=3,column=3).value="Hcl data"
j=100
for i in range(10,60,10):
    j+=1
    sheet.cell