import os
import pandas as pd


# Note: The first row or column integer is 1, not 0.

directory = 'C:/Users/natha/OneDrive/Desktop/Summer 2023  Image analysis/Ua vs Ui Data/'

files = [] # list of the paths of all excel docs in the folder



# iterate over files in directory and add them to files
for filename in os.listdir(directory):
    f = directory + filename

    # checking if it is a file
    if os.path.isfile(f):
        files.append(f)

        # reading the csv file
        cvsDataframe = pd.read_csv(f)

        # creating an output excel file
        resultExcelFile = pd.ExcelWriter(f + ".xlsx")

        # converting the csv file to an excel file
        cvsDataframe.to_excel(resultExcelFile, index=False)

        # saving the excel file
        resultExcelFile.close()

        os.remove(f)

        files.append(f + ".xlsx")



