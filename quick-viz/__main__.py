import pandas as pd
import pygwalker as pyg

df = pd.read_csv("quick-viz/sample_data/titanic_train.csv", encoding="utf-8")
viz = pyg.to_html(df)
with open("quick-viz/output/quick-viz.html", mode="w", encoding="utf-8") as f:
    f.write(viz)
