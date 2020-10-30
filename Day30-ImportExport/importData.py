import pandas as pd
import xlrd
import json
import matplotlib.pyplot as plotter

df = xlrd.open_workbook('trialData.xlsx')
sheet = df.sheet_by_name('Sheet1')

rdata = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

