import pandas as pd
import pygwalker as pyg

df = pd.read_csv("quick-viz/sample_data/titanic_train.csv", encoding="utf-8")
viz = pyg.to_html(df)

header = """
<head>
<meta charset="utf-8">
</head>
"""

head = viz.split("\n")[:2]
tail = viz.split("\n")[2:]
viz = ("\n").join(head) + header + ("\n").join(tail)

with open("quick-viz/output/quick-viz.html", mode="w", encoding="utf-8") as f:
    f.write(viz)
