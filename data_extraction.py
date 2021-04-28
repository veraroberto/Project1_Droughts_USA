#Data extraction converted to a function
# Dependencies and Setup
import pandas as pd
import numpy as np

def drought_data():
    #Reading the drought file and dropping a useless column
    input_file = "drought_data/us-droughts.csv"
    droughts_df=pd.read_csv(input_file)
    droughts_df=droughts_df.drop(columns="domStatisticFormatID")
    #altering the drought statistics to get data that is directly workable:See excel example on file
    droughts_df["D0"]=droughts_df["D0"]-droughts_df["D1"]
    droughts_df["D1"]=droughts_df["D1"]-droughts_df["D2"]
    droughts_df["D2"]=droughts_df["D2"]-droughts_df["D3"]
    droughts_df["D3"]=droughts_df["D3"]-droughts_df["D4"]
    droughts_df["Sumtotal"]=droughts_df["NONE"]+droughts_df["D0"]+droughts_df["D1"]+droughts_df["D2"]+droughts_df["D3"]+droughts_df["D4"]
    #sumtotal is a check to make sure it reaches 100% technically not required.
    #Reading the county data file
    input_file = "drought_data/county_info_2016.csv"
    #To read this file properly, due to the format it is recommended that you copy its contents to a new excel file.
    #There seems to be a format issue.
    county_df=pd.read_csv(input_file)
    #preparing the df for merging and merging
    county_df=county_df.rename(columns={"GEOID":"FIPS"})
    droughtwcount_df=droughts_df.merge(county_df,how='left',on="FIPS")
    #Removing repeated column and dropping all na values
    droughtwcount_df=droughtwcount_df.drop(columns=["NAME"])
    droughtwcount_df=droughtwcount_df.dropna()
    return droughtwcount_df


