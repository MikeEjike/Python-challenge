import os
import csv



csvpath = os.path.join('Resources', 'election_data.csv')



with open(csvpath,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next(csvfile)

   
    total_votes = 0
    
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    khan_percentage = 0
    correy_percentage = 0
    li_percentage = 0
    otooley_percentage = 0

    current_candidate = 0
    previous_candidate = 0

    candidates = []
    candidate_names = []
    
    for row in csvreader:
        total_votes = total_votes + 1


        current_candidate = row[2]

        
        # This function helped me find the unique candidates within the csv file
        def unique(names):
            unique_names = []
            for x in names:
                if x not in unique_names:
                    unique_names.append(x)
            for x in unique_names:
                print(x)
        
            
        # Compares the previous candidate with the current one so the function can differentiate between unique values
        if (current_candidate != previous_candidate):
            candidate_names.append(row[2])


        previous_candidate = row[2]

        # This counts the total votes per candidate
        if row[2] == "Khan":
            khan_count = khan_count + 1
        elif row[2] == "Correy":
            correy_count = correy_count + 1
        elif row [2] == "Li":
            li_count = li_count + 1
        elif row [2] == "O'Tooley":
            otooley_count = otooley_count + 1
    
    # This shows the percentage each candidate received from the total votes 
    khan_percentage = '{0:.3f}'.format(round((khan_count / total_votes) * 100))
    correy_percentage = '{0:.3f}'.format(round((correy_count / total_votes) * 100))
    li_percentage = '{0:.3f}'.format(round((li_count / total_votes) * 100))
    otooley_percentage = '{0:.3f}'.format(round((otooley_count / total_votes) * 100))


    candidates.append(["Khan","Correy","Li","O'Tooley"])


    print('Election Results \n-------------------------')
    print(f'Total Votes: {total_votes}\n-------------------------')
    print(f'{candidates[0][0]}: {khan_percentage}% ({khan_count})')
    print(f'{candidates[0][1]}: {correy_percentage}% ({correy_count})')
    print(f'{candidates[0][2]}: {li_percentage}% ({li_count})')
    print(f'{candidates[0][3]}: {otooley_percentage}% ({otooley_count})\n-------------------------')
    print(f'Winner: {candidates[0][0]}')



# Creating a new file and writing the results to that file
output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")

analysis_file = open(output_path, 'w')

analysis_file.write('Election Results \n-------------------------\n')
analysis_file.write(f'Total Votes: {total_votes}\n-------------------------\n')
analysis_file.write(f'{candidates[0][0]}: {khan_percentage}% ({khan_count})\n')
analysis_file.write(f'{candidates[0][1]}: {correy_percentage}% ({correy_count})\n')
analysis_file.write(f'{candidates[0][2]}: {li_percentage}% ({li_count})\n')
analysis_file.write(f'{candidates[0][3]}: {otooley_percentage}% ({otooley_count})\n-------------------------\n')
analysis_file.write(f'Winner: {candidates[0][0]}')

analysis_file.close()  