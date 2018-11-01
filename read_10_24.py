from os import listdir, walk
from os.path import join, isfile
from fnmatch import fnmatch
from pandas import DataFrame, read_excel
import pandas as pd
from data_10_24 import prefectures, pos_2014, pos_2015

path = "/Users/reasonwhy/Downloads/病床機能報告/"
row1 = 8

def find(partial, path):
  pattern = "*" + partial + "*"
  for root, dirs, files in walk(path):
    for file in files:
      if fnmatch(file, pattern):
        return join(root, file)
  return ""

for year in ["2014", "2015"]:
  print("---------- " + year + " ----------")
  path_year = join(path, year)
  row1_year = pos_2014[row1] if year == "2014" else pos_2015[row1]
  for k, v in prefectures.items():
    pref_name = v.get("prefecture")
    file_list = v.get("list")
    path_year_pref = join(path_year, pref_name)
    for hospital in file_list:
      file_path = find(hospital, path_year_pref)
      if file_path:
        df = read_excel(file_path)
        value = df.iloc[row1_year][9]
        print("" if pd.isnull(value) else value)
      else:
        print("")

  print("---------- END ----------\n")
