#import dependencies
import pandas as pd
import csv 
import datetime

def fires_data():
    # File to Load (Remember to Change These)
    file = "fires_data/Fires_data.csv"

    # Read Purchasing File and store into Pandas data frame
    fires_df = pd.read_csv(file)

    # Clean data and eliminate columns
    clean_df = fires_df.drop(['X', 'Y', 'OBJECTID', 'NODATA_THRESHOLD', 'LOW_THRESHOLD','MODERATE_THRESHOLD', 'HIGH_THRESHOLD','GREENNESS_THRESHOLD','FIRE_ID', 'ASMNT_TYPE', 'PRE_ID', 'POST_ID', 'FIRE_NAME', 'IRWINID', 'MAP_ID', 'MAP_PROG', 'PERIM_ID', 'DNBR_OFFST', 'DNBR_STDDV', 'COMMENTS'],axis=1)
    
    # Convert to datetime
    clean_df.IG_DATE = pd.to_datetime(clean_df.IG_DATE, format='%Y-%m-%d')
    
    # Eliminate other kinds of fires
    wildfire_df = clean_df.loc[fires_df["FIRE_TYPE"] == "Wildfire", :]

    # Select data from 2000 to 2016
    filtered_df = wildfire_df.loc[(wildfire_df['IG_DATE'] >= '2000-01-01')
                         & (wildfire_df['IG_DATE'] < '2016-12-31')]
    # clean dates and add year column
    filtered_date_df = pd.DataFrame(filtered_df)
    filtered_date_df.IG_DATE = pd.to_datetime(filtered_date_df.IG_DATE, format='%Y-%m-%d').dt.date
    filtered_date_df["YEAR"] = pd.DatetimeIndex(filtered_date_df['IG_DATE']).year
    
    #Convert Acres to Miles
    filtered_date_df["MILES"] = filtered_date_df["ACRES"].astype(float)*(1/640)
    
    # Add and reset index
    filtered_date_df.reset_index(inplace=True)
    index_df = filtered_date_df.drop("index", axis=1)

    
    # group data
    #years_group = filtered_date_df.groupby("YEAR")
    
        
    return index_df