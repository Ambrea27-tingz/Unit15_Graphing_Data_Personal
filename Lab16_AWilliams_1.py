"""
Author: Ambrea Williams
Date: 05/01/2024
Title: Graphing Unemployment Rate in Ohio
Description: Reads data about Ohio's unemployment rates from 1976 to 2022 using matplotlib.
Unit 15: Lab 16
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

"""Loads in csv data from the specific file path using pathlib"""
path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

"""Generates a csv reader object to read the data"""
reader = csv.reader(lines)
header_row = next(reader)

#Uses enumerate to print the index and title of each column
# for index, col_title in enumerate(header_row) :
#     print(f'{index} {col_title}, ', end='')
# print()

"""Creates empty lists to store the dates and rates"""
rates = []
dates = []

""" Loops through the csv data and appends the dates and rates to the lists"""
for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        rate = float(row[1])
    except ValueError:
        print(f"Skipping row with bad data: {row}")
    else:
        dates.append(current_date)
        rates.append(rate)

""" Creates a visualization of the data"""
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rates)

"""Adds a title and axis labels"""
ax.set_title("Unemployment Rate in Ohio", fontsize=20)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Unemployment Rate (%)", fontsize=14)

"""Prevents the labels from clipping or overlapping"""
plt.tight_layout()

"""Displays the graph"""
plt.show()