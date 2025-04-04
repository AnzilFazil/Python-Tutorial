import pandas as pd

df = pd.read_csv("employee.csv")

print("First 7 Records:")
print(df.head(7))
print("\nEmployee Names (Alphabetical):")
print(df["name"].sort_values())

highest_paid = df.loc[df["salary"].idxmax(), "name"]
print("\nEmployee with Highest Salary:", highest_paid)

print("\nMale Employees:")
print(df[df["gender"] == "M"]["name"])

print("\nTeams Employees Belong To:")
print(df["team"].unique())
