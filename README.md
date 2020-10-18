# MDT_Icy_Roads
This repository is for the MDT Icy Roads project; https://www.mdt.mt.gov/research/projects/safety/icy-road-rwis.shtml
Scripts are to analyze Resonon hyperspectral camera outputs.

###MSU sub-zero lab analysis

Script for this task:
Ice_Index_Sample_Mean.py

This script takes TIFF images generated from ArcGIS (images are two asphalt samples with calibration panel, takes 70GB data to 450 MB), makes an arrary of the pixel values, deletes the pixel values associated with the calibration panel, then averages NDVI values by quadrant of each sample.

- Sept 22, Pika L camera used on dry samples from 4C - 8C at 2 degree increments
- Sept 23, Pika L camera used on 1/2 dry and 1/2 wet/ice samples from 4C - 8C at 2 degree increments
- Sept 24, Pika 320 camera used on 1/2 dry and 1/2 wet/ice samples from 4C - 8C at 2 degree increments
- Sept. 25, Pika L camera used on 1/2 dry and 1/2 wet/snow samples from 4C - 8C at 2 degree increments

quadrants 1,3,5,7	contain snow/ice/wet

 - ice_index = (NIR wavelength - Red wavelength)/(NIR wavelength + Red wavelength)
 - If ice_index is positive then asphalt is dry, if ice_index is negative then asphalt has ice. Trying to discern between black ice and dry asphalt.

Resonon camera software outputs .bip or .bil file. 
- Goal: remove arcGIS from workflow and choose NIR and Red wavelengths to optimize results. Next task is to either write python plugin to calulate NDVI in script then convert output to tif or try this;
https://stackoverflow.com/questions/23816545/reading-zipped-esri-bil-files-with-python
- Upcoming task, K-means clustering of data to see if method can discern between black ice and dry asphalt.
- Upcoming task, explore Principal Component Analysis(PCA) which is a popular and widely used dimensionality reduction technique for hyperspectral data

###KMSO image analysis (January - Feburary 2021)

###MDT Road image analysis

