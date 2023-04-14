import os
import pandas as pd
import pygwalker as pyg
import subprocess

print("csvファイルをドラッグして下さい")
path = input()[1:-1]

try:
    df = pd.read_csv(path, encoding="utf-8")
except:
    df = pd.read_csv(path, encoding="CP932")
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

subprocess.call(["open", path])
