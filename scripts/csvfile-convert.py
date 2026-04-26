# -*- coding: utf-8 -*-
# コード表を元に読みやすいデータに変換する
import csv
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent.parent

# コード変換辞書
SIRYOUKUBUN = {1: '本票', 2: '補充票', 3: '高速票'}
JIKONAIYOU = {1: '死亡事故', 2: '負傷事故'}
TYUUYA = {11: '昼－明', 12: '昼－昼', 13: '昼－暮', 21: '夜－暮', 22: '夜－夜', 23: '夜－明'}
TENKOU = {1: '晴', 2: '曇', 3: '雨', 4: '霧', 5: '雪'}
TIKEI = {1: '市街地－人口集中', 2: '市街地－その他', 3: '非市街地'}
ROMENJYOUTAI = {1: '舗装－乾燥', 2: '舗装－湿潤', 3: '舗装－凍結', 4: '舗装－積雪', 5: '非舗装'}
DOUROKEIJYOU = {
    '31': '交差点－環状交差点', '01': '交差点－その他',
    '37': '交差点付近－環状交差点付近', '07': '交差点付近－その他',
    '11': '単路－トンネル', '12': '単路－橋', '13': '単路－カーブ・屈折', '14': '単路－その他',
    '21': '踏切－第一種', '22': '踏切－第三種', '23': '踏切－第四種',
    '00': '一般交通の場所',
}
SINGOUKI = {
    1: '点灯－３灯式', 8: '点灯－歩車分式', 2: '点灯－押ボタン式',
    3: '点滅－３灯式', 4: '点滅－１灯式', 5: '消灯', 6: '故障', 7: '施設なし',
}
ITIJITEISIKISEI_HYOUSIKI = {
    '01': '標準－反射式', '02': '標準－自発光式', '03': '標準－内部照明式',
    '04': '拡大－反射式', '05': '拡大－自発光式', '06': '拡大－内部照明式',
    '07': '縮小', '08': 'その他', '09': '規制なし', '00': '対象外当事者',
}
ITIJITEISIKISEI_HYOUJI = {'21': '表示あり', '22': '表示なし', '00': '対象外当事者'}
SYADOUHUKUIN = {
    '01': '単路－3.5m未満', '02': '単路－3.5m以上', '03': '単路－5.5m以上',
    '04': '単路－9.0m以上', '05': '単路－13.0m以上', '06': '単路－19.5m以上',
    '11': '交差点－小（5.5m未満）－小', '14': '交差点－中（5.5m以上）－小',
    '15': '交差点－中（5.5m以上）－中', '17': '交差点－大（13.0ｍ以上）－小',
    '18': '交差点－大（13.0ｍ以上）－中', '19': '交差点－大（13.0ｍ以上）－大',
    '00': '一般交通の場所',
}
DOUROSENKEI = {
    1: 'カーブ・屈折－右－上り', 2: 'カーブ・屈折－右－下り', 3: 'カーブ・屈折－右－平坦',
    4: 'カーブ・屈折－左－上り', 5: 'カーブ・屈折－左－下り', 6: 'カーブ・屈折－左－平坦',
    7: '直線－上り', 8: '直線－下り', 9: '直線－平坦', 0: '一般交通の場所',
}
SYOUTOTUTITEN = {'01': '単路（交差点付近を含む）', '30': '交差点内', '20': 'その他'}
ZOONKISEI = {'01': 'ゾーン30', '70': '規制なし'}
TYUUOUBUNRITAISISETUTOU = {
    1: '中央分離帯', 2: '中央線－高輝度標示', 3: '中央線－チャッターバー等',
    6: '中央線－ポストコーン', 7: '中央線－ワイヤロープ', 4: '中央線－ペイント',
    5: '中央分離なし', 0: '一般交通の場所',
}
HOSYADOUKUBUN = {1: '区分あり－防護柵等', 2: '区分あり－縁石・ブロック等', 3: '区分あり－路側帯', 4: '区分なし'}
JIKORUIKEI = {'01': '人対車両', '21': '車両相互', '41': '車両単独', '61': '列車'}
NENREI = {
    '01': '0～24歳', '25': '25～34歳', '35': '35～44歳', '45': '45～54歳',
    '55': '55～64歳', '65': '65～74歳', '75': '75歳以上', '00': '不明',
}
TOUJISYASYUBETU = {
    '01': '乗用車－大型車', '02': '乗用車－中型車', '07': '乗用車－準中型車',
    '03': '乗用車－普通車', '04': '乗用車－軽自動車', '05': '乗用車－ミニカー',
    '11': '貨物車－大型車', '12': '貨物車－中型車', '17': '貨物車－準中型車',
    '13': '貨物車－普通車', '14': '貨物車－軽自動車',
    '21': '特殊車－大型－農耕作業用', '22': '特殊車－大型－その他',
    '23': '特殊車－小型－農耕作業用', '24': '特殊車－小型－その他',
    '31': '二輪車－自動二輪－小型二輪－751ｃｃ以上', '32': '二輪車－自動二輪－小型二輪－401～750ｃｃ',
    '33': '二輪車－自動二輪－小型二輪－251～400cc', '34': '二輪車－自動二輪－軽二輪－126～250cc',
    '35': '二輪車－自動二輪－原付二種－51～125cc', '36': '二輪車－原付自転車',
    '41': '路面電車', '42': '列車',
    '51': '軽車両－自転車', '52': '軽車両－駆動補助機付自転車', '59': '軽車両－その他',
    '61': '歩行者', '71': '歩行者以外の道路上の人（補充票のみ）',
    '72': '道路外の人（補充票のみ）', '75': '物件等', '76': '相手なし', '00': '対象外当事者',
}
YOUTOBETU = {'01': '事業用', '31': '自家用', '41': '自転車', '00': '対象外当事者'}
SYARYOUKEIJYOU = {'01': '乗用車', '11': '貨物車', '31': '立ち乗り型電動車', '00': '対象外当事者'}
SOKUDOKISEI_SITEINOMI = {
    '01': '20㎞／ｈ以下', '02': '30㎞／ｈ以下', '03': '40㎞／ｈ以下', '04': '50㎞／ｈ以下',
    '05': '60㎞／ｈ以下', '06': '70㎞／ｈ以下', '07': '80㎞／ｈ以下', '08': '100㎞/h以下',
    '11': '120㎞/h以下', '12': '120㎞/h超過', '10': '指定の速度規制なし等', '00': '対象外当事者',
}
SYARYOUNOSONKAITEIDO = {'1': '大破', '2': '中破', '3': '小破', '4': '損壊なし', '0': '対象外当事者', '': '－'}
EABAGUNOSOUBI = {1: '装備あり 作動', 2: 'その他', 0: '対象外当事者'}
SAIDOEABAGUNOSOUBI = {1: '装備あり 作動', 2: 'その他', 0: '対象外当事者'}
JINSINSONSYOUTEIDO = {1: '死亡', 2: '負傷', 4: '損傷なし', 0: '対象外当事者'}
YOUBI = {1: '日', 2: '月', 3: '火', 4: '水', 5: '木', 6: '金', 7: '土'}
SYUKUJITU = {1: '当日', 2: '前日', 3: 'その他'}


def rosenkoudo(code):
    if 1 <= code <= 999:
        return '一般国道（国道番号）'
    elif 1000 <= code <= 1499:
        return '主要地方道－都道府県道'
    elif 1500 <= code <= 1999:
        return '主要地方道－市道'
    elif 2000 <= code <= 2999:
        return '一般都道府県道'
    elif 3000 <= code <= 3999:
        return '一般市町村道'
    elif 4000 <= code <= 4999:
        return '高速自動車国道 *1'
    elif 5000 <= code <= 5499:
        return '自動車専用道－指定 *1'
    elif 5500 <= code <= 5999:
        return '自動車専用道－その他'
    elif 6000 <= code <= 6999:
        return '道路運送法上の道路'
    elif 7000 <= code <= 7999:
        return '農（免）道'
    elif 8000 <= code <= 8499:
        return '林道'
    elif 8500 <= code <= 8999:
        return '港湾道'
    elif 9000 <= code <= 9499:
        return '私道'
    elif code == 9500:
        return 'その他'
    elif code == 9900:
        return '一般の交通の用に供するその他の道路'
    return None


def load_code_dict(filepath, key_cols, value_col, skip_rows=5, encoding='utf-8'):
    with open(filepath, mode='r', encoding=encoding) as f:
        reader = csv.reader(f)
        for _ in range(skip_rows):
            next(reader)
        return {''.join(row[c] for c in key_cols): row[value_col] for row in reader}


def convert():
    # コード表を辞書に読み込み
    dict_todouhuken = load_code_dict(ROOT / 'code' / '2_koudohyou_todouhukenkoudo.csv', [0], 1)
    dict_keisatusyo = load_code_dict(
        ROOT / 'code' / '3_koudohyou_keisatusyotoukoudo_2023.csv', [0, 1], 3)
    dict_rosenkousoku = load_code_dict(
        ROOT / 'code' / '9_koudohyou_rosen_kousokujidousya_jidousyasenyou_2022.csv', [0, 1], 3)

    with open(ROOT / 'code' / 'hit.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        dict_syaryounosyoutotubui = {row[0]: row[1] for row in reader}

    # 本票データ読み込み
    data = pd.read_csv(ROOT / 'honhyo_2023_to-degree.csv', dtype=object).values.tolist()
    print(f'{len(data)}件')

    fieldnames = [
        '資料区分', '都道府県名', '警察署等名', '本票番号', '事故内容', '死者数', '負傷者数',
        '路線名', '上下線', '地点コード', '市区町村コード',
        '発生日時_年', '発生日時_月', '発生日時_日', '発生日時_時', '発生日時_分',
        '昼夜', '天候', '地形', '路面状態', '道路形状', '環状交差点の直径', '信号機',
        '一時停止規制_標識（当事者A）', '一時停止規制_表示（当事者A）',
        '一時停止規制_標識（当事者B）', '一時停止規制_表示（当事者B）',
        '車道幅員', '道路線形', '衝突地点', 'ゾーン規制', '中央分離帯施設等', '歩車道区分', '事故類型',
        '年齢（当事者A）', '年齢（当事者B）', '当事者種別（当事者A）', '当事者種別（当事者B）',
        '用途別（当事者A）', '用途別（当事者B）', '車両形状（当事者A）', '車両形状（当事者B）',
        '速度規制（指定のみ）（当事者A）', '速度規制（指定のみ）（当事者B）',
        '車両の衝突部位（当事者A）', '車両の衝突部位（当事者B）',
        '車両の損壊程度（当事者A）', '車両の損壊程度（当事者B）',
        'エアバッグの装備（当事者A）', 'エアバッグの装備（当事者B）',
        'サイドエアバッグの装備（当事者A）', 'サイドエアバッグの装備（当事者B）',
        '人身損傷程度（当事者A）', '人身損傷程度（当事者B）',
        '地点_緯度（北緯）', '地点_経度（東経）', '曜日(発生年月日)', '祝日(発生年月日)',
        '地点_緯度（北緯）_10進数', '地点_経度（東経）_10進数',
        '日の出時刻　　時', '日の出時刻　　分', '日の入り時刻　　時', '日の入り時刻　　分',
        'オートマチック車（当事者A）', 'オートマチック車（当事者B）',
        'サポカー（当事者A）', 'サポカー（当事者B）',
        '認知機能検査経過日数（当事者A）', '認知機能検査経過日数（当事者B）',
        '運転練習の方法（当事者A）', '運転練習の方法（当事者B）',
    ]

    with open(ROOT / 'honhyo_2023_convert.csv', 'w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()

        for row in data:
            # 路線名
            str_rosenkoudo = str(row[7])
            int_rosenkoudo = int(str_rosenkoudo[0:4])
            res_rosenkoudo = rosenkoudo(int_rosenkoudo)
            if res_rosenkoudo in ('高速自動車国道 *1', '自動車専用道－指定 *1'):
                res_rosenkoudo = dict_rosenkousoku.get(
                    str(row[1]) + str_rosenkoudo[0:4], res_rosenkoudo)
            elif res_rosenkoudo == '一般国道（国道番号）':
                res_rosenkoudo = '一般国道' + str(int(str_rosenkoudo[0:4])) + '号'

            writer.writerow({
                '資料区分': SIRYOUKUBUN.get(int(row[0])),
                '都道府県名': dict_todouhuken.get(row[1]),
                '警察署等名': dict_keisatusyo.get(str(row[1]) + str(row[2])),
                '本票番号': row[3],
                '事故内容': JIKONAIYOU.get(int(row[4])),
                '死者数': row[5],
                '負傷者数': row[6],
                '路線名': res_rosenkoudo,
                '上下線': '',
                '地点コード': row[9],
                '市区町村コード': row[10],
                '発生日時_年': row[11],
                '発生日時_月': row[12],
                '発生日時_日': row[13],
                '発生日時_時': row[14],
                '発生日時_分': row[15],
                '昼夜': TYUUYA.get(int(row[16])),
                '天候': TENKOU.get(int(row[17])),
                '地形': TIKEI.get(int(row[18])),
                '路面状態': ROMENJYOUTAI.get(int(row[19])),
                '道路形状': DOUROKEIJYOU.get(str(row[20])),
                '環状交差点の直径': '',
                '信号機': SINGOUKI.get(int(row[22])),
                '一時停止規制_標識（当事者A）': ITIJITEISIKISEI_HYOUSIKI.get(str(row[23])),
                '一時停止規制_表示（当事者A）': ITIJITEISIKISEI_HYOUJI.get(str(row[24])),
                '一時停止規制_標識（当事者B）': ITIJITEISIKISEI_HYOUSIKI.get(str(row[25])),
                '一時停止規制_表示（当事者B）': ITIJITEISIKISEI_HYOUJI.get(str(row[26])),
                '車道幅員': SYADOUHUKUIN.get(str(row[27])),
                '道路線形': DOUROSENKEI.get(int(row[28])),
                '衝突地点': SYOUTOTUTITEN.get(str(row[29])),
                'ゾーン規制': ZOONKISEI.get(str(row[30])),
                '中央分離帯施設等': TYUUOUBUNRITAISISETUTOU.get(int(row[31])),
                '歩車道区分': HOSYADOUKUBUN.get(int(row[32])),
                '事故類型': JIKORUIKEI.get(str(row[33])),
                '年齢（当事者A）': NENREI.get(str(row[34])),
                '年齢（当事者B）': NENREI.get(str(row[35])),
                '当事者種別（当事者A）': TOUJISYASYUBETU.get(str(row[36])),
                '当事者種別（当事者B）': TOUJISYASYUBETU.get(str(row[37])),
                '用途別（当事者A）': YOUTOBETU.get(str(row[38])),
                '用途別（当事者B）': YOUTOBETU.get(str(row[39])),
                '車両形状（当事者A）': SYARYOUKEIJYOU.get(str(row[40])),
                '車両形状（当事者B）': SYARYOUKEIJYOU.get(str(row[41])),
                '速度規制（指定のみ）（当事者A）': SOKUDOKISEI_SITEINOMI.get(str(row[42])),
                '速度規制（指定のみ）（当事者B）': SOKUDOKISEI_SITEINOMI.get(str(row[43])),
                '車両の衝突部位（当事者A）': dict_syaryounosyoutotubui.get(str(row[44])),
                '車両の衝突部位（当事者B）': dict_syaryounosyoutotubui.get(str(row[45])),
                '車両の損壊程度（当事者A）': SYARYOUNOSONKAITEIDO.get(str(row[46])),
                '車両の損壊程度（当事者B）': SYARYOUNOSONKAITEIDO.get(str(row[47])),
                'エアバッグの装備（当事者A）': EABAGUNOSOUBI.get(int(row[48])),
                'エアバッグの装備（当事者B）': EABAGUNOSOUBI.get(int(row[49])),
                'サイドエアバッグの装備（当事者A）': SAIDOEABAGUNOSOUBI.get(int(row[50])),
                'サイドエアバッグの装備（当事者B）': SAIDOEABAGUNOSOUBI.get(int(row[51])),
                '人身損傷程度（当事者A）': JINSINSONSYOUTEIDO.get(int(row[52])),
                '人身損傷程度（当事者B）': JINSINSONSYOUTEIDO.get(int(row[53])),
                '地点_緯度（北緯）': row[54],
                '地点_経度（東経）': row[55],
                '曜日(発生年月日)': YOUBI.get(int(row[56])),
                '祝日(発生年月日)': SYUKUJITU.get(int(row[57])),
                '地点_緯度（北緯）_10進数': row[58],
                '地点_経度（東経）_10進数': row[59],
                '日の出時刻　　時': row[60],
                '日の出時刻　　分': row[61],
                '日の入り時刻　　時': row[62],
                '日の入り時刻　　分': row[63],
                'オートマチック車（当事者A）': row[64],
                'オートマチック車（当事者B）': row[65],
                'サポカー（当事者A）': row[66],
                'サポカー（当事者B）': row[67],
                '認知機能検査経過日数（当事者A）': row[68],
                '認知機能検査経過日数（当事者B）': row[69],
                '運転練習の方法（当事者A）': row[70],
                '運転練習の方法（当事者B）': row[71],
            })

    print('処理終了')


convert()
