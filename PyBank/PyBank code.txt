import os
import csv
net = 0
total_months = 0
profloss = []
greatest_increase, greatest_decrease = 0, 0
difference = 0
month1 = ""
month2 = ""
profitloss = os.path.join("budget_data.csv")
with open (profitloss, newline="") as pybank:
    monthlyanalysis = csv.reader(pybank, delimiter=",")
    next(monthlyanalysis, None)
    total_months +=1
    first_row = next(monthlyanalysis)
    change = int(first_row[1])
    net = int(first_row[1])
    def change_in_profloss(change):
        return((int(row[1]))-change)
    for row in monthlyanalysis:
        total_months +=1
        net += int(row[1])
        difference = change_in_profloss(change)
        change = int(row[1])
        profloss.append(difference)
        if difference >= greatest_increase:
            greatest_increase = difference
            month1 = (row[0])
        elif difference <= greatest_decrease:
            greatest_decrease = difference
            month2 = (row[0])
    average_change = (sum(profloss)/int(len(profloss)))


print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {month1} ${greatest_increase}")
print(f"Greatest Decrease: {month2} ${greatest_decrease}")