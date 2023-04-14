import os
import subprocess
import sys


try:
    import pandas as pd
    import pygwalker as pyg
except:
    print("エラー！'pip install pandas'と'pip install pygwalker'を実行してください。")
    sys.exit(1)


def main():
    # パスのread
    print("csvファイルまたはxlsxファイルをドラッグして下さい。")
    path = input().strip("'")

    # csvをread
    if ".csv" in path:
        try:
            df = pd.read_csv(path, encoding="utf-8")
        except:
            df = pd.read_csv(path, encoding="cp932")
    # xlsxをread
    elif ".xlsx" in path:
        df = pd.read_excel(path)
    else:
        print("エラー！対応していないファイル形式です。")
        sys.exit(1)

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
