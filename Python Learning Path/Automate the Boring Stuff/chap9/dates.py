#! python3

# renameDates.py - Renames filnames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.

dataPattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-               
    ((0|1|2|3)?\d)-
    ((19|20|)\d\d)
    (.*?)$
    """, re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir("."):
    mo = dataPattern.search(amerFilename)

    #Skip files without a date
    if mo == None:
        continue
    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form thje European-style filename.
    euroFilename = beforePart + dayPart + "-" + yearPart + afterPart

    # Get the full, absolute filepaths
    absWorkingDir = os.path.abspath(".")
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(ameriFilename, euroFilename) 


    


    