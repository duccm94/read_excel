from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import data_source

for key, value in data_source.file_2015.items():
 
  file = "/Users/reasonwhy/Downloads/" + value
  df = pd.read_excel(file)
  
  # show data
  print("----------" + key + "----------")
  for k, v in data_source.pos_2015.items():
    print(k, df.iloc[v][9])
  print("")
