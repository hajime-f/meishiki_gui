import sys
from datetime import datetime as dt

import kanshi_data as kd


class Unsei:
    """
    大運のクラス
    """

    def __init__(self, meishiki):

        self.meishiki = meishiki
        self.birthday = meishiki.birthday
        self.sex = meishiki.sex
        self.unsei = {}

    def convert_year_ratio(self, birthday):
        """
        ＜機能＞
        生年月日から前の節入日までの日数と、生年月日から次の節入日までの日数との比を、
        10年に占める割合に直す。
        例：8日：22日→3年：7年
        ＜入力＞
          - brithday（datetime）：生年月日
        ＜出力＞
          - year_ratio_list（list）：10年に占める割合
        """

        for i, s in enumerate(kd.setsuiri):
            p = self.meishiki.is_setsuiri(birthday, birthday.month)
            if (s[0] == birthday.year) and (s[1] == birthday.month):
                if not p:
                    k = kd.setsuiri[i+1]
                    previous_setsuiri = dt(year=s[0], month=s[1], day=s[2],
                                           hour=s[3], minute=s[4])
                    next_setsuiri = dt(year=k[0], month=k[1], day=k[2],
                                       hour=k[3], minute=k[4])
                else:
                    k = kd.setsuiri[i-1]
                    previous_setsuiri = dt(year=k[0], month=k[1], day=k[2],
                                           hour=k[3], minute=k[4])
                    next_setsuiri = dt(year=s[0], month=s[1], day=s[2],
                                       hour=s[3], minute=s[4])
                break

        diff_previous = birthday - previous_setsuiri   # 生年月日から前の節入日までの日数
        diff_next = next_setsuiri - birthday           # 生年月日から次の節入日までの日数

        # ３日間を１年に置き換えるので、３除した値を丸める
        p_year = round(
            (diff_previous.days + (diff_previous.seconds / 60 / 60 / 24)) / 3)
        n_year = round(
            (diff_next.days + (diff_next.seconds / 60 / 60 / 24)) / 3)

        year_ratio_list = [p_year, n_year]

        return year_ratio_list

    def is_junun_gyakuun(self, sex, y_kan):
        """
        ＜機能＞
        大運が順運か逆運かを判定する
        ＜入力＞
          - y_kan（int）：年柱天干の番号
          - self.sex（int）：性別の番号
        ＜出力＞
          - 順運（1）または逆運（0）の二値
        ＜異常検出＞
        取得できなかった場合はエラーメッセージを出力して強制終了する
        """

        if (((y_kan % 2) == 0) and (sex == 0)) or (((y_kan % 2) == 1) and (sex == 1)):
            return 1   # 年柱天干が陽干の男命 or 年柱天干が陰干の女命は、順運

        elif (((y_kan % 2) == 1) and (sex == 0)) or (((y_kan % 2) == 0) and (sex == 1)):
            return 0   # 年柱天干が陽干の女命 or 年柱天干が陰干の男命は、逆運

        else:
            print('大運の順逆を判定できませんでした。')
            sys.exit(1)

    def find_kanshi_idx(self, kan, shi, p):
        """
        六十干支表から所定の干支のインデクスを返す
        """
        for idx, sk in enumerate(kd.sixty_kanshi):
            if (sk[0] == kan) and (sk[1] == shi):
                return idx + p

        print('干支が見つかりませんでした。')
        sys.exit(1)

    def is_kango(self, tenkan_zokan, kan):

        for i, k in enumerate(tenkan_zokan):
            if k == -1:
                continue
            if k == kd.kango[kan]:
                return i
        return -1

    def is_shigo(self, chishi, shi):

        for i, s in enumerate(chishi):
            if s == -1:
                continue
            if s == kd.shigo[shi]:
                return i
        return -1

    def is_hogo(self, chishi, shi):

        chishi_p = chishi + shi

        for i, h in enumerate(kd.hogo):
            if (h[0][0] in chishi_p) and (h[0][1] in chishi_p) and (h[0][2] in chishi_p):
                return i
        return -1

    def append_daiun(self):
        """
        大運を命式に追加する
        """
        daiun = []
        year_ratio_list = self.convert_year_ratio(self.birthday)
        meishiki = self.meishiki.meishiki

        # 順運か逆運か？
        if self.is_junun_gyakuun(self.meishiki.sex, meishiki["nenchu"][0]):
            ry = year_ratio_list[1]  # 次の節入日が立運の起算日
            p = 1                    # 六十干支表を順にたどる
        else:
            ry = year_ratio_list[0]  # 前の節入日が立運の起算日
            p = -1                   # 六十干支表を逆にたどる

        idx = self.find_kanshi_idx(
            meishiki["getchu"][0], meishiki["getchu"][1], p)

        for n in list(range(10, 140, 10)):

            if idx >= 60:
                idx = 0
            kan, shi = kd.sixty_kanshi[idx]
            tsuhen = kd.kan_tsuhen[meishiki["nikkan"]].index(kan)

            kango = self.is_kango(
                meishiki["tenkan"] + meishiki["zokan"], kan)  # 干合
            shigo = self.is_shigo(meishiki["chishi"], shi)  # 支合

            if not meishiki["hogo"]:
                hogo = self.is_hogo(meishiki["chishi"], shi)    # 方合
            else:
                hogo = -1

            sango = is_sango(meishiki["chishi"], shi)  # 三合
            if sango == -1:
                hankai = is_hankai(meishiki["chishi"], shi)  # 半会
            else:
                hankai = -1
            tc = is_tensen_chichu(meishiki.nitchu[1], tsuhen, shi)  # 天戦地冲
            if tc == -1:
                chu = is_chu(meishiki.chishi, shi)  # 冲
            else:
                chu = -1
            kei = is_kei(meishiki.chishi, shi)  # 刑
            gai = is_gai(meishiki.chishi, shi)  # 害

            daiun.append([ry, kan, shi, tsuhen, kango, shigo,
                         hogo, sango, hankai, tc, chu, kei, gai])

            ry += 10
            idx += p

        return daiun

    def append_nenun(self, daiun):
        """
        年運を命式に追加する
        """
        nenun = []
        idx = (self.meishiki.birthday.year - 3) % 60 - 1
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
