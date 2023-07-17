import pandas as pd
import matplotlib.pyplot as plt
import csv


df = pd.read_csv('prices.csv')

df['date'] = pd.to_datetime(df['date'])

df['adjusted'] = df['adjusted'].astype('float')

df.plot.bar(x='adjusted', y='date')

plt.title('Valores Atualizados')

plt.show()
