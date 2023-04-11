import unicodedata
import re
import datetime

# 各年号の元年を定義
eraDict = {
    "昭和": 1926,
    "平成": 1989,
    "令和": 2019,
}


def wareki_converter(text):
    
    # 正規化
    normalized_text = unicodedata.normalize("NFKC", text)
    
    # 西暦の場合を処理
    if normalized_text[0:2] == '西暦':
        year = normalized_text[2:6]
        if normalized_text[8:9] == '月':
            month = normalized_text[7:8]
            if normalized_text[10:11] == '日':
                day = normalized_text[9:10]
            else:
                day = normalized_text[9:11]
        else:
            month = normalized_text[7:9]
            if normalized_text[11:12] == '日':
                day = normalized_text[10:11]
            else:
                day = normalized_text[10:12]
        return datetime.date(int(year), int(month), int(day))
    
    # 年月日を抽出
    pattern = r"(?P<era>{eraList})(?P<year>[0-9]{{1,2}}|元)年(?P<month>[0-9]{{1,2}})月(?P<day>[0-9]{{1,2}})日".format(eraList="|".join(eraDict.keys()))
    date = re.search(pattern, normalized_text)
    
    # 抽出できなかったら終わり
    if date is None:
        print("Cannot convert to western year")
        
    # 年を変換
    for era, startYear in eraDict.items():
        if date.group("era") == era:
            if date.group("year") == "元":
                year = eraDict[era]
            else:
                year = eraDict[era] + int(date.group("year")) - 1
                
    # date型に変換して返す
    return datetime.date(year, int(date.group("month")), int(date.group("day")))


def time_converter(date, time_text):
    
    d = date.strftime("%Y-%m-%d")
    if time_text == '':
        return datetime.datetime.strptime(d, '%Y-%m-%d'), False
    else:
        birthday = datetime.datetime.strptime(d + ' ' + time_text, '%Y-%m-%d %H時%M分')

        # サマータイムを考慮する
        if datetime.datetime(year=1948, month=5, day=2) <= birthday < datetime.datetime(year=1951, month=9, day=8):
            birthday = datetime.datetime(year = birthday.year, month = birthday.month, day = birthday.day,
                                         hour = birthday.hour - 1, minute = birthday.minute)
        
        return birthday, True
    
    
