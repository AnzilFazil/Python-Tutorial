import pandas as pd

df = pd.read_csv("auto.csv")

df.dropna(inplace=True)

most_expensive = df.loc[df["price"].idxmax(), "company"]
print("Most expensive car company:", most_expensive)

toyota_cars = df[df["company"].str.lower() == "toyota"]
print("\nToyota Cars:")
print(toyota_cars)

car_counts = df["company"].value_counts()
print("\nTotal cars by company:")
print(car_counts)

# 5) Find the highest priced car of all companies
highest_priced_cars = df.loc[df.groupby("company")["price"].idxmax()]
print("\nHighest priced car of each company:")
print(highest_priced_cars[["company", "price"]])

avg_mileage = df.groupby("company")["average-mileage"].mean()
print("\nAverage mileage of all companies:")
print(avg_mileage)

sorted_cars = df.sort_values(by="price", ascending=False)
print("\nCars sorted by price:")
print(sorted_cars)

df.to_csv("cleaned_auto.csv", index=False)
print("\nCleaned data saved to 'cleaned_auto.csv'.")
