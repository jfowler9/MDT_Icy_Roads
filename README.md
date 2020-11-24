# MDT_Icy_Roads
This repository is for the MDT Icy Roads project; https://www.mdt.mt.gov/research/projects/safety/icy-road-rwis.shtml
Scripts are to analyze Resonon hyperspectral camera outputs.

### MSU sub-zero lab analysis

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
- Goal: remove arcGIS from workflow and choose NIR and Red wavelengths to optimize results. Next task is to either write python plugin to calulate ice index in script then convert output to tif or try this;
https://stackoverflow.com/questions/23816545/reading-zipped-esri-bil-files-with-python
- Upcoming task, K-means clustering of data to see if method can discern between black ice and dry asphalt.
- Upcoming task, explore Principal Component Analysis(PCA) which is a popular and widely used dimensionality reduction technique for hyperspectral data

Script for plotting:
Ice_Index_plots.Rmd

### KMSO image analysis (January - Feburary 2021)

### MDT Road image analysis

## Feedback

It's a mistake to make this an RMD file. I've changed it to a .R file. I also tried to improve your code. You watched the `dplyr` lecture, right? Did 
you do that exercise? It's not obvious from the bizarre coding choices.... Jen! The point of taking the classes is to become less of a 
hack programmer. As I mentioned in class, consider running your data frame through `janitor::clean_names()` to get names that work better in
R (and, not coincidentally, conform to the style guide we're supposed to be using). Compare what you had to what I commited. (Which, btw, 
I haven't tested, so there might be some typo-y errors.) 

Are you familiar with the DRY programming principle? Code like this next section cries out for a function: 
```
sub8 = df.loc[1129:1504 , 450:899] #get dataframe subset #9/22 (dry) Pika L = 1129:1504 , 450:899, Pika 320 = 352:469 , 160:319
        array8 = sub8.to_numpy() #make array from dataframe #9/23 (ice) Pika L = 1122:1495 , 450:899, 9/25 Pika L = 1089:1451 , 450:899
        mean8 = array8.mean() #calculate mean
        std8 = np.std(array8)
        error8 = std8/np.sqrt(array8.size)
```

There are a lot of reasons to avoid code like this, but the biggest ones are to avoid bugs and make your code easier to maintain. 

On the other hand, the analysis is awesome, so maybe I shouldn't care so much about how you get there. Really cool result, really 
nice write-up. I have some TSWD-style comments on the graphs (chiefly using a color scheme for the points so that 1, 3, 5, and 7 
are grouped together (all shades of, say, blue) while 2, 4, 6, and 8 are grouped (say, red)). I'm always looking for good collaborations
that can lead to journal articles--if you ever need someone to do stats for you, call me!

Consider this complete. Nice work. 
