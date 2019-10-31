import matplotlib.pyplot as plt
import numpy as np
import openpyxl

class ExcelToPlot:

    def read_excel(path, sheet_name):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook[sheet_name]
        for row in sheet.rows:
            for cell in row:
                print(cell.value, "\t", end="")
            print()
