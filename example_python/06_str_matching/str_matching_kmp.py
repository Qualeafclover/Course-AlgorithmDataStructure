"""str_matching_kmp.py

-----------------------------------------------------------------------
KMP法による文字列パターン照合のサンプルプログラム。

このプログラムではテキスト中にパターンの文字列が現れるかどうか
をKMP法で探索するプログラムを実装しています。
"""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="KMP法による文字列パターン照合のサンプルプログラム")
    parser.add_argument("--text", type=str, default="ababcabcabababdabababcabababdababd", help="テキスト文字列")
    parser.add_argument("--pattern", type=str, default="ababca", help="パターン文字列")
    return parser.parse_args()


# ずらし表を作成する関数
# LPS（Longest Prefix Suffix）配列と呼ばれる
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0  # 直前までの最長接頭辞＝接尾辞の長さ
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# KMP法による文字列パターン照合
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    print("LPS:", lps)
    print("Shift table:", [1] + [i - lps[i - 1] for i in range(1, m)])
    
    result = []

    i = 0  # text側
    j = 0  # pattern側

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


if __name__ == "__main__":
    args = parse_args()
    text = args.text
    pattern = args.pattern

    # テキストとパターンの表示
    print(f"text   : {text}")
    print(f"pattern: {pattern}")

    # 文字列の探索
    print("KMP法で文字列を探索します。")
    search_result = kmp_search(text, pattern)

    # 結果の表示
    if len(search_result) > 0:
        for sr in search_result:
            print(f"該当箇所: {sr} 文字目")
    else:
        print("該当なし")


# # ---------------------------------------------------------------------
# # テキストとパターンの定義
# text = "ababcabcabababdabababcabababdababd"
# pattern = "ababd"
# print(f"text   : {text}")
# print(f"pattern: {pattern}")

# # 文字列の探索
# print("KMP法で文字列を探索します。")
# search_result = kmp_search(text, pattern)

# # 結果の表示
# if len(search_result) > 0:
#     for sr in search_result:
#         print(f"該当箇所: {sr} 文字目")
# else:
#     print("該当なし")
