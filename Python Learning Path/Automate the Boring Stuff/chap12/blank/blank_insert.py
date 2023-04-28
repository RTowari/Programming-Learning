#! python3
# black_inserter.py - Create a new file and fill it with numbers. Then takes M and N as command line arguments.
                        # N - Number of blanks rows
                        # M - First blank row position. Next ones will be below

import os, openpyxl, sys

N = int(sys.argv[1])
M = int(sys.argv[2])

def main():
    # Spreadsheet creation
    wb = openpyxl.Workbook()
    sheet = wb.get_sheet_by_name('Sheet')
    sheet = spreadsheet_file(sheet)
    wb.save("not_spaces.xlsx")

    
    # New spreadsheet where blank cells will be added
    new_wb = openpyxl.Workbook()
    new_sheet = new_wb.get_sheet_by_name('Sheet')
    new_sheet = rows_above(sheet, new_sheet)
    new_sheet = rows_below(sheet, new_sheet)
    new_wb.save("with_spaces.xlsx")

    # Copy rows before first blank line


# Fill spreadsheet
def spreadsheet_file(sheet):
    for i in range(1, 50):
        for x in range(1, 50):
            cell = sheet.cell(row=i, column=x)
            cell.value = 1
    
    return sheet

# Copy rows from spreadsheet into new one and stop before new blank line
def rows_above(sheet, new_sheet):
    for i in range(1, M):
        for x in range(1, 50):
            cell = sheet.cell(row=i, column=x)
            new_cell = new_sheet.cell(row=i, column=x)
            new_cell.value = cell.value


    return new_sheet
            
# Copy rows from spreadsheet into new one. Start after blank line
def rows_below(sheet, new_sheet):
    u = M+N
    for i in range(u, 50 + N):
        for x in range(1, 50):      
            cell = sheet.cell(row=i, column=x)
            new_cell = new_sheet.cell(row=i, column=x)
            new_cell.value = cell.value


    return new_sheet
    










# TODO Create a spreadsheet and fill 50x50 cells with the number 1

# TODO Command line argument to ints for easy handling

# TODO Create the blank spaces

main()