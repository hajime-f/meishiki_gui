import kanshi_data as kd
from datetime import datetime as dt

class Unsei:

    def __init__(self, meishiki):

        self.meishiki = meishiki
        self.birthday = meishiki.birthday
        self.sex = meishiki.sex
        self.unsei = {}
        

    def convert_year_ratio(self):
        
        p = self.meishiki.is_setsuiri_month()
        
        if not p:
            previous_setsuiri = dt(year = self.birthday.year, month = self.birthday.month, day = kd.setsuiri[self.birthday.month - 1], hour = 0, minute = 0)
            if self.birthday.month == 12:
                next_setsuiri = dt(year = self.birthday + 1, month = 1, day = kd.setsuiri[0], hour = 0, minute = 0)
            else:
                next_setsuiri = dt(year = self.birthday.year, month = self.birthday.month + 1, day = kd.setsuiri[self.birthday.month], hour = 0, minute = 0)    
        else:
            if self.birthday.month == 1:
                previous_setsuiri = dt(year = self.birthday.year - 1, month = 12, day = kd.setsuiri[11], hour = 0, minute = 0)
            else:
                previous_setsuiri = dt(year = self.birthday.year, month = self.birthday.month - 1, day = kd.setsuiri[self.birthday.month - 2], hour = 0, minute = 0)
            next_setsuiri = dt(year = self.birthday.year, month = self.birthday.month, day = kd.setsuiri[self.birthday.month - 1], hour = 0, minute = 0)

        diff_previous = self.birthday - previous_setsuiri   # 生年月日から前の節入日までの日数
        diff_next = next_setsuiri - self.birthday           # 生年月日から次の節入日までの日数
        
        # ３日間を１年に置き換えるので、３除した値を丸める
        p_year = round((diff_previous.days + (diff_previous.seconds / 60 / 60 / 24)) / 3)
        n_year = round((diff_next.days + (diff_next.seconds / 60 / 60 / 24)) / 3)
        
        year_ratio_list = [p_year, n_year]

        return year_ratio_list


    def is_junun_gyakuun(self, sex, y_kan):
        
        if (((y_kan % 2) == 0) and (sex == 0)) or (((y_kan % 2) == 1) and (sex == 1)):
            return 1   # 年柱天干が陽干の男命 or 年柱天干が陰干の女命は、順運
        
        elif (((y_kan % 2) == 1) and (sex == 0)) or (((y_kan % 2) == 0) and (sex == 1)):
            return 0   # 年柱天干が陽干の女命 or 年柱天干が陰干の男命は、逆運
        
        else:
            exit()

            
    def find_kanshi_idx(self, kan, shi, p):
        
        # 六十干支表から所定の干支のインデクスを返す
        
        for idx, sk in enumerate(kd.sixty_kanshi):
            if (sk[0] == kan) and (sk[1] == shi):
                return idx + p
            
        print('干支が見つかりませんでした。')
        exit()


    def append_daiun(self):
        
        # ＜機能＞
        # 大運を命式に追加する
        
        daiun = []
        year_ratio_list = self.convert_year_ratio()
        
        if self.is_junun_gyakuun(self.meishiki.sex, self.meishiki.meishiki["nenchu"][0]):  # 順運か逆運か？
            ry = year_ratio_list[1]  # 次の節入日が立運の起算日
            p = 1                    # 六十干支表を順にたどる
        else:
            ry = year_ratio_list[0]  # 前の節入日が立運の起算日
            p = -1                   # 六十干支表を逆にたどる
            
        idx = self.find_kanshi_idx(self.meishiki.meishiki["getchu"][0], self.meishiki.meishiki["getchu"][1], p)
        
        for n in list(range(10, 140, 10)):
            
            if idx >= 60:
                idx = 0
            kan, shi = kd.sixty_kanshi[idx]
            tsuhen = kd.kan_tsuhen[self.meishiki.meishiki["nikkan"]].index(kan)
            
            daiun.append([ry, kan, shi, tsuhen])
            ry += 10
            idx += p

        return daiun
    

    def append_nenun(self, daiun):
        
        nenun = []
        idx = (self.meishiki.birthday.year - 3) % 60 - 1 # + self.meishiki.is_setsuiri(2)
        ry = daiun[0][0]
        
        for n in list(range(0, 120)):
            kan, shi = kd.sixty_kanshi[idx]
            tsuhen = kd.kan_tsuhen[self.meishiki.meishiki["nikkan"]].index(kan)
            
            if n >= ry:
                nenun.append([n, kan, shi, tsuhen])
                
            idx += 1
            if idx >= 60:
                idx = 0
                
        return nenun

    
    def build_unsei(self):
        
        # 大運を得る
        daiun = self.append_daiun()
        
        # 年運を得る
        nenun = self.append_nenun(daiun)

        self.unsei.update({"daiun": daiun})
        self.unsei.update({"nenun": nenun})

        
