import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/pritp/Desktop/internship_file/zomato_sample_dataset.csv")

cuisines = df['Cuisines'].str.split(', ').explode()
top_cuisines = cuisines.value_counts().head(10)

print("Top 10 Popular Cuisines:")
print(top_cuisines)

top_cuisines.plot(kind='bar', figsize=(8,5))
plt.title('Top 10 Popular Cuisines')
plt.xlabel('Cuisine')
plt.ylabel('Number of Restaurants')
plt.show()