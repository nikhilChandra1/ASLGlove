# ASLGlove

Download Arduino and Putty

Putty inputs all data to test.txt, so change the file path in putty to test.txt
Also change port number on Putty based on the port shown from Arduino>Tools>Port

All the averages.txt files were used for data collection, and createFinalAverages would find the averages to then be used to find the averages for each data marker which was then compared to averages found from a live translation.

run GetAllData for arduino data collection

run testAverage.py to append the averages of each sign to the averages.txt files

run createFinalAverages to get the final average for each data marker based on the averages.txtfiles

run the euclidianDistanceTranslationAlgorithm at the end of conducting a sign to get a translation

If averages for each data marker are being found again remember to change the averages in the euclidianDistanceTranslationAlgorithm.py and normalize them again. Normalize them using the normalization formula with the highest and lowest values found from the data marker averages of the signs which will already be in the arrays created from createFinalAverages and in the euclidianDistanceTranslationAlgorithm.py
