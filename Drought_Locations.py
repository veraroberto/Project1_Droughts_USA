
# Dependencies and Setup
#plotting code adapted from https://www.kaggle.com/balagpdy/heatmap-animation-us-drought-map
import pandas as pd
import numpy as np
from data_extraction import drought_data
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from mpl_toolkits.basemap import Basemap
import matplotlib.animation as animation


def drought_map(drought_data):
    drought_datay=drought_data
    #Confirming data is in datetime format and then resampling it to a yearly basis
    drought_datay.releaseDate=pd.to_datetime(drought_datay.releaseDate, format='%Y-%m-%d')
    drought_datay=drought_datay.set_index('releaseDate').groupby("FIPS").resample("Y").mean()
    #fixing an issue with INTPTLONG that somehow keeps turning up.
    drought_datay=drought_datay.rename(columns={"INTPTLONG                                                                                                               ":"INTPTLONG"})
    #Chaning indexes to columns
    drought_datay=drought_datay.reset_index(level=1)
    drought_datay=drought_datay.drop("FIPS",axis=1)
    drought_datay.reset_index(inplace=True)
    #then grouping by county
    drought_datay=drought_datay.groupby("FIPS")

    #plotting and making the animation
    #set initial values before updating
    figure=plt.figure(figsize=(20,10))
    axes=figure.add_subplot(111)
    #using same projection as example map because I liked how it looked like
    basemap=Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection="lcc",lat_1=33,lat_2=45,lon_0=-95)
    basemap.drawcoastlines()
    basemap.drawmapboundary(zorder=0,fill_color='#9fdbff')
    basemap.fillcontinents(color='#FFFECE',zorder=1,lake_color='#9fdbff',alpha=1)
    basemap.drawcountries(linewidth=1)
    basemap.drawstates()
    #Basemap is finished setting up, 
    pdf=drought_datay
    xloc,yloc=basemap(pdf.nth(0).INTPTLONG.tolist(),pdf.nth(0).INTPTLAT.tolist())
    color=pdf.nth(0).Level.tolist()
    pointsize=(pdf.nth(0).ALAND_SQMI/7).tolist()
    colormap=plt.cm.YlOrRd
    scalarmap = ScalarMappable(cmap=colormap)
    scatter = axes.scatter(xloc,yloc,s=pointsize,c=color,cmap=colormap,alpha=1,edgecolors='face',marker='o',vmax=5,vmin=0,zorder=1.5)
    plt.colorbar(scatter)
    plt.title('US Average Drought Level for the Year '+pdf.nth(0).releaseDate.iloc[0].strftime('%Y'))

    def update(frame):
        color=pdf.nth(frame).Level.tolist()
        scatter.set_color(scalarmap.to_rgba(color))
        plt.title('US Average Drought Level for the Year '+pdf.nth(frame).releaseDate.iloc[0].strftime('%Y'))
        return scatter
                  
    anim=animation.FuncAnimation(figure,func=update,frames=17,interval=1000)
    anim.save('Heatmap_animation_US_Drought.gif', writer='imagemagick')
    #This function will not have an output, to display the result in jupyter do the following:
    #from IPython.display import Image
    #Image("img/picture.png")

