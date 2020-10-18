# MDT_Icy_Roads
This repository is for the MDT Icy Roads project; https://www.mdt.mt.gov/research/projects/safety/icy-road-rwis.shtml

#MSU sub-zero lab analysis

Script for this task:
NDVI_Sample_Mean.py

This script takes TIFF images generated from ArcGIS (images are two asphalt samples with calibration panel), makes an arrary of the pixel values, deletes the pixel values associated with the calibration panel, then averages NDVI by quadrant of each sample.
