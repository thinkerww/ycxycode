import os
import pandas as pd
import feather
df = feather.read_dataframe(".\Python\Data\dataset\\topic_basic_info.feather")
df.to_csv('.\Python\Data\data4_csv.csv')
# print(df[0:1])
