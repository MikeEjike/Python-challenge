import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')
#csvreader = csv.reader(csvfile, delimiter=',')


with open(csvpath,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next(csvfile)

   
    total_months = 0
    net_total = 0

    # Monthly profit/Losses, when looped will count as the previous month when subtracted by the current month
    monthlyPL = 0
    
    # Amount change from current month to previous month
    changed_data = 0

    # Average Change
    average_change = 0

    # WIll be the greatest increases/decreases and month associated with
    greatest_increase = 0
    greatest_increase_month = 0
    greatest_decrease = 0
    greatest_decrease_month = 0

    # Monthly profit/loss data
    monthly_data = []

    # Previous month's profit/loss change list
    previous_change_over_period = []

    # Current month's profit/loss change list
    change_over_period = []

    for row in csvreader:
        
        


  
        total_months = total_months + 1  
        net_total = net_total + int(row[1])
        monthly_data.append(int(row[1])) 


        previous_change_over_period.append(changed_data)
        changed_data = int(row[1])-monthlyPL
        monthlyPL = int(row[1])
        change_over_period.append(changed_data) 
        

        average_change = '{0:.2f}'.format(sum(change_over_period) / len(change_over_period))
        greatest_increase = max(change_over_period)
        greatest_decrease = min(change_over_period)
        

        # Determines the month at which the change it at its greatest increase/deacrease
        if (changed_data == greatest_increase):
            greatest_increase_month = row[0]
        elif (changed_data == greatest_decrease):
            greatest_decrease_month = row[0]

    
    print('Financial Analysis \n---------------------------------\n')
    print(f'Total Months: {total_months}')
    print(f'Total : ${net_total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}')    

# Creating a new file and writing the results to that file
output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

analysis_file = open(output_path, 'w')

analysis_file.write('Financial Analysis \n---------------------------------\n')
analysis_file.write(f'Total Months: {total_months}\n')
analysis_file.write(f'Total : ${net_total}\n')
analysis_file.write(f'Average Change: ${average_change}\n')
analysis_file.write(f'Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}\n')
analysis_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}\n')     

analysis_file.close()  