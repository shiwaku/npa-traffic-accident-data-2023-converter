# -*- coding: utf-8 -*-
# CSVファイルのマージ
import glob
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent.parent


def csv_file_merge():
    all_files = glob.glob(str(ROOT / 'csv' / '*.csv'))
    print(all_files)

    if not all_files:
        print('対象ファイルが見つかりません')
        return

    dfs = []
    for file in all_files:
        dfs.append(pd.read_csv(file, index_col=0, encoding='utf-8', dtype=object))
        print(file)

    df = pd.concat(dfs, sort=False)
    df.to_csv(ROOT / 'honhyo_2019-2023_convert.csv')
    print('処理終了')


csv_file_merge()
