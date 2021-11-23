# CLIM680 Project

## David Klein

### Introduction

#### This project will examine the effect of variations in sea surface temperature on soil moisture, examining the local and global impacts, with a focus on the western United States.

### Soil Moisture

#### This project will examine variations in soil moisture with other climate parameters. The source of soil moisture data for this project is the Climate Prediction Center (CPC). The soil moisture data consists of monthly means of soil moisture in a 0.5 degree latitude and longitude grid. The soil moisture is reported in a water height equivalent in millimeters (mm). The data is model-calculated, from observations of precipitation and surface temperature, and using a one layer "bucket" model. Soil moisture anomalies were calculated from a climatology covering the entire time period of the dataset, from 1948 to 2021. The data can be found on the [CPC Website](https://www.psl.noaa.gov/data/gridded/data.cpcsoil.html).

#### The long term average soil moisture levels can be seen below (Fig 1). Low values are seen in arid areas such as the Sahara desert, Western Australia, and Antarctica. High values are seen in the tropical rainforests, as well as the temperate climates of Eastern North America, parts of Europe, Eastern China, and Japan.
![Fig 1 CPC Soil Moisture 1948-2021](/CLIM680/hw1/longtermmean.png)

#### Monthly climatology over the time period of the dataset (1948-2021) can be seen below (Fig 2). Significant monthly and seasonal variations are seen in the temperate climates, while deserts do not see significant variation even outside the tropics.
![Fig 2 CPC Soil Moisture Monthly Climatology](/CLIM680/hw2/monthlyswmean.png)

### Sea Surface Temperatures

#### This project analyzes how variation in sea surface temperatures (SSTs) in two regions of the ocean affect soil moisture. The source of SST data for this project is the Japanese Meterological Agency. The SST data consists of monthly means of SST in a 1 degree latitude and longitude grid. The COBE SST data used is measured in degrees Celsius, and is derived from multiple observational sources, including shipboard and satellite measurements, combined to form a best estimate of monthly mean SST. SST anomalies were calculated from a climatology covering the time period of the soil moisture dataset, from 1948 to 2021. The data was obtained from the [CPC Website](https://psl.noaa.gov/data/gridded/data.cobe.html).

#### Two areas of the ocean were examined to determine their impact on soil moisture. The niño3.4 index was used. This index consists of the mean monthly SST of the area bounded by 5N-5S and 170W-120W. El Niño was defined as an anomalous SST of +1° C for a month, with La Niña being -1°C for a month. The second area of the ocean evaluted was a region off the western coast of North American bounded by 27-48N and 125-158W. The mean monthly SST of this area was dubbed the 'East Pacific Index'. This index was divided into time periods of positive and negative anomalies. A time series of this index can be seen below (Fig 3). The significant warming at the end of this time series is likely a climate change signal.
![Fig 3 East Pacific Index 1948-2021](/CLIM680/Project_Figures/eastpacindex.png)

## Modes of Analysis

#### Three methods were used to determine the effect of SSTs on soil moisture. The first was a composite analysis. The average soil moisture anomalies at each grid point were determined during time periods of El Niño, neutral, and La Niña conditions, as well as during positive and negative East Pacific Index conditions. Shown below are the composite soil moisture differences between El Niño(Fig 4)/La Niña(Fig 5) conditions and neutral conditions. Stippling shows statistically significant grid points.
![Fig 4 El Niño - Neutral Soil Moisture Composite](/CLIM680/Project_Figures/elninocompsig.png) ![Fig 5 La Niña - Neutral Soil Moisture Composite](/CLIM680/Project_Figures/laninacompsig.png)

#### Below is the composite analysis of soil moisture difference between positive and negative East Pacific Index conditions (Fig 6).
![Fig 6 Positive - Negative EPI Soil Moisture Composite](/CLIM680/Project_Figures/EPAcomp.png)

#### The next method of analysis was a correlation. SST anomalies in each index were correlated with soil moisture anomalies at each grid point. The method used was a linear least squares [method](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html). The mapped results are shown below in figures 7 and 8.
![Fig 7 ENSO Soil Moisture Correlation](/CLIM680/Project_Figures/ensocorr.png) ![Fig 8 EPI Soil Moisture Correlation](/CLIM680/Project_Figures/EPAcorr.png)

#### The same statistical method used to calculate the correlation was also used to calculate the linear regression between the SST anomaly in each index and soil moisture anomalies at each grid point. The mapped results are shown below in figures 9 and 10.
![Fig 9 ENSO Soil Moisture Linear Regression](/CLIM680/Project_Figures/ensolinreg.png) ![Fig 10 EPI Soil Moisture Linear Regression](/CLIM680/Project_Figures/EPAlinreg.png)

## Analysis

#### The niño3.4 index has an effect on soil moisture around the globe. Composite analysis shows that El Niño conditions are assoicated with drier soil moisture conditions in many areas of the world, including parts of the Amazon rainforest in Brazil, eastern Australia, Indonesia, southeast Asia, northern China, India, and South Africa. El Niño conditions are assoicated with wetter soil moisture in the central United States, southern South America, east Africa, and southern China. La Niña conditions are 'opposite' to El Niño conditions in many of these regions. For example, the Amazon tends to have wetter soil moisture conditions during La Niña. However, the central United States and southern China are not associated with dry conditions according to the composite analysis. The correlation and linear regression analysis of all of the above mentioned regions track with the compositie analysis. Notably, the correlation and linear regression analysis show a robust link between ENSO and soil moisture in the central United States and southern China, despite what the composite analysis showed. Possible explanations for this include a very strong El Niño response, and trends during neutral conditions. Overall the soil moisture response to ENSO is similar to the precipitation response to ENSO. Increased precipitation could lead directly to wetter soil moisture, if runoff and evapotranspiration do not increase to match the increased precipitation. Cloudier and more humid conditions associated with increased precipitation could limit evapotranspiration in energy limited environments.

#### ENSO has a limited impact on the soil moisture in the western United States, per the analysis done here. No statistically significant response is noted, except in the regions close to New Mexico  and Texas which see wetter soil moisture associated with El Niño conditions.

#### The East Pacific Index has an effect on soil moisture around the globe. This result is less expected than the niño3.4 result. El Niño and La Niña conditions are associated with weather and climate conditions with known teleconnections. The East Pacific Index was designed to determine the effect of local SSTs on the western United States. The global impact of this index, comparable with ENSO in this analysis, could be a result of multiple things. For one, the index could simply track global SST anomalies, which should affect climate and soil moisture worldwide. Additionally, the index used is a broad section of the Pacific that could have connections with ENSO.

#### Globally, the association between the East Pacific Index and soil moisture is similar to that between ENSO and soil moisture. Notable exceptions are in India, Indonesia, and southern South America, which have approximately reversed associations. The relationships in India and southern South American are not statistically robust across much of those regions, however. The East Pacific Index generally show more statistically significant composites and correlations across the northern hemisphere, which makes sense given its geographical location.

#### In the western United States, the East Pacific Index does have a statistically significant association with soil moisture. Hotter SST anomalies are associated with drier soil moistures in the western United States. There are multiple possible explanations for this association. A weather pattern of high pressure could cover both parts of the western United States and parts of the local ocean, causing heat waves and drought over land and marine heat waves at sea. Months or longer periods of time with more of these weather patterns could cause the association between higher SSTs and drier soil moisture. On the other hand, higher SSTs would tend to increase evaporation from the part of the ocean into the atmosphere, increasing the humidity of that air. Westerly wind, which is the long term mean for that region, would tend to move that moisture over the western United States. The analysis in this project does not support that likely increased moisture causing wetter soil moisture. Precipitation may not increase, or runoff and evapotranspiration may increase, or some other climate pattern prevents the moisture transport analysis described above.

## Conclusion

#### SSTs are assoicated with changes in soil moisture, locally and globally. In the case of the western United States, soil moisture is more highly associated with local SSTs than tropical SSTs in the form of ENSO. Higher local SSTs are associated with drier soil moisture in the western United States.

#### One note of caution with the overall analysis in this project is that the soil moisture data is model calculated. The model uses as inputs precipitation and surface temperature observations to calculate soil moisture. There is a risk that the analysis in this project is calculating how the model operates, rather than any real world association. However, the observations used to calculate soil moisture are different than those used to calculate SST, so this risk is mitigated somewhat.

### References

#### Python notebooks were used to calculate the various figures. They can be found at the following locations: [Figure 1](https://github.com/dklein3/CLIM680/blob/master/hw1/CLIM680KleinHW1.ipynb), [Figure 2](https://github.com/dklein3/CLIM680/blob/master/hw2/CLIM680KleinHw2.ipynb), [Figures 4, 5, 7, 9](https://github.com/dklein3/CLIM680/blob/master/Project_Figures/ENSOanalysis.ipynb), and [Figures 6, 8, 10](https://github.com/dklein3/CLIM680/blob/master/Project_Figures/EastPacAnalysis.ipynb). The [jupyter environment](https://github.com/dklein3/CLIM680/blob/master/environment.yml) and [functions](https://github.com/dklein3/CLIM680/blob/master/clim680_utils.py) are also available at the linked locations.

### Acknowledgments

#### Thank you very much to Dr Paul Dirmeyer and Dr Natalie Burls, GMU, for all the great instruction over the course of the semester and working on this project.

#### CPC Soil Moisture data provided by the NOAA/OAR/ESRL PSL, Boulder, Colorado, USA, from their Web site at [https://www.psl.noaa.gov/data/gridded/data.cpcsoil.html](https://www.psl.noaa.gov/data/gridded/data.cpcsoil.html)
#### COBE SST data provided by the NOAA/OAR/ESRL PSL, Boulder, Colorado, USA, from their Web site at [https://www.psl.noaa.gov/data/gridded/data.cobe.html](https://www.psl.noaa.gov/data/gridded/data.cobe.html)
