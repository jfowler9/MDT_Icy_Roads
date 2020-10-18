import glob
from PIL import Image
from numpy import asarray
import numpy as np
import pandas as pd
import os

#Change path and means.to_csv depending on folder date

path = r'/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/9_25_20_TIF' # look in this directory, use absolute path 
all_files = glob.glob(path + "/*.tif") #find all files with .tif extension
means = []

select = (os.path.basename(path))

for filename in all_files:
    #read tiff file. File is NDVI ratio from bands selected in ArcGIS
    #imh = Image.open('filename') 
    imh = Image.open(os.path.join(path, filename))
   #convert from image object to numpy array.
    data = asarray(imh)
    
    if select == "9_22_20_TIF":
        FIRST = 725 
        LAST = 849 
        subset = list(range(FIRST)) + list(range(LAST + 1, len(data)))#make a subset array, + list concatenates, len to get end of array
        new_data = data[subset].copy()
        
        df = pd.DataFrame(new_data) #made a dataframe to use pandas
        #df = pd.DataFrame(data) #needed for Pika 320, calibration panel not obvious so get cropped images
    
        sub1 = df.loc[0:376 , 0:449] #get dataframe subset #9/22 Pika L = 0:376 , 0:449, Pika 320 = 0:116 , 0:159
        array1 = sub1.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 0:449, 9/25 Pika L = 0:362 , 0:449
        mean1 = array1.mean() #calculate mean
        std1 = np.std(array1) #calculate standard deviation
        error1 = std1/np.sqrt(array1.size) #calculate error in the mean (N = rowsxcolumns) #320 = 18720, 9/22 = 169200, 9/23 = 168300
        
        sub2 = df.loc[0:376 , 450:899] #get dataframe subset #9/22 Pika L = 0:376 , 450:899, Pika 320 = 0:116 , 160:319
        array2 = sub2.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 450:899, 9/25 Pika L = 0:362 , 450:899
        mean2 = array2.mean() #calculate mean
        std2 = np.std(array2)
        error2 = std2/np.sqrt(array2.size)
        
        sub3 = df.loc[377:752 , 0:449] #get dataframe subset #9/22 Pika L = 377:752 , 0:449, Pika 320 = 117:234 , 0:159
        array3 = sub3.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 0:449, 9/25 Pika L = 363:725 , 0:449
        mean3 = array3.mean() #calculate mean
        std3 = np.std(array3)
        error3 = std3/np.sqrt(array3.size)
        
        sub4 = df.loc[377:752 , 450:899] #get dataframe subset #9/22 Pika L = 377:752 , 450:899, Pika 320 = 117:234 , 160:319
        array4 = sub4.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 450:899, 9/25 Pika L = 363:725 , 450:899
        mean4 = array4.mean() #calculate mean
        std4 = np.std(array4)
        error4 = std4/np.sqrt(array4.size) 
        
        sub5 = df.loc[753:1128 , 0:449] #get dataframe subset #9/22 Pika L = 753:1128 , 0:449, Pika 320 = 235:351 , 0:159
        array5 = sub5.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 0:449, 9/25 Pika L = 726:1088 , 0:449
        mean5 = array5.mean() #calculate mean
        std5 = np.std(array5)
        error5 = std5/np.sqrt(array5.size)
        
        sub6 = df.loc[753:1128 , 450:899] #get dataframe subset #9/22 Pika L = 753:1128 , 450:899, Pika 320 = 235:351 , 160:319
        array6 = sub6.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 450:899, 9/25 Pika L = 726:1088 , 450:899
        mean6 = array6.mean() #calculate mean
        std6 = np.std(array6)
        error6 = std6/np.sqrt(array6.size)
        
        sub7 = df.loc[1129:1504 , 0:449] #get dataframe subset #9/22 Pika L = 1129:1504 , 0:449, Pika 320 = 352:469 , 0:159
        array7 = sub7.to_numpy() #make array from dataframe #9/23 Pika L = 1122:1495 , 0:449, 9/25 Pika L = 1089:1451, 0:449
        mean7 = array7.mean() #calculate mean
        std7 = np.std(array7)
        error7 = std7/np.sqrt(array7.size)
        
        sub8 = df.loc[1129:1504 , 450:899] #get dataframe subset #9/22 (dry) Pika L = 1129:1504 , 450:899, Pika 320 = 352:469 , 160:319
        array8 = sub8.to_numpy() #make array from dataframe #9/23 (ice) Pika L = 1122:1495 , 450:899, 9/25 Pika L = 1089:1451 , 450:899
        mean8 = array8.mean() #calculate mean
        std8 = np.std(array8)
        error8 = std8/np.sqrt(array8.size)
        
        marr = np.array([mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8])
        earr = np.array([error1, error2, error3, error4, error5, error6, error7, error8])
        
        #make new folder to hold calculated data
#        if not os.path.isdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_22_20'):
#            os.mkdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_22_20')
        
        file = os.path.split(filename) #returns a tuple that represents head and tail of the specified path name.
        
        
        col_Names=[file[1]]
        df_2 = pd.DataFrame(marr, columns=col_Names)
        means.append(df_2) #filling in empty list defined above
    #    df_3 = pd.DataFrame(earr, columns=col_Names) #adds error values to file
    #    means.append(df_3)
    
    
    elif select == "9_23_20_TIF":
        FIRST = 757 
        LAST = 891 
        subset = list(range(FIRST)) + list(range(LAST + 1, len(data)))#make a subset array, + list concatenates, len to get end of array
        new_data = data[subset].copy()
        
        df = pd.DataFrame(new_data) #made a dataframe to use pandas
        #df = pd.DataFrame(data) #needed for Pika 320, calibration panel not obvious so get cropped images
    
        sub1 = df.loc[0:373 , 0:449] #get dataframe subset #9/22 Pika L = 0:376 , 0:449, Pika 320 = 0:116 , 0:159
        array1 = sub1.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 0:449, 9/25 Pika L = 0:362 , 0:449
        mean1 = array1.mean() #calculate mean
        std1 = np.std(array1) #calculate standard deviation
        error1 = std1/np.sqrt(array1.size) #calculate error in the mean (N = rowsxcolumns) #320 = 18720, 9/22 = 169200, 9/23 = 168300
        
        sub2 = df.loc[0:373 , 450:899] #get dataframe subset #9/22 Pika L = 0:376 , 450:899, Pika 320 = 0:116 , 160:319
        array2 = sub2.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 450:899, 9/25 Pika L = 0:362 , 450:899
        mean2 = array2.mean() #calculate mean
        std2 = np.std(array2)
        error2 = std2/np.sqrt(array2.size)
        
        sub3 = df.loc[374:747 , 0:449] #get dataframe subset #9/22 Pika L = 377:752 , 0:449, Pika 320 = 117:234 , 0:159
        array3 = sub3.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 0:449, 9/25 Pika L = 363:725 , 0:449
        mean3 = array3.mean() #calculate mean
        std3 = np.std(array3)
        error3 = std3/np.sqrt(array3.size)
        
        sub4 = df.loc[374:747 , 450:899] #get dataframe subset #9/22 Pika L = 377:752 , 450:899, Pika 320 = 117:234 , 160:319
        array4 = sub4.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 450:899, 9/25 Pika L = 363:725 , 450:899
        mean4 = array4.mean() #calculate mean
        std4 = np.std(array4)
        error4 = std4/np.sqrt(array4.size) 
        
        sub5 = df.loc[748:1121 , 0:449] #get dataframe subset #9/22 Pika L = 753:1128 , 0:449, Pika 320 = 235:351 , 0:159
        array5 = sub5.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 0:449, 9/25 Pika L = 726:1088 , 0:449
        mean5 = array5.mean() #calculate mean
        std5 = np.std(array5)
        error5 = std5/np.sqrt(array5.size)
        
        sub6 = df.loc[748:1121 , 450:899] #get dataframe subset #9/22 Pika L = 753:1128 , 450:899, Pika 320 = 235:351 , 160:319
        array6 = sub6.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 450:899, 9/25 Pika L = 726:1088 , 450:899
        mean6 = array6.mean() #calculate mean
        std6 = np.std(array6)
        error6 = std6/np.sqrt(array6.size)
        
        sub7 = df.loc[1122:1495 , 0:449] #get dataframe subset #9/22 Pika L = 1129:1504 , 0:449, Pika 320 = 352:469 , 0:159
        array7 = sub7.to_numpy() #make array from dataframe #9/23 Pika L = 1122:1495 , 0:449, 9/25 Pika L = 1089:1451, 0:449
        mean7 = array7.mean() #calculate mean
        std7 = np.std(array7)
        error7 = std7/np.sqrt(array7.size)
        
        sub8 = df.loc[1122:1495 , 450:899] #get dataframe subset #9/22 (dry) Pika L = 1129:1504 , 450:899, Pika 320 = 352:469 , 160:319
        array8 = sub8.to_numpy() #make array from dataframe #9/23 (ice) Pika L = 1122:1495 , 450:899, 9/25 Pika L = 1089:1451 , 450:899
        mean8 = array8.mean() #calculate mean
        std8 = np.std(array8)
        error8 = std8/np.sqrt(array8.size)
        
        marr = np.array([mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8])
        earr = np.array([error1, error2, error3, error4, error5, error6, error7, error8])
        
        #make new folder to hold calculated data
#        if not os.path.isdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_22_20'):
#            os.mkdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_22_20')
        
        file = os.path.split(filename) #returns a tuple that represents head and tail of the specified path name.
        
        col_Names=[file[1]]
        df_2 = pd.DataFrame(marr, columns=col_Names)
        means.append(df_2)
    #    df_3 = pd.DataFrame(earr, columns=col_Names) #adds error values to file
    #    means.append(df_3)
    
    elif select == "9_24_20_TIF":
        FIRST = 239 
        LAST = 283 
        subset = list(range(FIRST)) + list(range(LAST + 1, len(data)))#make a subset array, + list concatenates, len to get end of array
        new_data = data[subset].copy()
        df = pd.DataFrame(new_data) #made a dataframe to use pandas
        #df = pd.DataFrame(data) #needed for Pika 320, calibration panel not obvious so get cropped images
    
        sub1 = df.loc[0:116 , 0:159] #get dataframe subset #9/22 Pika L = 0:376 , 0:449, Pika 320 = 0:116 , 0:159
        array1 = sub1.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 0:449, 9/25 Pika L = 0:362 , 0:449
        mean1 = array1.mean() #calculate mean
        std1 = np.std(array1) #calculate standard deviation
        error1 = std1/np.sqrt(array1.size) #calculate error in the mean (N = rowsxcolumns) #320 = 18720, 9/22 = 169200, 9/23 = 168300
        
        sub2 = df.loc[0:116 , 160:319] #get dataframe subset #9/22 Pika L = 0:376 , 450:899, Pika 320 = 0:116 , 160:319
        array2 = sub2.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 450:899, 9/25 Pika L = 0:362 , 450:899
        mean2 = array2.mean() #calculate mean
        std2 = np.std(array2)
        error2 = std2/np.sqrt(array2.size)
        
        sub3 = df.loc[117:234 , 0:159] #get dataframe subset #9/22 Pika L = 377:752 , 0:449, Pika 320 = 117:234 , 0:159
        array3 = sub3.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 0:449, 9/25 Pika L = 363:725 , 0:449
        mean3 = array3.mean() #calculate mean
        std3 = np.std(array3)
        error3 = std3/np.sqrt(array3.size)
        
        sub4 = df.loc[117:234 , 160:319] #get dataframe subset #9/22 Pika L = 377:752 , 450:899, Pika 320 = 117:234 , 160:319
        array4 = sub4.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 450:899, 9/25 Pika L = 363:725 , 450:899
        mean4 = array4.mean() #calculate mean
        std4 = np.std(array4)
        error4 = std4/np.sqrt(array4.size) 
        
        sub5 = df.loc[235:351 , 0:159] #get dataframe subset #9/22 Pika L = 753:1128 , 0:449, Pika 320 = 235:351 , 0:159
        array5 = sub5.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 0:449, 9/25 Pika L = 726:1088 , 0:449
        mean5 = array5.mean() #calculate mean
        std5 = np.std(array5)
        error5 = std5/np.sqrt(array5.size)
        
        sub6 = df.loc[235:351 , 160:319] #get dataframe subset #9/22 Pika L = 753:1128 , 450:899, Pika 320 = 235:351 , 160:319
        array6 = sub6.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 450:899, 9/25 Pika L = 726:1088 , 450:899
        mean6 = array6.mean() #calculate mean
        std6 = np.std(array6)
        error6 = std6/np.sqrt(array6.size)
        
        sub7 = df.loc[352:469 , 0:159] #get dataframe subset #9/22 Pika L = 1129:1504 , 0:449, Pika 320 = 352:469 , 0:159
        array7 = sub7.to_numpy() #make array from dataframe #9/23 Pika L = 1122:1495 , 0:449, 9/25 Pika L = 1089:1451, 0:449
        mean7 = array7.mean() #calculate mean
        std7 = np.std(array7)
        error7 = std7/np.sqrt(array7.size)
        
        sub8 = df.loc[352:469 , 160:319] #get dataframe subset #9/22 (dry) Pika L = 1129:1504 , 450:899, Pika 320 = 352:469 , 160:319
        array8 = sub8.to_numpy() #make array from dataframe #9/23 (ice) Pika L = 1122:1495 , 450:899, 9/25 Pika L = 1089:1451 , 450:899
        mean8 = array8.mean() #calculate mean
        std8 = np.std(array8)
        error8 = std8/np.sqrt(array8.size)
        
        marr = np.array([mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8])
        earr = np.array([error1, error2, error3, error4, error5, error6, error7, error8])
        
        #make new folder to hold calculated data
#        if not os.path.isdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_24_20'):
#            os.mkdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_24_20')
#        
        file = os.path.split(filename) #returns a tuple that represents head and tail of the specified path name.
        
        col_Names=[file[1]]
        df_2 = pd.DataFrame(marr, columns=col_Names)
        means.append(df_2)
    #    df_3 = pd.DataFrame(earr, columns=col_Names) #adds error values to file
    #    means.append(df_3)
    
    elif select == "9_25_20_TIF":
        FIRST = 0 
        LAST = 147 
        subset = list(range(FIRST)) + list(range(LAST + 1, len(data)))#make a subset array, + list concatenates, len to get end of array
        new_data = data[subset].copy()
        
        df = pd.DataFrame(new_data) #made a dataframe to use pandas
        #df = pd.DataFrame(data) #needed for Pika 320, calibration panel not obvious so get cropped images
    
        sub1 = df.loc[0:362 , 0:449] #get dataframe subset #9/22 Pika L = 0:376 , 0:449, Pika 320 = 0:116 , 0:159
        array1 = sub1.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 0:449, 9/25 Pika L = 0:362 , 0:449
        mean1 = array1.mean() #calculate mean
        std1 = np.std(array1) #calculate standard deviation
        error1 = std1/np.sqrt(array1.size) #calculate error in the mean (N = rowsxcolumns) #320 = 18720, 9/22 = 169200, 9/23 = 168300
        
        sub2 = df.loc[0:362 , 450:899] #get dataframe subset #9/22 Pika L = 0:376 , 450:899, Pika 320 = 0:116 , 160:319
        array2 = sub2.to_numpy() #make array from dataframe #9/23 Pika L = 0:373 , 450:899, 9/25 Pika L = 0:362 , 450:899
        mean2 = array2.mean() #calculate mean
        std2 = np.std(array2)
        error2 = std2/np.sqrt(array2.size)
        
        sub3 = df.loc[363:725 , 0:449] #get dataframe subset #9/22 Pika L = 377:752 , 0:449, Pika 320 = 117:234 , 0:159
        array3 = sub3.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 0:449, 9/25 Pika L = 363:725 , 0:449
        mean3 = array3.mean() #calculate mean
        std3 = np.std(array3)
        error3 = std3/np.sqrt(array3.size)
        
        sub4 = df.loc[363:725 , 450:899] #get dataframe subset #9/22 Pika L = 377:752 , 450:899, Pika 320 = 117:234 , 160:319
        array4 = sub4.to_numpy() #make array from dataframe #9/23 Pika L = 374:747 , 450:899, 9/25 Pika L = 363:725 , 450:899
        mean4 = array4.mean() #calculate mean
        std4 = np.std(array4)
        error4 = std4/np.sqrt(array4.size) 
        
        sub5 = df.loc[726:1088 , 0:449] #get dataframe subset #9/22 Pika L = 753:1128 , 0:449, Pika 320 = 235:351 , 0:159
        array5 = sub5.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 0:449, 9/25 Pika L = 726:1088 , 0:449
        mean5 = array5.mean() #calculate mean
        std5 = np.std(array5)
        error5 = std5/np.sqrt(array5.size)
        
        sub6 = df.loc[726:1088 , 450:899] #get dataframe subset #9/22 Pika L = 753:1128 , 450:899, Pika 320 = 235:351 , 160:319
        array6 = sub6.to_numpy() #make array from dataframe #9/23 Pika L = 748:1121 , 450:899, 9/25 Pika L = 726:1088 , 450:899
        mean6 = array6.mean() #calculate mean
        std6 = np.std(array6)
        error6 = std6/np.sqrt(array6.size)
        
        sub7 = df.loc[1089:1451, 0:449] #get dataframe subset #9/22 Pika L = 1129:1504 , 0:449, Pika 320 = 352:469 , 0:159
        array7 = sub7.to_numpy() #make array from dataframe #9/23 Pika L = 1122:1495 , 0:449, 9/25 Pika L = 1089:1451, 0:449
        mean7 = array7.mean() #calculate mean
        std7 = np.std(array7)
        error7 = std7/np.sqrt(array7.size)
        
        sub8 = df.loc[1089:1451 , 450:899] #get dataframe subset #9/22 (dry) Pika L = 1129:1504 , 450:899, Pika 320 = 352:469 , 160:319
        array8 = sub8.to_numpy() #make array from dataframe #9/23 (ice) Pika L = 1122:1495 , 450:899, 9/25 Pika L = 1089:1451 , 450:899
        mean8 = array8.mean() #calculate mean
        std8 = np.std(array8)
        error8 = std8/np.sqrt(array8.size)
        
        marr = np.array([mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8])
        earr = np.array([error1, error2, error3, error4, error5, error6, error7, error8])
        
        #make new folder to hold calculated data
#        if not os.path.isdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_25_20'):
#            os.mkdir('/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_25_20')
        
        file = os.path.split(filename) #returns a tuple that represents head and tail of the specified path name.
        
        col_Names=[file[1]]
        df_2 = pd.DataFrame(marr, columns=col_Names)
        means.append(df_2)
    #    df_3 = pd.DataFrame(earr, columns=col_Names) #adds error values to file
    #    means.append(df_3)
        
means = pd.concat(means, sort=False)
means = means.T
#
#
means.to_csv(r'/Users/jen/Box Sync/AASOMain/Grants/MDT/Icy Roads Project/Sub-Zero Lab Measurements/Python code/TIF_Data/means9_25_20.csv') #put edited files into new folder
