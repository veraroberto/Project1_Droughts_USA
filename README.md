# Project1_Droughts_USA
## Team Members 
* Roberto Vera 
* Leo Muñoz 
* Salvador Del Cos 
* Ángeles Cruz 

### We analyzed the droughts levels across the US and its possible correlation with wildfires throughout the years 2000 to 2016.

* We selected two data sources, one from Kaggle y the other one from MTBS (Monitoring Trends in Burn Severity). 
* We cleaned up the datasets, drop columns we weren't going to use and null values too. 
* The clean up process for both datasets turned into .py functions to avoid huge jupyter notebooks. 
* In the exploration process, we generated different visualization, such as linear and bar plots. 
* We also used a library called Basemap, to draw the US map and avoid using the API from Google. 

### Findings 
* Based on the droughts levels we generated, throught the year 2000 to 2016, the highest average drought level ocurred in 2012, with a level of 1.4. 
* 2.4 has been the highest average drought level, the top 5 counties are located in the state of Nevada. 
* Out of the 6 drought levels, the number 5 (which is the exceptional drought) didn't decrease drom 2011 to 2016, as it did in previous years. 
* More than 8K wildires had taken place in the US in the same years. 
* 2011 was the year with most wildfires, 846. 
* 2005 was the year with the most sq. miles burned. However, this year wasnt the year with most wildfires. So, the wildfires quantity doesn't mean more sq. miles are burned. 
* In our animated maps, highest drought level locations seem to be located as the wildfires. 


<img src="https://github.com/veraroberto/Project1_Droughts_USA/blob/main/Heatmap_animation_US_Drought.gif 
" width="90%"></img>

<img src="https://github.com/veraroberto/Project1_Droughts_USA/blob/main/Fires_map.gif 
" width="90%"></img>


### Presentation 
* https://github.com/veraroberto/Project1_Droughts_USA/blob/main/Project1_Droughts_in_the_USA.pdf 


### Data Cleaning 
* Droughts & Counties: https://github.com/veraroberto/Project1_Droughts_USA/blob/main/data_extraction.ipynb 

* Fires: https://github.com/veraroberto/Project1_Droughts_USA/blob/main/wildfires_dataframe.ipynb 


### Data Analysis 

* Droughts Intensity: https://github.com/veraroberto/Project1_Droughts_USA/blob/main/Drought_Intensity.ipynb

* Droughts Location: https://github.com/veraroberto/Project1_Droughts_USA/blob/main/Drought_Locations.ipynb 

* Fires: https://github.com/veraroberto/Project1_Droughts_USA/blob/main/fires_data_maping.ipynb 