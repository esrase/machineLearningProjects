import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



data = pd.read_csv("DailyDelhiClimateTrain.csv")
print(data.head())
print (data.describe())
print(data.info())

#mean temperature#
figure = px.line(data, x="date",
                 y="meantemp",
                 title='Mean Temperature in Delhi Over Years')
figure.show()
#humidity#
figure = px.line(data, x="date",
                 y="humidity",
                 title='')
figure.show()
#wind speed#
figure = px.line(data, x="date",
                 y="wind_speed",
                 title='Wind Speed in Delhi Over the Years')
figure.show()
# Temperature Change#
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="date", y="meantemp")
plt.title("Temperature Change Over Time")
plt.xlabel("date")
plt.ylabel("average temperature")
plt.show()

#temp-humidity#
figure = px.scatter(data_frame = data, x="humidity",
                    y="meantemp", size="meantemp",
                    trendline="ols",
                    title = "Relationship Between Temperature and Humidity")
figure.show()
#changing data type#
data["date"] = pd.to_datetime(data["date"], format = '%Y-%m-%d')
data['year'] = data['date'].dt.year
data["month"] = data["date"].dt.month
print(data.head())
#temp change#
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
plt.title("Temperature Change in Delhi Over the Years")
sns.lineplot(data = data, x='month', y='meantemp', hue='year')
plt.show()
# Temperature change over the years#
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="month", y="meantemp", hue="year", palette="viridis")
plt.title("Temperature Change by Years")
plt.xlabel("Month")
plt.ylabel("Average temperature")
plt.legend(title="Year")
plt.show()
