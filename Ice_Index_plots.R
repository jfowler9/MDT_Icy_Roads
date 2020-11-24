
library(tidyverse)
library(reshape2)
library(lubridate)

data.file <- "Sub_Zero_Lab_MeasurementR.txt"
d <- read_tsv(paste0(data.file))

#Remove columns in dataframe
#drop <- c("Date","Room Temp C", "Sample Temp C", "Ice Temp C","Room Temp F", "Sample Temp F", "Ice Temp F", "File Name Raw", "File Name Corrected","Index TIFF", "Uncertainty")
# You don't use the above, so I'm commenting it out. 

df <- d %>% 
  select(-Date, 
         -`Room Temp C`, 
         -`Sample Temp C`,
         -`Ice Temp C`, 
         -`Room Temp F`, 
         -`Sample Temp F`,
         -`Ice Temp F`,
         -`File name Raw`, 
         -`File Name Corrected`,
         -`Index TIFF`, 
         -`Uncertainty`)

# Above replaces this line
#df = d[,!(names(d) %in% c("Date","Room Temp C", "Sample Temp C", "Ice Temp C", "Room Temp F", "Sample Temp F", "Ice Temp F", "File Name Raw", "File Name #Corrected","Index TIFF", "Uncertainty"))]

#Make sure time column is read properly
# df %>%  mutate(time = as.POSIXct(hms::parse_hm(Time))) 
# the above line doesn't assign the results anywhwere. I'm also 
# wondering if lubridate function will work for you.
df <- df %>%
    mutate(time = hm(Time))


#Grab values by day, slice keeps indicated rows
subdf_dry <- slice(df, (1:22), .preserve = TRUE)
df_melted_dry <- melt(subdf_dry, id.vars = 'Time')
# OMG, don't mix assignment operators

subdf_ice <- slice(df, (23:42), .preserve = TRUE)
df_melted_ice <- melt(subdf_ice, id.vars = 'Time')

subdf_snow <- slice(df, (58:68), .preserve = TRUE)
df_melted_snow <- melt(subdf_snow, id.vars = 'Time')


#Scatterplot of ice index versus time (and temperature which changes by time).
ggplot(df_melted_dry, aes(x = Time, y = value)) + 
    geom_point(aes(color = variable, group = variable)) + 
    labs(title = 'Ice Index vs Time by Sample Quadrant (variable) of Dry Sample') + 
    theme_gray() # Always nice to add a theme. 
    
    
ggplot(df_melted_ice, aes(x = Time, y = value)) + 
    geom_point(aes(color = variable, group = variable)) + 
    labs(title = 'Ice Index vs Time by Sample Quadrant (variable) of Ice Sample') + 
    theme_gray()

ggplot(df_melted_snow, aes(x = Time, y = value)) + 
  geom_point(aes(color = variable, group = variable)) + 
  labs(title = 'Ice Index vs Time by Sample Quadrant (variable) of Snow Sample') + 
  theme_gray()
  
# Pika L data only here, ice and snow were in quadrants 1,3,5,7	

