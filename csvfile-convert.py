# -*- coding: utf-8 -*-
# コード表を元に読みやすいデータに変換する
import pandas as pd
import csv

# 出力CSVファイルオープン
output_csvfile = "./honhyo_2023_convert.csv"
with open(output_csvfile, 'a', encoding='UTF-8') as f:
    # ヘッダー行出力
    fieldnames = ['資料区分', '都道府県名', '警察署等名', '本票番号', '事故内容', '死者数', '負傷者数', '路線名', '上下線', '地点コード', '市区町村コード', '発生日時_年', '発生日時_月', '発生日時_日',
                  '発生日時_時', '発生日時_分', '昼夜', '天候', '地形', '路面状態', '道路形状', '環状交差点の直径', '信号機', '一時停止規制_標識（当事者A）', '一時停止規制_表示（当事者A）', '一時停止規制_標識（当事者B）', '一時停止規制_表示（当事者B）',
                  '車道幅員', '道路線形', '衝突地点', 'ゾーン規制', '中央分離帯施設等', '歩車道区分', '事故類型', '年齢（当事者A）', '年齢（当事者B）', '当事者種別（当事者A）', '当事者種別（当事者B）', '用途別（当事者A）', '用途別（当事者B）',
                  '車両形状（当事者A）', '車両形状（当事者B）', '速度規制（指定のみ）（当事者A）', '速度規制（指定のみ）（当事者B）', '車両の衝突部位（当事者A）', '車両の衝突部位（当事者B）', '車両の損壊程度（当事者A）', '車両の損壊程度（当事者B）',
                  'エアバッグの装備（当事者A）', 'エアバッグの装備（当事者B）', 'サイドエアバッグの装備（当事者A）', 'サイドエアバッグの装備（当事者B）', '人身損傷程度（当事者A）', '人身損傷程度（当事者B）', '地点_緯度（北緯）', '地点_経度（東経）', '曜日(発生年月日)', '祝日(発生年月日)',
                  '地点_緯度（北緯）_10進数', '地点_経度（東経）_10進数', '日の出時刻　　時', '日の出時刻　　分', '日の入り時刻　　時', '日の入り時刻　　分', 'オートマチック車（当事者A）', 'オートマチック車（当事者B）', 'サポカー（当事者A）', 'サポカー（当事者B）',
                  '認知機能検査経過日数（当事者A）', '認知機能検査経過日数（当事者B）', '運転練習の方法（当事者A）', '運転練習の方法（当事者B）']

    csvfile_writer = csv.DictWriter(
        f, fieldnames=fieldnames, lineterminator='\n')
    csvfile_writer.writeheader()

    # CSVファイルをデータフレームに格納
    # 本票
    data = pd.read_csv(
        "./honhyo_2023_to-degree.csv", dtype=object).values.tolist()

    # 02_都道府県コードを辞書に読み込み
    csv_file_todouhuken = "code/2_koudohyou_todouhukenkoudo.csv"
    with open(csv_file_todouhuken, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # 5行のヘッダーをスキップ
        for _ in range(5):
            next(reader)

        # 辞書にデータを追加
        dict_todouhuken = {row[0]: row[1] for row in reader}

    print('--- 2_koudohyou_todouhukenkoudo.csv ---')
    print(dict_todouhuken)

    # 03_警察署等コードを辞書に読み込み
    # csv_file_keisatusyo = "code/3_koudohyou_keisatusyotoukoudo.csv"
    # csv_file_keisatusyo = "code/3_koudohyou_keisatusyotoukoudo_2022.csv"
    csv_file_keisatusyo = "code/3_koudohyou_keisatusyotoukoudo_2023.csv"
    with open(csv_file_keisatusyo, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # 5行のヘッダーをスキップ
        for _ in range(5):
            next(reader)

        # 辞書にデータを追加
        dict_keisatusyo = {
            row[0] + row[1]: row[3] for row in reader}

    print('--- 3_koudohyou_keisatusyotoukoudo.csv ---')
    print(dict_keisatusyo)

    # 09_路線（高速自動車国道,自動車専用道（指定））コードを辞書に読み込み
    # csv_file_rosenkousoku = "code/9_koudohyou_rosen_kousokujidousya_jidousyasenyou.csv"
    csv_file_rosenkousoku = "code/9_koudohyou_rosen_kousokujidousya_jidousyasenyou_2022.csv"
    with open(csv_file_rosenkousoku, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # 5行のヘッダーをスキップ
        for _ in range(5):
            next(reader)

        # 辞書にデータを追加
        dict_rosenkousoku = {
            row[0] + row[1]: row[3] for row in reader}

    print('--- 9_koudohyou_rosen_kousokujidousya_jidousyasenyou.csv ---')
    print(dict_rosenkousoku)

    # 35_車両の衝突部位コードを辞書に読み込み
    # 当該データはCode for FUKUIが作成したコード値表（https://github.com/code4fukui/traffic-accident）を使用
    csv_file_syaryounosyoutotubui = "code/hit.csv"
    with open(csv_file_syaryounosyoutotubui, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # 1行のヘッダーをスキップ
        next(reader)

        # 辞書にデータを追加
        dict_syaryounosyoutotubui = {row[0]: row[1] for row in reader}

    print('--- hit.csv ---')
    print(dict_syaryounosyoutotubui)

    # print(HsyaryounosyoutotubuiTbl.get('88'))
    # print('-')

    # コード値を読み替える関数
    # 01_資料区分
    def siryoukubun(code):
        if code == 1:
            return '本票'
        elif code == 2:
            return '補充票'
        elif code == 3:
            return '高速票'

    # 05_事故内容
    def jikonaiyou(code):
        if code == 1:
            return '死亡事故'
        elif code == 2:
            return '負傷事故'

    # 08_路線コード
    def rosenkoudo(code):
        if code >= 1 and code <= 999:
            return '一般国道（国道番号）'
        elif code >= 1000 and code <= 1499:
            return '主要地方道－都道府県道'
        elif code >= 1500 and code <= 1999:
            return '主要地方道－市道'
        elif code >= 2000 and code <= 2999:
            return '一般都道府県道'
        elif code >= 3000 and code <= 3999:
            return '一般市町村道'
        elif code >= 4000 and code <= 4999:
            return '高速自動車国道 *1'
        elif code >= 5000 and code <= 5499:
            return '自動車専用道－指定 *1'
        elif code >= 5500 and code <= 5999:
            return '自動車専用道－その他'
        elif code >= 6000 and code <= 6999:
            return '道路運送法上の道路'
        elif code >= 7000 and code <= 7999:
            return '農（免）道'
        elif code >= 8000 and code <= 8499:
            return '林道'
        elif code >= 8500 and code <= 8999:
            return '港湾道'
        elif code >= 9000 and code <= 9499:
            return '私道'
        elif code == 9500:
            return 'その他'
        elif code == 9900:
            return '一般の交通の用に供するその他の道路'

    # 2022年では項目なし
    '''
    # 10_上下線
    def jyougesen(code):
        if code == 1:
            return '上'
        elif code == 2:
            return '下'
        elif code == 0:
            return '対象外'
    '''

    # 14_昼夜
    def tyuuya(code):
        if code == 11:
            return '昼－明'
        elif code == 12:
            return '昼－昼'
        elif code == 13:
            return '昼－暮'
        elif code == 21:
            return '夜－暮'
        elif code == 22:
            return '夜－夜'
        elif code == 23:
            return '夜－明'

    # 天候
    def tenkou(code):
        if code == 1:
            return '晴'
        elif code == 2:
            return '曇'
        elif code == 3:
            return '雨'
        elif code == 4:
            return '霧'
        elif code == 5:
            return '雪'

    # 地形
    def tikei(code):
        if code == 1:
            return '市街地－人口集中'
        elif code == 2:
            return '市街地－その他'
        elif code == 3:
            return '非市街地'

    # 路面状態
    def romenjyoutai(code):
        if code == 1:
            return '舗装－乾燥'
        elif code == 2:
            return '舗装－湿潤'
        elif code == 3:
            return '舗装－凍結'
        elif code == 4:
            return '舗装－積雪'
        elif code == 5:
            return '非舗装'

    # 道路形状
    def dourokeijyou(code):
        if code == '31':
            return '交差点－環状交差点'
        elif code == '01':
            return '交差点－その他'
        elif code == '37':
            return '交差点付近－環状交差点付近'
        elif code == '07':
            return '交差点付近－その他'
        elif code == '11':
            return '単路－トンネル'
        elif code == '12':
            return '単路－橋'
        elif code == '13':
            return '単路－カーブ・屈折'
        elif code == '14':
            return '単路－その他'
        elif code == '21':
            return '踏切－第一種'
        elif code == '22':
            return '踏切－第三種'
        elif code == '23':
            return '踏切－第四種'
        elif code == '00':
            return '一般交通の場所'

    # 2022年では項目なし
    # 環状交差点の直径
    '''
    def kanjyoukousatennotyokkei(code):
        if code == '01':
            return '小（27ｍ未満）'
        elif code == '02':
            return '中（27ｍ以上）'
        elif code == '03':
            return '大（43ｍ以上）'
        elif code == '00':
            return '環状交差点以外'
    '''

    # 信号機
    def singouki(code):
        if code == 1:
            return '点灯－３灯式'
        elif code == 8:
            return '点灯－歩車分式'
        elif code == 2:
            return '点灯－押ボタン式'
        elif code == 3:
            return '点滅－３灯式'
        elif code == 4:
            return '点滅－１灯式'
        elif code == 5:
            return '消灯'
        elif code == 6:
            return '故障'
        elif code == 7:
            return '施設なし'

    # 一時停止規制　標識
    def itijiteisikisei_hyousiki(code):
        if code == '01':
            return '標準－反射式'
        elif code == '02':
            return '標準－自発光式'
        elif code == '03':
            return '標準－内部照明式'
        elif code == '04':
            return '拡大－反射式'
        elif code == '05':
            return '拡大－自発光式'
        elif code == '06':
            return '拡大－内部照明式'
        elif code == '07':
            return '縮小'
        elif code == '08':
            return 'その他'
        elif code == '09':
            return '規制なし'
        elif code == '00':
            return '対象外当事者'

    # 一時停止規制　表示
    def itijiteisikisei_hyouji(code):
        if code == '21':
            return '表示あり'
        elif code == '22':
            return '表示なし'
        elif code == '00':
            # return 'その他'
            return '対象外当事者'

    # 車道幅員
    def syadouhukuin(code):
        if code == '01':
            return '単路－3.5m未満'
        elif code == '02':
            return '単路－3.5m以上'
        elif code == '03':
            return '単路－5.5m以上'
        elif code == '04':
            return '単路－9.0m以上'
        elif code == '05':
            return '単路－13.0m以上'
        elif code == '06':
            return '単路－19.5m以上'
        elif code == '11':
            return '交差点－小（5.5m未満）－小'
        elif code == '14':
            return '交差点－中（5.5m以上）－小'
        elif code == '15':
            return '交差点－中（5.5m以上）－中'
        elif code == '17':
            return '交差点－大（13.0ｍ以上）－小'
        elif code == '18':
            return '交差点－大（13.0ｍ以上）－中'
        elif code == '19':
            return '交差点－大（13.0ｍ以上）－大'
        elif code == '00':
            return '一般交通の場所'

    # 道路線形
    def dourosenkei(code):
        if code == 1:
            return 'カーブ・屈折－右－上り'
        elif code == 2:
            return 'カーブ・屈折－右－下り'
        elif code == 3:
            return 'カーブ・屈折－右－平坦'
        elif code == 4:
            return 'カーブ・屈折－左－上り'
        elif code == 5:
            return 'カーブ・屈折－左－下り'
        elif code == 6:
            return 'カーブ・屈折－左－平坦'
        elif code == 7:
            return '直線－上り'
        elif code == 8:
            return '直線－下り'
        elif code == 9:
            return '直線－平坦'
        elif code == 0:
            return '一般交通の場所'

    # 衝突地点
    def syoutotutiten(code):
        if code == '01':
            return '単路（交差点付近を含む）'
        elif code == '30':
            return '交差点内'
        elif code == '20':
            return 'その他'

    # ゾーン規制
    def zoonkisei(code):
        if code == '01':
            return 'ゾーン30'
        elif code == '70':
            return '規制なし'

    # 中央分離帯施設等
    def tyuuoubunritaisisetutou(code):
        if code == 1:
            return '中央分離帯'
        elif code == 2:
            return '中央線－高輝度標示'
        elif code == 3:
            return '中央線－チャッターバー等'
        elif code == 6:
            return '中央線－ポストコーン'
        elif code == 7:
            # 2022年追加
            return '中央線－ワイヤロープ'
        elif code == 4:
            return '中央線－ペイント'
        elif code == 5:
            return '中央分離なし'
        elif code == 0:
            return '一般交通の場所'

    # 歩車道区分
    def hosyadoukubun(code):
        if code == 1:
            return '区分あり－防護柵等'
        elif code == 2:
            return '区分あり－縁石・ブロック等'
        elif code == 3:
            return '区分あり－路側帯'
        elif code == 4:
            return '区分なし'

    # 事故類型
    def jikoruikei(code):
        if code == '01':
            return '人対車両'
        elif code == '21':
            return '車両相互'
        elif code == '41':
            return '車両単独'
        elif code == '61':
            return '列車'

    # 年齢
    def nenrei(code):
        if code == '01':
            return '0～24歳'
        elif code == '25':
            return '25～34歳'
        elif code == '35':
            return '35～44歳'
        elif code == '45':
            return '45～54歳'
        elif code == '55':
            return '55～64歳'
        elif code == '65':
            return '65～74歳'
        elif code == '75':
            return '75歳以上'
        elif code == '00':
            return '不明'

    # 当事者種別
    def toujisyasyubetu(code):
        if code == '01':
            return '乗用車－大型車'
        elif code == '02':
            return '乗用車－中型車'
        elif code == '07':
            return '乗用車－準中型車'
        elif code == '03':
            return '乗用車－普通車'
        elif code == '04':
            return '乗用車－軽自動車'
        elif code == '05':
            return '乗用車－ミニカー'
        elif code == '11':
            return '貨物車－大型車'
        elif code == '12':
            return '貨物車－中型車'
        elif code == '17':
            return '貨物車－準中型車'
        elif code == '13':
            return '貨物車－普通車'
        elif code == '14':
            return '貨物車－軽自動車'
        elif code == '21':
            return '特殊車－大型－農耕作業用'
        elif code == '22':
            return '特殊車－大型－その他'
        elif code == '23':
            return '特殊車－小型－農耕作業用'
        elif code == '24':
            return '特殊車－小型－その他'
        elif code == '31':
            return '二輪車－自動二輪－小型二輪－751ｃｃ以上'
        elif code == '32':
            return '二輪車－自動二輪－小型二輪－401～750ｃｃ'
        elif code == '33':
            return '二輪車－自動二輪－小型二輪－251～400cc'
        elif code == '34':
            return '二輪車－自動二輪－軽二輪－126～250cc'
        elif code == '35':
            return '二輪車－自動二輪－原付二種－51～125cc'
        elif code == '36':
            return '二輪車－原付自転車'
        elif code == '41':
            return '路面電車'
        elif code == '42':
            return '列車'
        elif code == '51':
            return '軽車両－自転車'
        elif code == '52':
            return '軽車両－駆動補助機付自転車'
        elif code == '59':
            return '軽車両－その他'
        elif code == '61':
            return '歩行者'
        elif code == '71':
            return '歩行者以外の道路上の人（補充票のみ）'
        elif code == '72':
            return '道路外の人（補充票のみ）'
        elif code == '75':
            return '物件等'
        elif code == '76':
            return '相手なし'
        elif code == '00':
            return '対象外当事者'

    # 用途別
    def youtobetu(code):
        if code == '01':
            return '事業用'
        elif code == '31':
            return '自家用'
        elif code == '41':
            return '自転車'
        elif code == '00':
            return '対象外当事者'

    # 車両形状
    def syaryoukeijyou(code):
        if code == '01':
            return '乗用車'
        elif code == '11':
            return '貨物車'
        elif code == '31':
            return '立ち乗り型電動車'
        elif code == '00':
            return '対象外当事者'

    # 速度規制（指定のみ）
    def sokudokisei_siteinomi(code):
        if code == '01':
            return '20㎞／ｈ以下'
        elif code == '02':
            return '30㎞／ｈ以下'
        elif code == '03':
            return '40㎞／ｈ以下'
        elif code == '04':
            return '50㎞／ｈ以下'
        elif code == '05':
            return '60㎞／ｈ以下'
        elif code == '06':
            return '70㎞／ｈ以下'
        elif code == '07':
            return '80㎞／ｈ以下'
        elif code == '08':
            return '100㎞/h以下'
        elif code == '11':
            return '120㎞/h以下'
        elif code == '12':
            return '120㎞/h超過'
        elif code == '10':
            return '指定の速度規制なし等'
        elif code == '00':
            return '対象外当事者'

    # 車両の損壊程度
    def syaryounosonkaiteido(code):
        if code == '1':
            return '大破'
        elif code == '2':
            return '中破'
        elif code == '3':
            return '小破'
        elif code == '4':
            return '損壊なし'
        elif code == '0':
            return '対象外当事者'
        elif code == '':
            return '－'

    # エアバッグの装備
    def eabagunosoubi(code):
        if code == 1:
            return '装備あり 作動'
        elif code == 2:
            return 'その他'
        elif code == 0:
            return '対象外当事者'

    # サイドエアバッグの装備
    def saidoeabagunosoubi(code):
        if code == 1:
            return '装備あり 作動'
        elif code == 2:
            return 'その他'
        elif code == 0:
            return '対象外当事者'

    # 人身損傷程度
    def jinsinsonsyouteido(code):
        if code == 1:
            return '死亡'
        elif code == 2:
            return '負傷'
        elif code == 4:
            return '損傷なし'
        elif code == 0:
            return '対象外当事者'

    # 曜日
    def youbi(code):
        if code == 1:
            return '日'
        elif code == 2:
            return '月'
        elif code == 3:
            return '火'
        elif code == 4:
            return '水'
        elif code == 5:
            return '木'
        elif code == 6:
            return '金'
        elif code == 7:
            return '土'

    # 祝日
    def syukujitu(code):
        if code == 1:
            return '当日'
        elif code == 2:
            return '前日'
        elif code == 3:
            return 'その他'

    print(len(data))
    for i in range(len(data)):

        # コード値の読み替え後の値を格納

        # 資料区分
        res_siryoukubun = siryoukubun(int(data[i][0]))

        # 都道府県名
        # res_todouhuken = HtodouhukenTbl.get(data[i][1])
        if data[i][1] in dict_todouhuken:
            res_todouhuken = dict_todouhuken[data[i][1]]

        # 事故内容
        res_jikonaiyou = jikonaiyou(int(data[i][4]))

        # 路線名
        str_rosenkoudo = str(data[i][7])
        int_rosenkoudo = int(str_rosenkoudo[0:4])  # 上4桁
        res_rosenkoudo = rosenkoudo(int_rosenkoudo)
        if res_rosenkoudo == '高速自動車国道 *1' or res_rosenkoudo == '自動車専用道－指定 *1':
            # 高速道路の場合、dict_rosenkousokuから路線名を取得
            # res_rosenkoudo = HrosenkousokuTbl.get(str(data[i][1]) + str(str_rosenkoudo[0:4]))  # 上4桁
            if str(data[i][1]) + str(str_rosenkoudo[0:4]) in dict_rosenkousoku:
                res_rosenkoudo = dict_rosenkousoku[str(
                    data[i][1]) + str(str_rosenkoudo[0:4])]
        elif res_rosenkoudo == '一般国道（国道番号）':
            # 一般国道の場合、路線コードから路線番号を付与
            res_rosenkoudo = '一般国道' + str(int(str_rosenkoudo[0:4])) + "号"

        # 警察署等名
        # res_keisatusyo = HkeisatusyoTbl.get(str(data[i][1]) + str(data[i][2]))
        if str(data[i][1]) + str(data[i][2]) in dict_keisatusyo:
            res_keisatusyo = dict_keisatusyo[str(data[i][1]) + str(data[i][2])]

        # 2022年では項目なし
        # 上下線
        # res_jyougesen = jyougesen(int(data[i][8]))

        # 昼夜
        res_tyuuya = tyuuya(int(data[i][16]))

        # 天候
        res_tenkou = tenkou(int(data[i][17]))

        # 地形
        res_tikei = tikei(int(data[i][18]))

        # 路面状態
        res_romenjyoutai = romenjyoutai(int(data[i][19]))

        # 道路形状
        res_dourokeijyou = dourokeijyou(str(data[i][20]))

        # 2022年では項目なし
        # 環状交差点の直径
        '''
        res_kanjyoukousatennotyokkei = kanjyoukousatennotyokkei(
            str(data[i][21]))
        '''

        # 信号機
        res_singouki = singouki(int(data[i][22]))

        # 一時停止規制_標識（当事者A）
        res_itijiteisikisei_hyousiki_a = itijiteisikisei_hyousiki(
            str(data[i][23]))

        # 一時停止規制_表示（当事者A）
        # res_itijiteisikisei_hyouji_a = itijiteisikisei_hyouji(int(data[i][24]))
        res_itijiteisikisei_hyouji_a = itijiteisikisei_hyouji(str(data[i][24]))

        # 一時停止規制_標識（当事者B）
        res_itijiteisikisei_hyousiki_b = itijiteisikisei_hyousiki(
            str(data[i][25]))

        # 一時停止規制_表示（当事者B）
        # res_itijiteisikisei_hyouji_b = itijiteisikisei_hyouji(int(data[i][26]))
        res_itijiteisikisei_hyouji_b = itijiteisikisei_hyouji(str(data[i][24]))

        # 車道幅員
        res_syadouhukuin = syadouhukuin(str(data[i][27]))

        # 道路線形
        res_dourosenkei = dourosenkei(int(data[i][28]))

        # 衝突地点
        res_syoutotutiten = syoutotutiten(str(data[i][29]))

        # ゾーン規制
        res_zoonkisei = zoonkisei(str(data[i][30]))

        # 中央分離帯施設等
        res_tyuuoubunritaisisetutou = tyuuoubunritaisisetutou(int(data[i][31]))

        # 歩車道区分
        res_hosyadoukubun = hosyadoukubun(int(data[i][32]))

        # 事故類型
        res_jikoruikei = jikoruikei(str(data[i][33]))

        # 年齢（当事者A）
        res_nenrei_a = nenrei(str(data[i][34]))

        # 年齢（当事者B）
        res_nenrei_b = nenrei(str(data[i][35]))

        # 当事者種別（当事者A）
        res_toujisyasyubetu_a = toujisyasyubetu(str(data[i][36]))

        # 当事者種別（当事者B）
        res_toujisyasyubetu_b = toujisyasyubetu(str(data[i][37]))

        # 用途別（当事者A）
        res_youtobetu_a = youtobetu(str(data[i][38]))

        # 用途別（当事者B）
        res_youtobetu_b = youtobetu(str(data[i][39]))

        # 車両形状（当事者A）
        res_syaryoukeijyou_a = syaryoukeijyou(str(data[i][40]))

        # 車両形状（当事者B）
        res_syaryoukeijyou_b = syaryoukeijyou(str(data[i][41]))

        # 速度規制（指定のみ）（当事者A）
        res_sokudokisei_siteinomi_a = sokudokisei_siteinomi(str(data[i][42]))

        # 速度規制（指定のみ）（当事者B）
        res_sokudokisei_siteinomi_b = sokudokisei_siteinomi(str(data[i][43]))

        # 車両の衝突部位（当事者A）
        # res_syaryounosyoutotubui_a = HsyaryounosyoutotubuiTbl.get(str(data[i][44]))
        if str(data[i][44]) in dict_syaryounosyoutotubui:
            res_syaryounosyoutotubui_a = dict_syaryounosyoutotubui[str(
                data[i][44])]

        # 車両の衝突部位（当事者B）
        # res_syaryounosyoutotubui_b = HsyaryounosyoutotubuiTbl.get(str(data[i][45]))
        if str(data[i][45]) in dict_syaryounosyoutotubui:
            res_syaryounosyoutotubui_b = dict_syaryounosyoutotubui[str(
                data[i][45])]

        # 車両の損壊程度（当事者A）
        res_syaryounosonkaiteido_a = syaryounosonkaiteido(str(data[i][46]))

        # 車両の損壊程度（当事者B）
        res_syaryounosonkaiteido_b = syaryounosonkaiteido(str(data[i][47]))

        # エアバッグの装備（当事者A）
        res_eabagunosoubi_a = eabagunosoubi(int(data[i][48]))

        # エアバッグの装備（当事者B）
        res_eabagunosoubi_b = eabagunosoubi(int(data[i][49]))

        # サイドエアバッグの装備（当事者A）
        res_saidoeabagunosoubi_a = saidoeabagunosoubi(int(data[i][50]))

        # サイドエアバッグの装備（当事者B）
        res_saidoeabagunosoubi_b = saidoeabagunosoubi(int(data[i][51]))

        # 人身損傷程度（当事者A）
        res_jinsinsonsyouteido_a = jinsinsonsyouteido(int(data[i][52]))

        # 人身損傷程度（当事者B）
        res_jinsinsonsyouteido_b = jinsinsonsyouteido(int(data[i][53]))

        # 曜日(発生年月日)
        res_youbi = youbi(int(data[i][56]))

        # 祝日(発生年月日)
        res_syukujitu = syukujitu(int(data[i][57]))

        # 出力CSVファイルに書き込む
        csvfile_writer.writerow({
            '資料区分': res_siryoukubun, '都道府県名': res_todouhuken, '警察署等名': res_keisatusyo, '本票番号': data[i][3], '事故内容': res_jikonaiyou, '死者数': data[i][5],
            '負傷者数': data[i][6], '路線名': res_rosenkoudo, '上下線': '', '地点コード': data[i][9], '市区町村コード': data[i][10],
            '発生日時_年': data[i][11], '発生日時_月': data[i][12], '発生日時_日': data[i][13], '発生日時_時': data[i][14], '発生日時_分': data[i][15],
            '昼夜': res_tyuuya, '天候': res_tenkou, '地形': res_tikei, '路面状態': res_romenjyoutai, '道路形状': res_dourokeijyou,
            '環状交差点の直径': '', '信号機': res_singouki, '一時停止規制_標識（当事者A）': res_itijiteisikisei_hyousiki_a, '一時停止規制_表示（当事者A）': res_itijiteisikisei_hyouji_a, '一時停止規制_標識（当事者B）': res_itijiteisikisei_hyousiki_b,
            '一時停止規制_表示（当事者B）': res_itijiteisikisei_hyouji_b, '車道幅員': res_syadouhukuin, '道路線形': res_dourosenkei, '衝突地点': res_syoutotutiten, 'ゾーン規制': res_zoonkisei,
            '中央分離帯施設等': res_tyuuoubunritaisisetutou, '歩車道区分': res_hosyadoukubun, '事故類型': res_jikoruikei, '年齢（当事者A）': res_nenrei_a, '年齢（当事者B）': res_nenrei_b,
            '当事者種別（当事者A）': res_toujisyasyubetu_a, '当事者種別（当事者B）': res_toujisyasyubetu_b, '用途別（当事者A）': res_youtobetu_a, '用途別（当事者B）': res_youtobetu_b, '車両形状（当事者A）': res_syaryoukeijyou_a,
            '車両形状（当事者B）': res_syaryoukeijyou_b, '速度規制（指定のみ）（当事者A）': res_sokudokisei_siteinomi_a, '速度規制（指定のみ）（当事者B）': res_sokudokisei_siteinomi_b, '車両の衝突部位（当事者A）': res_syaryounosyoutotubui_a, '車両の衝突部位（当事者B）': res_syaryounosyoutotubui_b,
            '車両の損壊程度（当事者A）': res_syaryounosonkaiteido_a, '車両の損壊程度（当事者B）': res_syaryounosonkaiteido_b, 'エアバッグの装備（当事者A）': res_eabagunosoubi_a, 'エアバッグの装備（当事者B）': res_eabagunosoubi_b, 'サイドエアバッグの装備（当事者A）': res_saidoeabagunosoubi_a,
            'サイドエアバッグの装備（当事者B）': res_saidoeabagunosoubi_b, '人身損傷程度（当事者A）': res_jinsinsonsyouteido_a, '人身損傷程度（当事者B）': res_jinsinsonsyouteido_b, '地点_緯度（北緯）': data[i][54], '地点_経度（東経）': data[i][55],
            '曜日(発生年月日)': res_youbi, '祝日(発生年月日)': res_syukujitu, '地点_緯度（北緯）_10進数': data[i][58], '地点_経度（東経）_10進数': data[i][59], '日の出時刻　　時': data[i][60], '日の出時刻　　分': data[i][61],
            '日の入り時刻　　時': data[i][62], '日の入り時刻　　分': data[i][63], 'オートマチック車（当事者A）': data[i][64], 'オートマチック車（当事者B）': data[i][65], 'サポカー（当事者A）': data[i][66], 'サポカー（当事者B）': data[i][67],
            '認知機能検査経過日数（当事者A）': data[i][68], '認知機能検査経過日数（当事者B）': data[i][69], '運転練習の方法（当事者A）': data[i][70], '運転練習の方法（当事者B）': data[i][71]
        })

    print(u'処理終了')
