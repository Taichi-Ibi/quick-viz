import os
import subprocess

import pandas as pd
import pygwalker as pyg


def main():
    # パスのリード
    print("csvファイルをドラッグして下さい。")
    path = input().strip("'")

    # csvの判定
    assert ".csv" in path, "csvファイルではありません。"

    # csvをread
    try:
        df = pd.read_csv(path, encoding="utf-8")
    except:
        df = pd.read_csv(path, encoding="cp932")

    # pyg walkerをhtml化
    viz = pyg.to_html(df)

    # htmlのエンコーディング指定
    header = """
    <head>
    <meta charset="utf-8">
    </head>
    """
    # header情報を追加
    head = viz.split("\n")[:2]
    tail = viz.split("\n")[2:]
    viz = ("\n").join(head) + header + ("\n").join(tail)

    # 保存先を絶対パスで指定
    path = os.path.abspath("quick-viz.html")

    # htmlを出力
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(viz)

    # htmlをopen
    subprocess.call(["open", path])


if __name__ == "__main__":
    main()
