# Google-Vision-inline-text-rectifier
## Problem: 
Font mismatch causes word level bounding boxes to vary in height within a sentence. Google vision may interpret a word with higher height as belonging to an upper line than original and vice versa. This repo aims towards solving this problem
## Main Idea: 
Connect the two bounding boxes whose centroids is differs less than the average word length. This can be achived using both two methods.<br>
The first method is a dsu based approach where you can treat each word's centroid as a node and find connected component.<br>
The second is using an unsupervised learning algorithm to cluster words based on their centroids y-coordinates.

## Before Rectification:

Invoice Number:  <a>
3404
====================================================================================================
POS: 
====================================================================================================
01/21/2019 
Invoice Date: 

====================================================================================================
Payment $61 Due: 

====================================================================================================
$2,644.18 
Amount Due (USD): 

====================================================================================================

## After Rectification:

Invoice Number: <a>
3403 
====================================================================================================
POS: 
====================================================================================================
Invoice Date: 
01/21/2019 
====================================================================================================
Payment Due: 
610U/COVEO 
====================================================================================================
Amount Due (USD): 
$2,644.18 
====================================================================================================
