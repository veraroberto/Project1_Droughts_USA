# Dependencies and Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_extraction import drought_data
import datetime

def intensity(drought_data):
    #Getting total affected land area for each entry
    drought_data["None Area"]=drought_data["NONE"]*drought_data["ALAND_SQMI"]/100/1000
    drought_data["D0 Area"]=drought_data["D0"]*drought_data["ALAND_SQMI"]/100/1000
    drought_data["D1 Area"]=drought_data["D1"]*drought_data["ALAND_SQMI"]/100/1000
    drought_data["D2 Area"]=drought_data["D2"]*drought_data["ALAND_SQMI"]/100/1000
    drought_data["D3 Area"]=drought_data["D3"]*drought_data["ALAND_SQMI"]/100/1000
    drought_data["D4 Area"]=drought_data["D4"]*drought_data["ALAND_SQMI"]/100/1000
    drought_data=drought_data[["None Area","D0 Area","D1 Area","D2 Area","D3 Area","D4 Area","releaseDate"]]
    #resampling to monthy and getting the sum of all areas
    drought_datay=drought_data.set_index('releaseDate').resample("M").sum()

    #Plotting Begins
    plot_area=drought_datay[["None Area","D0 Area","D1 Area","D2 Area","D3 Area","D4 Area"]]
    #plot_area=drought_datay[["None Area Percentage", "D0 Area Percentage","D1 Area Percentage","D2 Area Percentage","D3 Area Percentage","D4 Area Percentage"]]
    fig=plot_area.plot(kind="line",figsize=(20,10))
    plt.yscale("log")
    plt.ylabel("Affected Area (Thousands of Sq. Miles)", fontsize=16)
    plt.yticks(fontsize=12)
    plt.xlabel("Year", fontsize=16)
    plt.ylim(1,4000)
    plt.xticks(fontsize=12)
    plt.title("Continental US Drought Area by level", fontsize=20)
    plt.legend(fontsize=14)
    return fig

