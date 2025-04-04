import pandas as pd

data = [
    [101, "Alice", 25],
    [102, "Bob", 30],
    [103, "Charlie", 22]
]

df = pd.DataFrame(data, columns=["ID", "Name", "Age"])

df.set_index("ID", inplace=True)

print(df)
