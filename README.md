# jp_citycode

総務省が提供する全国地方公共団体コードをJSON形式に変換する

- カーリル内部で使われていたコードを分離・継続的に管理する予定
- Python 3.14 / [uv](https://docs.astral.sh/uv/) に対応
- https://www.soumu.go.jp/denshijiti/code.html
  （※読み込むTSVファイルはエクセルデータをテキストにコピーしたもの）

## 使い方

```sh
uv sync
uv run convert.py data/20240101.tsv data/20240101.json
```
