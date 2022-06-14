temperature = int(input("What is the temperature outside?"))
if temperature >80:
    print("Turn on AC")
else:
    print("Open the window")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    message = (f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")
    print(message)

# The data we need to retrieve
# 1.The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election vsed on popular votes
import csv

# assign a variable for the file to load and the path
#file_to_load ='Resources/election_results.csv'
#open the election results and read the file
#election_data = open(file_to_load,'r')
#with open(file_to_load) as election_data:   
    # to do: perform analysis
    #print(election_data)
# close the file
# election_data.close()
import os
#file_to_load = os.path.join('Resources', 'election_results.csv')
#with open(file_to_load) as election_data:
 #   print(election_data)
# create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join('Analysis','election_analysis.txt')
#use the open () function with the "w" mode we will write data to the file
#open(file_to_save, "w") 

#create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join('Analysis', 'election_analysis.txt')

#use the open statement to open the file as a text file
#outfile = open(file_to_save, "w")
#write some data to the file
#outfile.write("this is the first line of text in the file")

# close the file
#outfile.close()

file_to_save = os.path.join('Analysis', 'election_analysis.txt')
with open(file_to_save,"w") as outfile:
    outfile.write("Counties in the Election: ")
    outfile.write("\n------------------------------")
    outfile.write('\nArapahoe\nDenver\nJefferson')
