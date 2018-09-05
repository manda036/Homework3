import os
import csv
net = 0
profloss = []
profitloss = os.path.join("budget_data.csv")
with open (profitloss, newline="") as pybank:
    monthlyanalysis = csv.reader(pybank, delimiter=",")
    next(monthlyanalysis, None)
    total_months = len(list(monthlyanalysis))
    first_row = next(monthlyanalysis)
    change = int(first_row[1])
    def change_in_profloss(change):
        return(int(row[1]-change))
    for row in monthlyanalysis:
        net += int(row[1])
        change_in_profloss(change)
        change = change_in_profloss(change)
    profloss.append(change)
    average_change = (sum(profloss)/int(len(profloss)))
    greatest_increase = max([value for value in profloss])
    greatest_decrease = min([value for value in profloss])
with open (profitloss, newline="") as pybank:
    monthlyanalysis = csv.reader(pybank, delimiter=",")
    next(monthlyanalysis, None)
    for row in monthlyanalysis:
        if int(row[1]) == greatest_increase:
            month1 = (row[0])
        if int(row[1]) == greatest_decrease:
            month2 = (row[0])

print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {month1} ${greatest_increase}")
print(f"Greatest Decrease: {month2} ${greatest_decrease}")