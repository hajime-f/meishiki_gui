import kanshi_data as kd
from datetime import datetime as dt
from datetime import timedelta as td



class Meishiki:

    def __init__(self, birthday, t_flag, sex):
        
        self.birthday = birthday
        self.t_flag = t_flag
        self.sex = sex
        self.meishiki = {}


    def is_setsuiri_year(self):

        start = dt(year = self.birthday.year, month = 1, day = 1, hour = 0, minute = 0)
        end = dt(year = self.birthday.year, month = 2, day = kd.setsuiri[1], hour = 0, minute = 0)
        if start <= self.birthday < end:
            return -1
        else:
            return 0
        

    def find_year_kanshi(self):
        
        sixty_kanshi_idx = (self.birthday.year - 3) % 60 - 1 + self.is_setsuiri_year()
        y_kan, y_shi = kd.sixty_kanshi[sixty_kanshi_idx]
        return y_kan, y_shi
    
    
    def is_setsuiri_month(self):

        start = dt(year = self.birthday.year, month = self.birthday.month, day = 1, hour = 0, minute = 0)
        end = dt(year = self.birthday.year, month = self.birthday.month, day = kd.setsuiri[self.birthday.month - 1], hour = 0, minute = 0)
        if start <= self.birthday < end:
            return -1
        else:
            return 0
    
    
    def find_month_kanshi(self, y_kan):
        
        month = self.birthday.month - 1 + self.is_setsuiri_month()
        m_kan, m_shi = kd.month_kanshi[y_kan][month]
        return m_kan, m_shi
        

    def find_day_kanshi(self):
        
        d = self.birthday.day + kd.kisu_table[(self.birthday.year - 1926) % 80][self.birthday.month - 1] - 1
        if d >= 60:
            d -= 60
        d_kan, d_shi = kd.sixty_kanshi[d]
        return d_kan, d_shi


    def find_time_kanshi(self, d_kan):
        
        time_span = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 24]
        
        for i in range(len(time_span) - 1):
            
            from_dt = dt(year = self.birthday.year, month = self.birthday.month, day = self.birthday.day,
                         hour = time_span[i], minute = 0)
            if (i == 0) or (i == len(time_span)):
                to_dt = from_dt + td(hours = 0, minutes = 59)
            else:
                to_dt = from_dt + td(hours = 1, minutes = 59)
                
            if from_dt <= self.birthday <= to_dt:
                t_kan, t_shi = kd.time_kanshi[d_kan][i]
                return t_kan, t_shi


    def find_zokan(self, shi):
        
        p = self.is_setsuiri_month()

        if p == 0:
            setsuiri = dt(year = self.birthday.year, month = self.birthday.month, day = kd.setsuiri[self.birthday.month - 1], hour = 0, minute = 0)
        else:
            if self.birthday.month == 1:
                setsuiri = dt(year = self.birthday.year - 1, month = 12, day = kd.setsuiri[11], hour = 0, minute = 0)
            else:
                setsuiri = dt(year = self.birthday.year, month = self.birthday.month - 1, day = kd.setsuiri[self.birthday.month - 2], hour = 0, minute = 0)
        
        if shi == 6:
            delta1 = td(days = kd.zokan_time[shi][0][0], hours = kd.zokan_time[shi][0][1])
            delta2 = td(days = kd.zokan_time[shi][1][0], hours = kd.zokan_time[shi][1][1])
        else:
            delta = td(days = kd.zokan_time[shi][0], hours = kd.zokan_time[shi][1])

        if shi == 6:
            if setsuiri + delta1 >= self.birthday:
                zokan = kd.zokan[shi][0]
            elif setsuiri + delta1 < self.birthday <= setsuiri + delta2:
                zokan = kd.zokan[shi][1]
            else:
                zokan = kd.zokan[shi][2]
        else:
            if setsuiri + delta >= self.birthday:
                zokan = kd.zokan[shi][0]
            else:
                zokan = kd.zokan[shi][1]
                
        return zokan
    
        
    def build_meishiki(self):
        
        # 天干・地支を得る
        y_kan, y_shi = self.find_year_kanshi()
        m_kan, m_shi = self.find_month_kanshi(y_kan)
        d_kan, d_shi = self.find_day_kanshi()
        if self.t_flag:
            t_kan, t_shi = self.find_time_kanshi(d_kan)
        else:
            t_kan = -1
            t_shi = -1

        # 蔵干を得る
        y_zkan = self.find_zokan(y_shi)
        m_zkan = self.find_zokan(m_shi)
        d_zkan = self.find_zokan(d_shi)
        if self.t_flag:
            t_zkan = self.find_zokan(t_shi)
        else:
            t_zkan = -1
        
        tenkan = [y_kan, m_kan, d_kan, t_kan]
        chishi = [y_shi, m_shi, d_shi, t_shi]
        zokan = [y_zkan, m_zkan, d_zkan, t_zkan]
        
        nenchu = [y_kan, y_shi, y_zkan]
        getchu = [m_kan, m_shi, m_zkan]
        nitchu = [d_kan, d_shi, d_zkan]
        jichu  = [t_kan, t_shi, t_zkan]
        
        # 五行（木火土金水）のそれぞれの数を得る
        gogyo = [0] * 5
        for t in tenkan:
            if t != -1:
                gogyo[kd.gogyo_kan[t]] += 1
        for s in chishi:
            if s != -1:
                gogyo[kd.gogyo_shi[s]] += 1

        # 通変を得る
        tsuhen = []
        for i in tenkan + zokan:
            if i == -1:
                tsuhen.append(-1)
            else:
                tsuhen.append(kd.kan_tsuhen[tenkan[2]].index(i))

        # 十二運を得る
        twelve_fortune = []
        for i in chishi:
            if i == -1:
                twelve_fortune.append(-1)
            else:
                twelve_fortune.append(kd.twelve_table[tenkan[2]][i])

        # 調候を得る
        kd.choko[d_kan][self.birthday.month - 1]

        # 空亡を得る
        d = self.birthday.day + kd.kisu_table[(self.birthday.year - 1926) % 80][self.birthday.month - 1] - 1
        if d >= 60:
            d -= 60  # d が 60 を超えたら 60 を引く
        kubo = kd.kubo[d // 10]
        
        # クラス変数 meishiki に情報を追加する
        self.meishiki.update({"tenkan": tenkan})
        self.meishiki.update({"chishi": chishi})
        self.meishiki.update({"zokan" : zokan})
        self.meishiki.update({"nenchu": nenchu})
        self.meishiki.update({"getchu": getchu})
        self.meishiki.update({"nitchu": nitchu})
        self.meishiki.update({"jichu" : jichu})
        self.meishiki.update({"gogyo" : gogyo})
        self.meishiki.update({"tsuhen": tsuhen})
        self.meishiki.update({"twelve_fortune": twelve_fortune})
        self.meishiki.update({"choko": choko})
        self.meishiki.update({"kubo": kubo})



                
