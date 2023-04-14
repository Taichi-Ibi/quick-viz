import os
import pandas as pd
import pygwalker as pyg
import webbrowser

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

path = os.path.abspath("quick-viz/output/quick-viz.html")

with open(path, mode="w", encoding="utf-8") as f:
    f.write(viz)

webbrowser.open(path)