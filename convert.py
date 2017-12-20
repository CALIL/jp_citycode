#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
総務省が提供する全国地方公共団体コードをJSON形式に変換する
http://www.soumu.go.jp/denshijiti/code.html
（※読み込むTSVファイルはエクセルデータをテキストにコピーしたもの）
"""

__copyright__ = "Copyright (C) 2017 CALIL Inc."
__author__ = "Ryuuji Yoshimoto <ryuuji@calil.jp>"

import click
import json
import unicodedata

DATA_VERSION = '1'


@click.command()
@click.argument('input', type=click.File('r', encoding='utf-8'))
@click.argument('output', type=click.File('wb'))
def run(input, output):
    data = input.read()
    result = []
    for line in data.split('\n'):
        cols = line.split('\t')
        if len(cols) == 5 and cols[0].isdigit():
            # 団体コード	"都道府県名（漢字）"	"市区町村名（漢字）"	"都道府県名（カナ）"	"市区町村名（カナ）"
            result.append({'code': unicodedata.normalize('NFKC', cols[0]).strip(),
                           'pref': unicodedata.normalize('NFKC', cols[1]).strip(),
                           'city': unicodedata.normalize('NFKC', cols[2]).strip(),
                           'pref_kana': unicodedata.normalize('NFKC', cols[3]).strip(),
                           'city_kana': unicodedata.normalize('NFKC', cols[4]).strip()})

    output.write(json.dumps({'title': 'jp_citycode', 'version': DATA_VERSION, 'table': result}, ensure_ascii=False).encode("utf-8"))
    click.echo('%d件処理しました' % len(result))


run()
