import pandas as pd
import pygwalker as pyg

df = pd.read_csv("quick-viz/sample_data/titanic_train.csv", encoding="utf-8")
print(pyg.to_html(df))
