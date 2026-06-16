"""quick_sort_hoare.py

-----------------------------------------------------------------------
クイックソートのサンプルプログラム。

このプログラムではランダムな配列に対してクイックソートを
実行しています。

※ このプログラムが講義動画で紹介している処理手順を実装し
たものです。

注意1：
このプログラムで紹介するクイックソートでは、追加の配列を
使用せず、対象のデータが格納された配列のみを用いて処理を
行います。この方式を in-place 方式と呼びます。

注意2：
このプログラムで紹介するクイックソートの処理は左右から中
央に向かって進み、pivotより小さいものは左へ、大きいものは
右へ入れ替えていく方法で処理を行い、pivotを基準に左右に分
割（partition）して整理を行います。この方式を
Hoare partition と呼びます。
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


# 左端を pivot にする in-place クイックソート
# Hoare partition 方式（シンプルな実装）
def quick_sort_hoare_left(data, left, right):
    compare_count = 0  # 比較回数のカウンタ
    if left >= right:
        return compare_count

    pivot = data[left]  # 左端を pivot にする
    i = left
    j = right

    while i < j:
        # 右から pivot より小さい値を探す
        while i < j and data[j] >= pivot:
            j -= 1
            compare_count += 1

        # 左から pivot より大きい値を探す
        while i < j and data[i] <= pivot:
            i += 1
            compare_count += 1

        if i < j:
            data[i], data[j] = data[j], data[i]

    # pivot を正しい位置へ
    data[left], data[i] = data[i], data[left]

    # 再帰的に左右の配列を処理
    compare_count += quick_sort_hoare_left(data, left, i - 1)
    compare_count += quick_sort_hoare_left(data, i + 1, right)
    return compare_count


# 右端を pivot にする in-place クイックソート
# Hoare partition 方式（シンプルな実装）
def quick_sort_hoare_right(data, left, right):
    if left >= right:
        return

    pivot = data[right]  # 右端を pivot にする
    i = left
    j = right

    while i < j:
        # 左から pivot より小さい値を探す
        while i < j and data[i] <= pivot:
            i += 1

        # 右から pivot より大きい値を探す
        while i < j and data[j] >= pivot:
            j -= 1

        if i < j:
            data[i], data[j] = data[j], data[i]

    # pivot を正しい位置へ移動
    data[right], data[i] = data[i], data[right]

    # 再帰的に左右の配列を処理
    quick_sort_hoare_right(data, left, i - 1)
    quick_sort_hoare_right(data, i + 1, right)


if __name__ == "__main__":
    args = parse_args()
    data = args.num

    # ソート前の配列の表示
    print("ソート前:", data)

    # クイックソート（左端pivot）の実行
    print("クイックソート（左端pivot）を実行します。")
    compare_count = quick_sort_hoare_left(data, 0, len(data) - 1)
    print(f"比較回数: {compare_count}")

    # ソート後の配列の表示
    print("ソート後:", data)

# ある程度整列されているデータ
# python3 quick_sort_hoare.py --num 2 1 3 5 4 6 7 9 8 10
# 比較回数: 31

# 完全にランダムなデータ
# python3 quick_sort_hoare.py --num 1 5 3 8 2 7 4 10 6 9
# 比較回数: 27
