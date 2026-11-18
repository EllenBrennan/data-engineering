import pandas as pd
import csv


df = pd.read_csv('gpPracticeScores.csv')

newFrame = df.filter(regex='pct|region')
print(newFrame.head())

newFrame.to_csv('cleanScores.csv', mode = 'a', header=True, index=False)