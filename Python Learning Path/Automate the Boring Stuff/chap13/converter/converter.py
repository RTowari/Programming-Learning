#! python3
#! converter.py - Takes spreadsheets and put data in cvs's files. One file per sheet

import os, openpyxl, csv, sys, re

# TODO For loop for each file
def main():
    directory_path = os.getcwd()
    for filename in os.listdir(directory_path):

        if filename == "converter.py" or filename.endswith(".csv"):
            continue                 
        else:
            file_path = os.path.join(directory_path, filename)
            wb = openpyxl.load_workbook(file_path)

            spreadsheet_handling(wb, directory_path, filename)


def spreadsheet_handling(wb, directory_path, filename):
    # Iterate over sheets
    for sheet in wb:
        column_count = sheet.max_column
        row_count = sheet.max_row 

        # Iterate over spreadsheet and make csv file
        regex = re.compile(r'[A-Z]')
        shift_word = str(regex.findall(filename))
        csv_file_name = shift_word + ".csv"
        csv_file_path = os.path.join(directory_path, csv_file_name)
        
        outputFile = open(csv_file_path, 'w', newline='')
        outputWriter = csv.writer(outputFile)

        csv_list = []

        for y in range(1, row_count + 1):
            for x in range(1, column_count + 1):
                # Append cell values into list
                csv_list.append(sheet.cell(row=y, column=x).value)
            outputWriter.writerow(csv_list)
            csv_list.clear()



    
    



                
                
            


main()