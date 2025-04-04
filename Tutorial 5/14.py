import csv

# Data to be written
header = ["Reg_no", "Name", "Sub_Mark1", "Sub_Mark2", "Sub_Mark3"]
rows = [
    [10001, "Jack", 76, 88, 76],
    [10002, "John", 77, 84, 79],
    [10003, "Alex", 74, 79, 81]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print("Data written successfully to 'students.csv'")
