# Data Overview 

## Source
All data is sourced from the National Solar Radiation Database ([NSRDB](https://nsrdb.nrel.gov/)). Solar Irradiation Data for Las Vegas, Chicago, and New York were taken using the 4km data while the data from Santa Fe used 2km data.

## Variables
The independent variables in all csv files are as follows: <br>
*Year*, *Month*, *Day*, *Hour*, *Minute* - Time the data was recorded <br>
*Dew Point* - The temperature in °C that the air must be cooled to be saturated with water <br>
*Surface Albedo* - Fraction of the sunlight reflected by the Earth <br>
*Wind Speed* - Speed of the wind in m/s <br>
*Wind Direction* - Direction in degrees that the wind is blowing <br>
*Relative Humidity* - Amount of water vapor in the air as a percentage of the amount needed for saturation <br>
*Temperature* - Measured in °C <br>
*Pressure* - Measured in mbar <br>
*Solar Zenith Angle* - Angle between the vertical and the ray from the sun <br>
*Precipitable Water* - Depth (in cm) of water in a column of air in the atmosphere if all water was condensed <br>
*Cloud Type* - Type of cloud present during the time interval (see below) <br>
*Cloud Type 0* - Clear <br>
*Cloud Type 1* - Probably Clear <br>
*Cloud Type 2* - Fog <br>
*Cloud Type 3* - Water <br>
*Cloud Type 4* - Super-Cooled Water <br>
*Cloud Type 5* - Mixed <br>
*Cloud Type 6* - Opaque Ice <br>
*Cloud Type 7* - Cirrus <br>
*Cloud Type 8* - Overlapping <br>
*Cloud Type 9* - Overshooting <br>
*Cloud Type 10* - Unknown <br>
*Cloud Type 11* - Dust <br>
*Cloud Type 12* - Smoke <br>

The response variable (measured in w/m^2) for all data is *Global Horizontal Irradiation* (GHI) which is the sum of Direct Normal Irradiation (DNI), Diffuse Horizontal Irradiance (DHI), and Ground-Reflected Irradiation.


## Files

### Chicago_Solar_Irradiation
*Chicago.csv* contains a joined version of the cleaned data between 2000-2020
*Chicago.nfo.csv* contains metadata about the collected data (unique ID, elevation, long, lat etc.) as well as units for all data columns
#### Cleaned
Contains the cleaned (info rows removed) data from between 2000-2020
#### Raw
Contains the raw data downloaded from NSRDB

### Las_Vegas_Solar_Irradiation
Same file structure as Chicago_Solar_Irradiation

### NY_Solar_Irradiation
Same file structure as Chicago_Solar_Irradiation

### MapData
Contains data downloaded from NSRDB from the year 2021 for an approximately 16km radius around Santa Fe

#### Raw
Contains the raw data downloaded from NSRDB
#### Cleaned
Contains the cleaned (info rows separated out) data. Metadata is contained in files that start with *info* and the actual data is contained in files that start with *data*

### Other
*SolarFull.csv* contains a cleaned and joined (but not preprocessed) csv of the data from the three cities. The variables are the same as those from the unjoined csvs. <br>
*mapJoined.csv.zip* contains a zipped version of a fully joined csv for all cleaned data files from MapData. Longitude, latitude, and unique location identifiers have been added as columns for the data rows.
