# npa-traffic-accident-data-2023-converter

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/deed.ja)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

警察庁が公開している[交通事故統計情報のオープンデータ](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)の[2023 年の本票](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/2023/opendata_2023.html)を、[コード表](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/2023/opendata_2023.html)をもとに読みやすい形式（GIS データ）に変換するプログラムです。

## 実行環境

- Python 3.8 以上

## 使い方

以下の順序でスクリプトを実行します。

```
Step 1: csvfile-to-degree.py   # 緯度経度を10進数に変換・文字コードをUTF-8に変換
         ↓ honhyo_2023_to-degree.csv
Step 2: csvfile-convert.py     # コード表をもとに値を読みやすい形式に変換
         ↓ honhyo_2023_convert.csv
Step 3: csvfile-merge.py       # 2019〜2023年のデータをマージ（任意）
         ↓ honhyo_2019-2023_convert.csv
```

---

## Step 1: csvfile-to-degree.py

本票 CSV（Shift-JIS）の「地点　緯度（北緯）」と「地点　経度（東経）」を 60 進数から 10 進数度（decimal degrees）に変換し、文字コードを UTF-8 に変換します。

### 入力データ

`./data/` フォルダに以下のファイルを配置してください。

| ファイル | サイズ | ダウンロード |
|---------|--------|-------------|
| `honhyo_2023.csv` | 64.3 MB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/data/honhyo_2023.csv) |

### 実行

```bash
python csvfile-to-degree.py
```

### 出力

| ファイル | サイズ |
|---------|--------|
| `honhyo_2023_to-degree.csv` | 75.6 MB |

---

## Step 2: csvfile-convert.py

Step 1 の出力ファイルをコード表をもとに読みやすい値に変換します（都道府県名、路線名、天候、事故類型など）。

### 入力データ

Step 1 の出力ファイル（`honhyo_2023_to-degree.csv`）とコード表（`code/` フォルダ）を使用します。

| ファイル | サイズ | ダウンロード |
|---------|--------|-------------|
| `honhyo_2023_to-degree.csv` | 75.6 MB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_to-degree.csv) |

> コード表の「車両の衝突部位」は [Code for FUKUI](https://github.com/code4fukui/traffic-accident) が作成したコード値表を使用しています。

### 実行

```bash
python csvfile-convert.py
```

### 出力

| ファイル | サイズ |
|---------|--------|
| `honhyo_2023_convert.csv` | 234.0 MB |

---

## Step 3: csvfile-merge.py（任意）

2019〜2023 年の変換済みデータをマージします。

### 入力データ

`./csv/` フォルダに以下のファイルを配置してください。

| ファイル | サイズ | ダウンロード |
|---------|--------|-------------|
| `honhyo_2019-2021_convert_v2.csv` | 722.4 MB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_convert_v2.csv) |
| `honhyo_2022_convert.csv` | 227.4 MB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_convert.csv) |
| `honhyo_2023_convert.csv` | 234.0 MB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_convert.csv) |

> 2019〜2021 年の変換ツール：[npa-traffic-accident-data-converter](https://github.com/shiwaku/npa-traffic-accident-data-converter)
> 2022 年の変換ツール：[npa-traffic-accident-data-2022-converter](https://github.com/shiwaku/npa-traffic-accident-data-2022-converter)

### 実行

```bash
python csvfile-merge.py
```

### 出力

**2019〜2023 年のデータをマージしたデータ（5 年間、約 160 万件）**

| 形式 | ファイル | サイズ | ダウンロード |
|------|---------|--------|-------------|
| CSV | `honhyo_2019-2023_convert.csv` | 1.2 GB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.csv) |
| GeoParquet | `honhyo_2019-2023_convert.parquet` | 154 MB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.parquet) |
| PMTiles | `honhyo_2019-2023_convert.pmtiles` | 313 MB | [ダウンロード](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.pmtiles) |

GeoParquet への変換は [GDAL/OGR (OSGeo4W)](https://trac.osgeo.org/osgeo4w/) を使用。

```bash
# CSVからGeoParquetの作成
ogr2ogr -f "Parquet" honhyo_2019-2023_convert.parquet honhyo_2019-2023_convert.csv -oo X_POSSIBLE_NAMES=地点_経度（東経）_10進数 -oo Y_POSSIBLE_NAMES=地点_緯度（北緯）_10進数 -s_srs EPSG:4326 -t_srs EPSG:4326

# CSVからGeoJSONの作成
ogr2ogr -f "GeoJSON" honhyo_2019-2023_convert.geojson honhyo_2019-2023_convert.csv -oo X_POSSIBLE_NAMES=地点_経度（東経）_10進数 -oo Y_POSSIBLE_NAMES=地点_緯度（北緯）_10進数 -s_srs EPSG:4326 -t_srs EPSG:4326
```

PMTiles への変換は [felt/tippecanoe](https://github.com/felt/tippecanoe) を使用。

```bash
# PMTilesの作成
tippecanoe -o honhyo_2019-2023_convert.pmtiles honhyo_2019-2023_convert.geojson -pf -pk -P -B12
```

---

## デモサイト

MapLibre GL JS を使った可視化デモ：[https://shiwaku.github.io/npa-traffic-accident-map/](https://shiwaku.github.io/npa-traffic-accident-map/)

使用データ：交通事故統計情報のオープンデータ（2019〜2024 年）の本票（PMTiles 形式）

---

## ライセンス

本データセットは [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) で提供されます。使用の際は本リポジトリへのリンクを提示してください。

本データセットは交通事故統計情報のオープンデータ（2019〜2023 年）の本票を加工して作成したものです。使用・加工にあたっては[警察庁 Web サイトの利用規約](https://www.npa.go.jp/rules/index.html)を必ずご確認ください。

## 免責事項

利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。

## 更新履歴

- **2026/04/08** バグ修正: 一時停止規制_表示（当事者B）のインデックス誤参照を修正

## 活用事例

- 秋田魁新報社 | 秋田の交通事故マップ：[https://www.sakigake.jp/special/maps/traffic-accident/](https://www.sakigake.jp/special/maps/traffic-accident/)
