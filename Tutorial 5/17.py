import pandas as pd

df = pd.read_csv("student.csv")

avg_cgpa = df["CGPA"].mean()
print("Average CGPA:", round(avg_cgpa, 2))

print("\nStudents with CGPA > 9:")
print(df[df["CGPA"] > 9])

print("\nCSE Students with CGPA > 9:")
print(df[(df["Branch"] == "CSE") & (df["CGPA"] > 9)])

max_cgpa_student = df.loc[df["CGPA"].idxmax()]
print("\nStudent with Maximum CGPA:")
print(max_cgpa_student)

avg_cgpa_branch = df.groupby("Branch")["CGPA"].mean()
print("\nAverage CGPA by Branch:")
print(avg_cgpa_branch)
