import pandas as pd
import json

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