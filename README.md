# npa-traffic-accident-data-2022-converter
## プログラムについて
- 本プログラムは、警察庁が公開している、[交通事故統計情報のオープンデータ（2022年）の本票](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/2022/opendata_2022.html)を[コード表](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/2022/opendata_2022.html)を元に読みやすいデータ（GISデータ）に変換するプログラムになります。
- Pythonで構築

### csvfile-to-degree.py
- 本票CSVファイル（2022年）の「地点　緯度（北緯）」と「地点　経度（東経）」を十進法度単位に変換するプログラムになります。
- 文字コードをUTF-8に変換します。

#### 使用データ
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/data/honhyo_2022.csv`,62.8MB

#### 出力結果
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_to-degree.csv`,73.8MB  

### csvfile-convert.py
- 十進法度単位に変換した本票CSVファイル（2022年）をコード表を元に読みやすいデータに変換するプログラムになります。

#### 使用データ
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_to-degree.csv`,73.8MB  
- コード表`https://github.com/shi-works/traffic-accident-data-2022-converter/tree/main/code`

hit.csv is based on https://github.com/code4fukui/traffic-accident Thanks!

#### 出力結果
##### csv形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_convert.csv`,227.4MB  
##### FlatGeobuf形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_convert.fgb`,358.9MB

### csvfile-merge.py
- 2019-2021年のデータと2022年のデータをマージするプログラムになります。
- 2019-2021年のデータの変換ツールは[こちらのリポジトリ](https://github.com/shi-works/npa-traffic-accident-data-converter)を参照してください。

#### 使用データ
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_convert_v2.csv`,722.4MB  
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2022_convert.csv`,227.4MB

#### 出力結果
##### csv形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2022_convert.csv`,978.7MB  
##### FlatGeobuf形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2022_convert.fgb`,1.5GB
##### GeoParquet形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2022_convert.parquet`,94.2MB

## デモサイト（MapLibre GL JS）
- 使用データ：[交通事故統計情報のオープンデータ（2019年、2020年、2021年、2022年）の本票（PMTiles形式）](https://github.com/shiwaku/npa-traffic-accident-pmtiles)
- https://shiwaku.github.io/npa-traffic-accident-map-on-maplibre/

## 使用データ及び出力結果のライセンスについて
本データセットは[CC-BY-4.0](https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/traffic-accident/LICENSE)で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは交通事故統計情報のオープンデータ（2019、2020、2021、2022年）の本票を加工して作成したものです。本データセットの使用・加工にあたっては、[警察庁Webサイトの利用規約](https://www.npa.go.jp/rules/index.html)を必ずご確認ください。

## 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
