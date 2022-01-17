# ASLGlove

To fully understand the project and code, refer to: https://drive.google.com/file/d/1_ij-H_Hi2xiw3T25jOMQu8cjde0JfS4K/view?usp=sharing

Some more specifics related to the code:

Arduino serial monitor data is logged using Putty

Putty inputs all data to test.txt, so change the file path in putty to test.txt
Also change port number on Putty based on the port shown from Arduino>Tools>Port

All the averages.txt files were used for data collection, and createFinalAverages would find the averages to then be used to find the averages for each data marker which was then compared to averages found from a live translation.

run GetAllData for arduino data collection

run testAverage.py to append the averages of each sign to the averages.txt files

run createFinalAverages to get the final average for each data marker based on the averages.txtfiles

run the euclidianDistanceTranslationAlgorithm at the end of conducting a sign to get a translation

If averages for each data marker are being found again remember to change the averages in the euclidianDistanceTranslationAlgorithm.py and normalize them again. Normalize them using the normalization formula with the highest and lowest values found from the data marker averages of the signs which will already be in the arrays created from createFinalAverages and in the euclidianDistanceTranslationAlgorithm.py

Extra stuff:

the 1000averagestrialredo folder was created to find the averages for each sign again after dust affected the sensors.

Currently confidence is calculated based on the difference between the euclidian distance of the recognized sign and the averages of the others. However, since the difference between the two does not necessarily indicate how confident it is. How close the euclidian distance is to 0 could be a better metric. Calculate the confidence based on a standardized number across all of the signs and the its difference with the euclidian distance of the translated sign. Preferrably this standardized number would be the farthest euclidian distance for a translated sign found.
