import os
import csv


csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')
#csvreader = csv.reader(csvfile, delimiter=',')


with open(csvpath,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csvheader = next(csvfile)
    # csvheader2 = next(csvfile)

    # date = csvreader[0]
    # total_months = int(len(csvreader[0]))
    # profit_losses = csvreader[1]

    # net_total = 0
    # for income in csvreader[1]:
    #     net_total = net_total + income 
        
    # average_change = net_total/total_months
        
    # Read each row of data after the header
   
    total_months = 0
    net_total = 0
    net_total2 = 0
    changed_data = []
    change_over_period = 0
    for row in csvreader:
        
        


  
        total_months = total_months + 1  
        net_total = net_total + float(row[1])
        # for row2 in csvreader:

        #     net_total2 = (increase + 1) - increase
        #     # changed_data.append(change_over_period)        

    

        # print(f'{total_months})
    #total_months = len(row[0])
    #profit_losses = row[1]         
    
    
    print('Financial Analysis')
    print(f'Total Months: {total_months}')
    print(f'Total : ${net_total}')
    






    csvheader2 = next(csvfile)

    total_months = 0
    net_total = 0
    net_total2 = 0
    changed_data = []
    change_over_period = 0
    for row in csvreader:
        
        


  
        total_months = total_months + 1  
        net_total = net_total + float(row[1])
        # for row2 in csvreader:

        #     net_total2 = (increase + 1) - increase
        #     # changed_data.append(change_over_period)        

    

        # print(f'{total_months})
    #total_months = len(row[0])
    #profit_losses = row[1]         
    
    print(csvheader2)
    print('Financial Analysis')
    print(f'Total Months: {total_months}')
    print(f'Total : ${net_total}')
    

    # print(f'Average Change: {average_change}')
    # print(f'Greatest Increase in Profits: {greatest_increase}')
    # print(f'Greatest Decrease in Profits: {greatest_decrease}')
    # for i in csvreader:
    #     print(i)




        # changed_data = []
        # change_over_period = 0
        # for increase in csvreader:
        #     change_over_period = (increase + 1) - increase
        #     changed_data.append(change_over_period)
    
        # greatest_increase = max(changed_data)
        # greatest_decrease = min(changed_data)

######################################################################
    # def python_analysis(csvreader):
    #     date = csvreader[0]
    #     total_months = int(len(csvreader[0]))
    #     profit_losses = csvreader[1]
        
    #     net_total = 0
    #     for income in csvreader[1]:
    #         net_total = net_total + income 
        
    #     average_change = net_total/total_months
        
        
    #     changed_data = []
    #     change_over_period = 0
    #     for increase in csvreader:
    #         change_over_period = (increase + 1) - increase
    #         changed_data.append(change_over_period)
        
    #     greatest_increase = max(changed_data)
    #     greatest_decrease = min(changed_data)

    #     print('Financial Analysis')
    #     print(f'Total Months: {total_months}')
    #     print(f'Average Change: {average_change}')
    #     print(f'Greatest Increase in Profits: {greatest_increase}')
    #     print(f'Greatest Decrease in Profits: {greatest_decrease}')

    # python_analysis(csvreader)