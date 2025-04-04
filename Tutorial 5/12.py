import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6]
facecream_sales = [2500, 2630, 2140, 3400, 3600, 2760]
facewash_sales = [1500, 1200, 1340, 2300, 2600, 1980]

plt.plot(months, facecream_sales, label="Face Cream", color="blue", marker="o")
plt.plot(months, facewash_sales, label="Face Wash", color="green", marker="s")

plt.title("Product Sales Over Months")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")

plt.legend()

plt.grid(True)

# Display the plot
plt.show()
