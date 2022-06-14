# The data we need to retrieve
# 1.The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election vsed on popular votes
import csv
import os
# assign a variable to load a file from a path
file_to_load = os.path.join('Resources', 'election_results.csv')
# assign a variable to same a file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

#open the election results file and read the file
with open(file_to_load) as electoin_data:
    # to do read and analyze the data here
    file_reader= csv.reader(electoin_data)
    #read and print the header row
    headers=next(file_reader)
    print(headers)
    #print each row in the CSV file
    #for row in file_reader:
        #print(row)



    