import pandas as pd
import matplotlib.pyplot as plt

# Read the sales data from CSV
df = pd.read_csv("sales.csv")

plt.figure(figsize=(8, 5))
plt.scatter(df["month_number"], df["toothpaste"], color="red", marker="o")
plt.xlabel("Month")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales Per Month")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df["month_number"] - 0.2, df["facecream"], width=0.4, label="Face Cream", color="blue")
plt.bar(df["month_number"] + 0.2, df["facewash"], width=0.4, label="Face Wash", color="green")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Face Cream & Face Wash Sales Per Month")
plt.xticks(df["month_number"])
plt.legend()
plt.show()
total_sales = df[["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]].sum()
plt.figure(figsize=(8, 8))
plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%", startangle=140, colors=["blue", "green", "red", "purple", "orange", "pink"])
plt.title("Total Sales of Each Product Over the Year")
plt.show()
