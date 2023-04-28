#! python3
# multiplication.py - Takes an int from the comman line and creates an NxN multiplication table in Excel spreadsheet

import os, openpyxl, sys


# Folder creation and command line argument handling.
NUMBER = int(sys.argv[1])    

def main():
    directory_path = os.getcwd()
    folder_path = os.path.join(directory_path, "table_folder")

    if os.path.exists(folder_path) == False:                                            
        os.mkdir(folder_path)
    else:   # If the folder already exist do nothing
        print("******Folder already exist. If there is a file inside it will be deleted...******")

    # Makes the spreadsheet numbers at the borders
    wb = openpyxl.Workbook()
    sheet = wb.get_sheet_by_name('Sheet')   # Get sheet object to work with

    row_col_lenght = NUMBER  # Set user input as lenght
    cell_value = 1
    print("Those are cols: ")
    # Add number to first row
    for col in sheet.iter_cols(max_row=1, min_col=2, max_col = row_col_lenght + 1): # First col doesn't count
        for cell in col:
            cell.value = cell_value
            cell_value = cell_value + 1
            print(cell.value, " : ", cell)

    cell_value = 1
    print("Those are rows: ")
    # Add number first col
    for row in sheet.iter_rows(max_col=1, min_row=2, max_row = row_col_lenght + 1): # First row doesn't count
        for cell in row:
            cell.value = cell_value
            cell_value = cell_value + 1
            print(cell.value, " : ", cell)

    # Multiplication for every cell
    sheet = iterate_whole_table(sheet, row_col_lenght)        

    # Saves spreadsheet in folder
    file_path = os.path.join(folder_path, 'table_file.xlsx')
    if os.path.exists(file_path) == False:  
        wb.save(file_path)
    else:
        os.remove(file_path)
        wb.save(file_path)

# This function will iterate every cells
def iterate_whole_table(sheet, row_col_lenght):

    for x in range(1, row_col_lenght + 1):
        for i in range(1, row_col_lenght + 1):
            active_cell = sheet.cell(row = i + 1, column = x + 1) # Dont touch A1
            active_cell.value = multiplication_handling(i, x)
        

# This function will take axis numbers and return the multiplication
def multiplication_handling(row_axis, col_axis):

    cell_value = (row_axis) * (col_axis)
    return cell_value


main()
