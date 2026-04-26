# CLAUDE.md

## プロジェクト概要

警察庁の交通事故統計情報オープンデータ（2023年本票）をGISデータ（読みやすい形式）に変換するPythonスクリプト群。

## スクリプト構成と実行順序

```
Step 1: scripts/csvfile-to-degree.py   → honhyo_2023_to-degree.csv
Step 2: scripts/csvfile-convert.py     → honhyo_2023_convert.csv
Step 3: scripts/csvfile-merge.py       → honhyo_2019-2023_convert.csv（任意）
```

## ディレクトリ構成

```
./
├── scripts/
│   ├── csvfile-to-degree.py   # Step 1: 緯度経度変換・UTF-8変換
│   ├── csvfile-convert.py     # Step 2: コード表による値の読み替え
│   └── csvfile-merge.py       # Step 3: 複数年データのマージ
├── code/                      # コード表CSV（変換辞書の元データ）
├── data/                      # 入力データ置き場（honhyo_2023.csv）※.gitignore
├── csv/                       # マージ対象CSV置き場（2019〜2023年）※.gitignore
├── requirements.txt
└── CLAUDE.md
```

## 依存パッケージ

```bash
pip install -r requirements.txt
```

## 各スクリプトの仕様

### csvfile-to-degree.py
- 入力: `./data/honhyo_2023.csv`（Shift-JIS、60進数緯度経度）
- 出力: `./honhyo_2023_to-degree.csv`（UTF-8、10進数緯度経度）
- 緯度が9桁・経度が10桁でない行はスキップする
- 出力は上書きモード（`w`）で毎回新規作成

### csvfile-convert.py
- 入力: `./honhyo_2023_to-degree.csv`、`code/` 配下のコード表CSV
- 出力: `./honhyo_2023_convert.csv`
- コード変換はモジュールレベルの辞書定数で定義（`SIRYOUKUBUN`、`TYUUYA` など）
- 範囲チェックが必要な路線コードのみ `rosenkoudo()` 関数で処理
- コード表CSV読み込みは `load_code_dict()` ヘルパーで共通化（5行ヘッダースキップ）
- 出力は上書きモード（`w`）で毎回新規作成

### csvfile-merge.py
- 入力: `./csv/` 配下の全CSV（2019〜2023年の変換済みデータ）
- 出力: `./honhyo_2019-2023_convert.csv`
- 対象ファイルが0件の場合は処理を中断してメッセージ出力

## コード表ファイルの注意事項

- 警察署等コード（`3_koudohyou_keisatusyotoukoudo_*.csv`）は年度ごとにファイルが異なる。`csvfile-convert.py` では2023年版を使用
- 路線コード（`9_koudohyou_rosen_kousokujidousya_jidousyasenyou_*.csv`）は2022年版を使用
- 車両の衝突部位（`hit.csv`）は [Code for FUKUI](https://github.com/code4fukui/traffic-accident) 作成のコード値表を使用。ヘッダーは1行のみ
