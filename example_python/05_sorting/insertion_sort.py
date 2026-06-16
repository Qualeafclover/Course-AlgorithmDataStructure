"""insertion_sort.py

-----------------------------------------------------------------------
挿入ソートのサンプルプログラム。

このプログラムではランダムな配列に対して挿入ソートを実行しています。
"""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Insertion Sort Example")
    parser.add_argument(
        "--num",
        nargs="+",
        type=int,
        default=[15, 27, 3, 9, 30, 21, 6, 14, 33, 18],
        help="List of numbers to sort (default: %(default)s)",
    )
    return parser.parse_args()


# 挿入ソート
def insertion_sort(data):
    # 配列の長さ（データの数）を取得
    n = len(data)
    compare_count = 0  # 比較回数のカウンタ

    # 一番左（0番目）は最初から操作済みにするので
    # 1からループ開始
    for i in range(1, n):
        key = data[i]
        j = i - 1

        # keyを入れる位置（インデックス）を探す
        compare_count += 1  # 最初の比較
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            compare_count += 1

        data[j + 1] = key

    print(f"比較回数: {compare_count}")
    return data


if __name__ == "__main__":
    args = parse_args()
    data = args.num

    # ソート前の配列の表示
    print("ソート前:", data)

    # 挿入ソートの実行
    print("挿入ソートを実行します。")
    data = insertion_sort(data)

    # ソート後の配列の表示
    print("ソート後:", data)


# ある程度整列されているデータ
# python3 insertion_sort.py --num 2 1 3 5 4 6 7 9 8 10
# 比較回数: 12

# 逆順に並んでいるデータ
# python3 insertion_sort.py --num 10 9 8 7 6 5 4 3 2 1
# 比較回数: 54

# 完全にランダムなデータ
# python3 insertion_sort.py --num 1 5 3 8 2 7 4 10 6 9
# 比較回数: 21

# 全て同じ値のデータ
# python3 insertion_sort.py --num 5 5 5 5 5 5 5 5 5 5
# 比較回数: 9
