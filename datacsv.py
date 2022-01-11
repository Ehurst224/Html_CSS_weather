import pandas as pd

data = pd.read_csv("cities.csv")

data.to_html("cities.html")