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

# Initialize a total vote counter
total_votes =0
# declare a candidate options list
candidate_options = []
# declare a dandidate votes dictionary
candidate_votes={}

#open the election results file and read the file
with open(file_to_load) as electoin_data:
    # to do read and analyze the data here
    file_reader= csv.reader(electoin_data)
    
    #read the header row
    #The .next() method returns the current row and moves to the next row.
    headers=next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        #print each candidate's name from each row with index
        candidate_name= row[2]

        # check if the candidate name is in the list
        if candidate_name not in candidate_options:
            #add the candidate name to the list
            candidate_options.append(candidate_name)
            # add the candidate name into the dictionary and start to track
            candidate_votes[candidate_name]=0
        #start to add votes to candidate_votes dict
        candidate_votes[candidate_name]+=1
        
#print total votes
#print(total_votes)
#print the candidate names
#print(candidate_votes)

#Winning candidate and winning votes count tracker
winning_candidate = ""
winning_count= 0
winning_percentage= 0
#determine the percentage of votes for each candidate by looping through the counts
# iterate through the candidate list
for candidate_name in candidate_options:
    #retrive vote count of a candidate from candidate votes dictionary
    votes=candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = (float(votes)/float(total_votes))*100
    #print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}%, ({votes:,})\n")
    
    #determine if votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count=votes
        winning_candidate= candidate_name
        winning_percentage = vote_percentage

#winning-candidate_summary message
winning_candidate_summary= (
    f"----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------\n"
)
print(winning_candidate_summary)