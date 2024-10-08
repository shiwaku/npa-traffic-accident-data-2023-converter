# npa-traffic-accident-data-2023-converter
## プログラムについて
- 本プログラムは、警察庁が公開している、[交通事故統計情報のオープンデータ](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)の[2023年の本票](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/2023/opendata_2023.html)を[コード表](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/2023/opendata_2023.html)をもとに読みやすい形式（GISデータ）に変換するプログラムになります。
- Pythonで構築

### csvfile-to-degree.py
- 本票CSVファイル（2023年）の「地点　緯度（北緯）」と「地点　経度（東経）」を十進法度単位に変換するプログラムになります。
- 文字コードをUTF-8に変換します。

#### 使用データ
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/data/honhyo_2023.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/data/honhyo_2023.csv),64.3MB

#### 出力結果
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_to-degree.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_to-degree.csv),75.6MB  

### csvfile-convert.py
- 十進法度単位に変換した本票CSVファイル（2023年）をコード表をもとに読みやすいデータに変換するプログラムになります。

#### 使用データ
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_to-degree.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_to-degree.csv),75.6MB
- コード表：[https://github.com/shiwaku/npa-traffic-accident-data-2023-converter/tree/main/code](https://github.com/shiwaku/npa-traffic-accident-data-2023-converter/tree/main/code)

hit.csv is based on https://github.com/code4fukui/traffic-accident Thanks!

#### 出力結果
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_convert.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_convert.csv),234.0MB  

### csvfile-merge.py
- 2019-2022年のデータと2023年のデータをマージするプログラムになります。
- 2019-2021年のデータの変換ツールは[こちらのリポジトリ](https://github.com/shiwaku/npa-traffic-accident-data-converter)を参照してください。
- 2022年のデータの変換ツールは[こちらのリポジトリ](https://github.com/shiwaku/npa-traffic-accident-data-2022-converter)を参照してください。

#### 使用データ
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_convert_v2.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_convert_v2.csv),722.4MB  
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_convert.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_convert.csv),227.4MB
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_convert.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2023_convert.csv),234.0MB  

#### 出力結果
**2019～2023年のデータをマージしたデータになります（5年間で約160万件）。**
##### CSV形式
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.csv](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.csv),1.2GB  
##### GeoParquet形式
※[GDAL/OGR(OSGeo4W)](https://trac.osgeo.org/osgeo4w/)でGeoParquet形式に変換しています
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.parquet](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.parquet),154MB
##### PMTiles形式
※[felt/tippecanoe](https://github.com/felt/tippecanoe)でPMTiles形式に変換しています
- [https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.pmtiles](https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2023_convert.pmtiles),313MB

## デモサイト（MapLibre GL JS）
- https://shiwaku.github.io/npa-traffic-accident-map-on-maplibre/
- 使用データ：交通事故統計情報のオープンデータ（2019年、2020年、2021年、2022年、2023年）の本票（PMTiles形式）

## 使用データ及び出力結果のライセンスについて
本データセットは[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは交通事故統計情報のオープンデータ（2019、2020、2021、2022、2023年）の本票を加工して作成したものです。本データセットの使用・加工にあたっては、[警察庁Webサイトの利用規約](https://www.npa.go.jp/rules/index.html)を必ずご確認ください。

## 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
