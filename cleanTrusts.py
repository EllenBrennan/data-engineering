import pandas as pd

h = ["orgCode", "name", "NHSER", "ICB", "addr1", "addr2", "addr3", "town", "county", "postcode", "startdt", "enddt", "A", "B",  "C", "D", "E", "tele", "F", "G", "H", "1", "I", "GOR", "J", "K", "L", "M"]
df = pd.read_csv("etr.csv", header=None, names=h)
df.to_csv("trusts.csv", index=False)