#import modules
import os
import csv

#file path
budget=os.path.join("Resources","Lessons_03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")

#1. The total number of months included in the dataset: 86
months=[]
string=months

with open(budget, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     for row in csvreader:
        # Add month
        months.append(row[0])
        #print (months)        
index_months=[string.count(month) for month in months]
#print (index_months)
total_months=sum(index_months)
#print(total_months)


#2. The net total amount of "Profit/Losses" over the entire period: $38382578
pl=[]
total_pl=0

with open(budget, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     for row in csvreader:
        # Add profits and losses
        pl.append(int(row[1]))
        #print (pl)  
   
for  x in range(0, len(pl)):
        total_pl=total_pl + pl[x]
#print (total_pl)

#3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes: $-2315.12
change=[]

for  x in range(1, len(pl)):
        change.append(int(pl[x]- pl[x-1]))
#print (change)
average_change=sum(change)/len(change)
#print(average_change)


#4. The greatest increase in profits (date and amount) over the entire period: Feb-2012 ($1926159)
increase=max(change)
date_increase=months[(change.index(increase)+1)]
#print(months[24+1], increase)

#5. The greatest decrease in losses (date and amount) over the entire period: Sep-2013 ($-2196167)
decrease=min(change)
date_decrease=months[(change.index(decrease)+1)]
#print(change.index(decrease))
#print(months[43+1], decrease)

#6. Print the analysis to the terminal and export a text file with the results.
results= os.path.join("analysis","results.txt")
with open(results, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write ("-----------------------\n")
    outfile.write ("Total Months: " + str(total_months)+"\n")
    outfile.write("Total: $" + str(total_pl)+"\n")
    outfile.write ("Average Change: $" + str(average_change)+"\n")
    outfile.write("Greatest Increase in Profits:" +str(date_increase) +" ($" + str(increase) +")"+"\n")
    outfile.write ("Greatest Decrease in Profits:" +str(date_decrease) +" ($" + str(decrease) +")")
