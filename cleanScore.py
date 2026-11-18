import pandas as pd
import csv


df = pd.read_csv('gpPracticeScores.csv')

newFrame = df.filter(regex='pcteval|region')
print(newFrame.head())

newFrame.to_csv('cleanScores.csv', mode = 'a', header=True, index=False)