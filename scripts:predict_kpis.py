import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("revenue_history.csv")

X = df[["month_index"]]
y = df["revenue"]

model = LinearRegression()
model.fit(X, y)

future = pd.DataFrame({"month_index": [13,14,15]})
forecast = model.predict(future)

print("Next Quarter Forecast:", forecast)
