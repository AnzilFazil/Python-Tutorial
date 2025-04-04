import pandas as pd

data = [
    [1, "Linus Torvalds", "Finland", "Linux Kernel", 1991],
    [2, "Tim Berners-Lee", "England", "World Wide Web", 1990],
    [3, "Guido van Rossum", "Netherlands", "Python", 1991]
]

df = pd.DataFrame(data, columns=["SN", "Name", "Country", "Contribution", "Year"])

df.to_csv("contributions.csv", index=False)

print("Data written to contributions.csv successfully!")
