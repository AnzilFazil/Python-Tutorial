import pandas as pd

data = {
    "ID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22]
}

df = pd.DataFrame(data)

df.to_excel("output.xlsx", index=False)

print("Data written to output.xlsx successfully!")
