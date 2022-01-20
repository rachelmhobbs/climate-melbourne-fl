import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
#import django

def load_data(data_path, csv_file_name):
    csv_path = os.path.join(data_path, csv_file_name)
    print(csv_path)
    return pd.read_csv(csv_path)

path = '/Users/rachel/github/climate-melbourne-fl/'
filename_mlb = 'kmlb_hrly_vals_2019.csv'
filename_sd = 'ksan_hrly_vals_2019.csv'

mlb_hrly = load_data(path, filename_mlb) #melbourne dataframe
sd_hrly = load_data(path, filename_sd) #san diego dataframe

print(mlb_hrly.head())
print(mlb_hrly.tail())

print(sd_hrly.head())
print(sd_hrly.tail())
