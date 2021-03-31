
#import modules
import os
import csv

#file path
election=os.path.join("Resources","Lessons_03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")

#1. The total number of votes cast: 3521001
voters=[]

with open(election, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     for row in csvreader:
        # Add voters
        voters.append(row[0])           
total_voters=len(voters)
#print(total_voters)

#2. A complete list of candidates who received votes
candidates=[]

with open(election, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     for row in csvreader:
        # Add voters
        candidates.append(row[2])

unique=[]
for candidate in candidates:
         if candidate not in unique:
                unique.append(candidate)
#print(unique)

#3 & 4.The total number of votes each candidate won & The percentage of votes each candidate won

total_khan=candidates.count('Khan')
p_khan=total_khan/total_voters*100

total_correy=candidates.count('Correy')
p_correy=total_correy/total_voters*100

total_li=candidates.count('Li')
p_li=total_li/total_voters*100

total_tooley=candidates.count("O'Tooley")
p_tooley=total_tooley/total_voters*100

#5. The winner of the election based on popular vote.
total=[total_khan,total_correy,total_li,total_tooley]

for i in total:
        if max(total)==total_khan:
                winner="Khan"
        elif max(total)==total_correy:
                winner="Correy"
        elif max(total)==total_li:
                winner="Li"
        elif max(total)==total_tooley:
                winner="O'Tooley"
#print(winner)

#6. Final script should both print the analysis to the terminal and export a text file with the results.

print("Election Results")
print("------------------------------")
print ("Total Votes: " + str(total_voters))
print("------------------------------")
print("Khan:" + '%.3f'%p_khan + "%"+" " + "("+str(total_khan)+")")
print("Correy:" + '%.3f'%p_correy + "%"+" " + "("+str(total_correy)+")")
print("Li:" + '%.3f'%p_li + "%"+" " + "("+str(total_li)+")")
print("Khan:" + '%.3f'%p_tooley + "%"+" " + "("+str(total_tooley)+")")
print("------------------------------")
print ("Winner: "+ winner)
print("------------------------------")

results= os.path.join("analysis","results.txt")
with open(results, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write ("-----------------------\n")
    outfile.write ("Total Votes: " + str(total_voters)+"\n")
    outfile.write ("-----------------------\n")
    outfile.write ("Khan:" + '%.3f'%p_khan + "%"+" " + "("+str(total_khan)+")" +"\n")
    outfile.write ("Correy:" + '%.3f'%p_correy + "%"+" " + "("+str(total_correy)+")" +"\n")
    outfile.write ("Li:" + '%.3f'%p_li + "%"+" " + "("+str(total_li)+")" +"\n")
    outfile.write ("Khan:" + '%.3f'%p_tooley + "%"+" " + "("+str(total_tooley)+")"+"\n")
    outfile.write ("-----------------------\n")
    outfile.write ("Winner: "+ winner+"\n")
    outfile.write ("-----------------------\n")

  