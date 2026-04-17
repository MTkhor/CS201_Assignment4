import pandas as pd
import matplotlib.pyplot as plt

#Reading data
df = pd.read_csv('random_walk.csv')


df["distance"] = (df["x"] ** 2 + df["y"]**2)**0.5

# analysing distance
stats = df["distance"].describe()
print(f"The greatest distance was: {stats['max']}, the average: {stats['mean']}.")

# filtering by distance
filtered_data = df[df["distance"] > stats["mean"]]
print(filtered_data)

filtered_data.to_json("filtered_walk.json")


# Plotting data
first_point = [df["x"][0], df["y"][0]]
last_point = [df["x"][len(df) - 1], df["y"][len(df) - 1]]

plt.figure(figsize=(12, 6))
plt.plot(df["x"], df["y"], color='pink', marker='none', linestyle='-', label="random wak trajectory")
plt.plot(first_point[0], first_point[1], color='red', marker='$\heartsuit$', linestyle='none', label="starting point")
plt.plot(last_point[0], last_point[1], color='purple', marker='$\heartsuit$', linestyle='none', label="ending point")
plt.title("Random walk example")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.grid(True)
plt.legend()
plt.show()