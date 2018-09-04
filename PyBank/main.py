import os
import csv
net = 0
profitloss = os.path.join("budget_data.csv")
with open (profitloss, newline="") as pybank:
    monthlyanalysis = csv.reader(pybank, delimiter=",")
    next(monthlyanalysis, None)
    profloss = []
    change = int(row[1])
    for row in monthlyanalysis:
        net += int(row[1])
        def change_in_profloss(profloss):
           return(change = int(row[1]-change))
        profloss.append(change)
    average_change = (sum(profloss)/int(len(profloss)))

print("Financial Analysis")
print("--------------------------------")
#print(f"Total Months: {total_months}"")
print(f"Total: ${net}")
print(f"Average Change: ${average_change}")
       
        
