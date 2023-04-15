import os
import sys
import subprocess

# サードパーティー製ライブラリのインポート
try:
    import pandas as pd
    import pygwalker as pyg
except:
    print("エラー！'pip install pandas'と'pip install pygwalker'を実行してください。")
    sys.exit(1)


# 引数ありで実行されているか確認
is_argv = len(sys.argv) > 1

if is_argv:
    # 引数ありの場合
    input_path = sys.argv[1]
else:
    # 引数なしの場合、inputしてもらう
    print("csvファイルまたはxlsxファイルをドラッグして下さい。")
    input_path = input()

# 半角スペースやクォーテーションを削除
path = input_path.strip().strip("'")

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

# pygwalkerにdfを渡してhtml化
html = pyg.to_html(df)

# htmlのエンコーディング指定
header = """
<head>
<meta charset="utf-8">
</head>
"""
# header情報を追加
head = html.split("\n")[:2]
tail = html.split("\n")[2:]
html = ("\n").join(head) + header + ("\n").join(tail)

# 保存先を絶対パスで指定
path = os.path.abspath("quick-viz.html")
# htmlを出力
with open(path, mode="w", encoding="utf-8") as f:
    f.write(html)

# htmlをopen
subprocess.call(["open", path])


# if __name__ == "__main__":
#     main()
