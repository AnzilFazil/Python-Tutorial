import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stud.csv")
print("Student Data:\n", df)

df.set_index("rollno", inplace=True)
print("\nData with rollno as index:\n", df)

print("\nName and Mark Columns:\n", df[["name", "mark"]])

sorted_by_name = df.sort_values("name")[["name", "mark"]]
print("\nSorted by Name:\n", sorted_by_name)

sorted_by_mark = df.sort_values("mark", ascending=False)[["name", "mark"]]
print("\nSorted by Mark (Descending):\n", sorted_by_mark)

print("\nStatistics of Marks:")
print("Average Mark:", df["mark"].mean())
print("Median Mark:", df["mark"].median())
print("Mode Mark:", df["mark"].mode()[0])  

print("\nMinimum Mark:", df["mark"].min())
print("Maximum Mark:", df["mark"].max())

print("\nVariance of Marks:", df["mark"].var())
print("Standard Deviation of Marks:", df["mark"].std())

plt.hist(df["mark"], bins=5, color="blue", edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Student Marks")
plt.show()

df.drop(columns=["place"], inplace=True)
print("\nData after removing 'place' column:\n", df)
