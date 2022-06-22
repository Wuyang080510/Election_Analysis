Use Python to Perform the Election Audit

# Election_Analysis

## Overview
In this project I was asked to go through the election data and perform election audit for the Colorado Board of Election with Python. 
### Purpose
Use Python to extract and analyze data from the election result csv file, use csv and os libraries to read and load data from csv file and write data into a text file. 
I will determine the election winner and the county with the most votes, output the results to a text file and print the results in the terminal with the Python script.
Finally, I will use GitBash to push the election audit results and resources to my GitHub repository.

## Election-Audit Results
- Total number of votes cast: 369,711 votes

- Election audit results by county:
    * Jefferson: 10.5% (38,855)
    * Denver: 82.8% (306,055)
    * Arapahoe: 6.7% (24,801)
  
  Denver county got the largest number of votes. Its votes are around five times more than the total votes received by Jefferson county and Arapahoe county. 
  The following image shows the code I used to extract and print out the election results for each county and the name of the county with the largest number   of votes. 
  
   
- Election audit results by candidate:
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606)

  Diana DeGette in Jefferson county is the winner of this election event. She got 272,892 votes, which is 73.8% of the total votes. 
  The following image shows the code I used to extract and print out the name of the candidate with the largest number of votes and the highest percentage of   the vote. 



## Election-Audit Summary
This Python election result audit project turns election audit into an automatic process. The script can be applied to different election districts and get election results in just a few minutes. 
To apply the code to other election districts, the election commission should first format the future election result file as the election_restults.csv file to use the same index numbers used in the code.  
Then, they need to modify the path to load new election result files and use a new path to save the election analysis results. 

### A Further Step
A further step could be taken is giving a breakdown of the vote sources of each candidate. This way, we know which county is the biggest supporter OF each candidate. 
Another application for this election analysis script could be a deeper analysis of the election data. For example, use for loop and if statement to get election results for states, or run analysis to show the votes received by each candidate based on different parties. 
