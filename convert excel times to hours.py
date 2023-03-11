# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:35:08 2021

@author: php18ejc
"""
from tkinter import Tk
from tkinter import filedialog
import pandas as pd
from datetime import datetime
import time
import os


#%%

def calculate_timepoints(rows, df):
    Hours = []
    for j in range(0, number_of_rows):
        x = df[df.columns[0]][j]
        try:
            d = datetime.strptime(x, "%Y.%m.%d %H.%M.%S") 
        except ValueError: #corrects for error where seconds = 60
            num = (len(x)-2)
            x_new = x[:(num)] + '59'
            d = datetime.strptime(x_new, "%Y.%m.%d %H.%M.%S")
        tot_sec = time.mktime(d.timetuple())
        if j == 0:
            initial_sec = tot_sec
            hour = 0
        else:
            pass
        if j>= 1:
            sec_since = tot_sec - initial_sec
            hour = sec_since/3600
        Hours.append(hour) 
    return Hours

#%%
working_directory = input("Where should we output the data?")
os.chdir(str(working_directory)) 
cwd = os.getcwd()

root = Tk()
root.lift()
root.withdraw()
alldemfiles = filedialog.askopenfilenames(parent = root)
alldemfileslist = root.tk.splitlist(alldemfiles)
root.withdraw()

#%%
headers = ['Time', 'Split', 'Device', 'Thing', 'Pixel 1', 'Pixel 2', 'Pixel 3', 'Pixel 4', 'Pixel 5', 'Pixel 6']

for s in range(len(alldemfileslist)): 
    df = pd.read_csv(alldemfileslist[s], header = None, names = headers, engine = 'python')
    row_number = df.shape[0]
    filename = os.path.splitext(os.path.split(alldemfileslist[s]) [1])[0]  
    
    Hours = []
    for j in range(0, row_number):
        x = df[df.columns[0]][j]
        try:
            d = datetime.strptime(x, "%Y.%m.%d %H.%M.%S") 
        except ValueError: #corrects for error where seconds = 60
            num = (len(x)-2)
            x_new = x[:(num)] + '59'
            d = datetime.strptime(x_new, "%Y.%m.%d %H.%M.%S")
        tot_sec = time.mktime(d.timetuple())
        if j == 0:
            initial_sec = tot_sec
            hour = 0
        else:
            pass
        if j>= 1:
            sec_since = tot_sec - initial_sec
            hour = sec_since/3600
        Hours.append(hour)
        
        hours_dataframe = pd.DataFrame(Hours)
        hours_dataframe.to_csv(cwd + '\\' + filename + '_hours.csv', )