#Data extraction converted to a function
# Dependencies and Setup
import pandas as pd
import numpy as np

def drought_data():
    #Reading the drought file and dropping a useless column
    input_file = "drought_data/us-droughts.csv"
    droughts_df=pd.read_csv(input_file, encoding = "ISO-8859-1")

    droughts_df = droughts_df.drop(droughts_df[['validStart', 'validEnd', 'domStatisticFormatID']], axis=1)
    droughts_df.releaseDate = pd.to_datetime(droughts_df.releaseDate, format='%Y-%m-%d')
    #altering the drought statistics to get data that is directly workable:See excel example on file
    droughts_df["D0"]=droughts_df["D0"]-droughts_df["D1"]
    droughts_df["D1"]=droughts_df["D1"]-droughts_df["D2"]
    droughts_df["D2"]=droughts_df["D2"]-droughts_df["D3"]
    droughts_df["D3"]=droughts_df["D3"]-droughts_df["D4"]
    #adding a drought level based on https://www.kaggle.com/balagpdy/heatmap-animation-us-drought-map
    ### Calculate drought level (when NONE is 100% => 0, if D4 is 100% => 5, and linearly between 0 and 5)
    droughts_df["Level"]=(droughts_df["D0"]+droughts_df["D1"]*2+droughts_df["D2"]*3+droughts_df["D3"]*4+droughts_df["D4"]*5)/100
    #Reading the county data file
    input_file = "drought_data/county_info_2016.csv"
    #To read this file properly, due to the format it is recommended that you copy its contents to a new excel file.
    #There seems to be a format issue.
    county_df=pd.read_csv(input_file)
    #preparing the df for merging and merging
    droughtwcount_df=pd.merge(droughts_df,county_df,how='inner',left_on="FIPS",right_on="GEOID",sort=False)
    droughtwcount_dfm = droughtwcount_df.set_index('releaseDate').groupby(['FIPS']).resample('M').mean()
    droughtwcount_dfm2=droughtwcount_dfm[["FIPS","NONE","D0","D1","D2","D3","D4","Level","ALAND_SQMI","AWATER_SQMI","INTPTLAT","INTPTLONG                                                                                                               "]]
    droughtwcount_dfm2.rename(columns={"INTPTLONG                                                                                                               ":"INTPTLONG"})
    droughtwcount_dfm2=droughtwcount_dfm2.dropna()
    droughtwcount_dfm2=droughtwcount_dfm2.reset_index(level=1)
    droughtwcount_dfm2=droughtwcount_dfm2.drop("FIPS",axis=1)
    droughtwcount_dfm2.reset_index(inplace=True)
    return droughtwcount_dfm2