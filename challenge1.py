import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
#import django

def load_data(data_path, csv_file_name):
    '''
    Merges the datapath to the name of the CSV file using os package, and uses
    the Pandas package to read in the csv file. Returns a dataframe containing
    the csv file information.

    Parameters:
        data_path: path on computer where data is stored
        csv_file_name: The name of the CSV file, including '.csv'
    '''
    csv_path = os.path.join(data_path, csv_file_name)
    print(csv_path)
    return pd.read_csv(csv_path)

def total_hrs_rained(df):

    '''
    Counts the total number of hours that it rained from column called 'precip_1hr'.

    Parameter:
        df: the dataframe
    '''
    count1 = (df['precip_1hr'] > 0).sum()
    print('The total number of hours it rained was', count1)
    return count1

def temp_over_100(df):

    '''
    Counts the total number of hours when temperature was strictly greater than
    100 degrees using dataframe column called 'temp'.

    Parameter:
        df: the dataframe
    '''
    count2 = (df['temp'] > 100).sum()
    print('The total number of hours when temperature was greater than 100 was', count2)
    return count2

def temp_less_32(df):

    '''
    Counts the total number of hours when temperature was strictly less than
    32 degrees using dataframe column called 'temp'.

    Parameter:
        df: the dataframe
    '''
    count3 = (df['temp'] < 32).sum()
    print('The total number of hours when temperature was less than 32 was', count3)
    return count3

def temp_ave(df):

    '''
    The mean of the dataframe column called 'temp'.

    Parameter:
        df: the dataframe
    '''
    temp_mean = df['temp'].mean()
    print('The total average temperature was', temp_mean)
    return temp_mean

def humidity(df):
    #got overflow warning, can suppress with warning package
    #something is wrong with H column - everything is 0? Does this make sense?
    #also, why are there so little values in H compared to the number of values
    #in dewpt or temp??
    '''
    Adds a new column 'H' to the end of the dataframe that contains humidity
    values based on information from columns 'dewpt' and 'temp'. Returns the
    dataframe with the newly added humidity column.

    Parameter:
        df: the dataframe
    '''
    numr = (np.exp(17.625 * df['dewpt']))/(243.04 + df['dewpt'])
    denom = (np.exp(17.625 * df['temp']))/(243.04 + df['temp'])
    df['H'] = 100 * (numr/denom)
    print(df.describe())
    return df

#def all_calculations(climate_df):

path = '/Users/rachel/github/climate-melbourne-fl/'
filename_mlb = 'kmlb_hrly_vals_2019.csv'
filename_sd = 'ksan_hrly_vals_2019.csv'

mlb_hrly = load_data(path, filename_mlb) #melbourne dataframe
sd_hrly = load_data(path, filename_sd) #san diego dataframe

print(mlb_hrly.head())
print(mlb_hrly.tail())

print(sd_hrly.head())
print(sd_hrly.tail())

mlb_rain = total_hrs_rained(mlb_hrly)
print(mlb_rain)

sd_rain = total_hrs_rained(sd_hrly)
print(sd_rain)

mlb_temp_gr_100 = temp_over_100(mlb_hrly)
print(mlb_temp_gr_100)

sd_temp_gr_100 = temp_over_100(sd_hrly)
print(sd_temp_gr_100)

mlb_temp_ls_32 = temp_less_32(mlb_hrly)
print(mlb_temp_ls_32)

sd_temp_ls_32 = temp_less_32(sd_hrly)
print(sd_temp_ls_32)

mlb_ave = temp_ave(mlb_hrly)
print(mlb_ave)

sd_ave = temp_ave(sd_hrly)
print(sd_ave)

mlb_hrly['time'] = pd.to_datetime(mlb_hrly['time'])

print(mlb_hrly['time']) #it's now a datetime type
#print(mlb_hrly['time'].min())
#print(mlb_hrly['time'].max())

mlb_hrly.set_index('time', inplace=True)
#print(mlb_hrly) #success

#print(mlb_hrly.loc['2019-01']) #values for january
print(mlb_hrly.loc['2019-01']['temp'].mean()) #january mean

#print(mlb_hrly.describe())
#print(sd_hrly.describe())

#humidity(mlb_hrly)
#humidity(sd_hrly)
#print(mlb_hrly.describe())
