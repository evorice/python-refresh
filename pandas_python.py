import pandas as pd

df = pd.read_csv('pixel_cafe_sales.csv')
# print(df)

#1 inspect: shows the number of rows and columns
# print(df.shape)
# print(df.columns)

#2 select: display product + quantity together
# print(df[["Product", "Quantity"]])

#3 filter: display food rows
# food = df[df["Category"] == "Food"]
# print(food)

# busy = df[df["Quantity"] > 30]
# print(busy)

both = df[(df["Quantity"] > 30) & (df["Category"] == "Food")]
print(both)
