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

        chishi_p = chishi + [shi]

        for i, h in enumerate(kd.hogo):
            if (h[0][0] in chishi_p) and (h[0][1] in chishi_p) and (h[0][2] in chishi_p):
                return i
        return -1

    def is_sango(self, chishi, shi):

        chishi_p = chishi + [shi]

        for i, s in enumerate(kd.sango):
            if (s[0][0] in chishi_p) and (s[0][1] in chishi_p) and (s[0][2] in chishi_p):
                return i
        return -1

    def is_hankai(self, chishi, shi):

        for i, h in enumerate(kd.hankai):
            if ((h[0][0] in chishi) and (h[0][1] in [shi])) or ((h[0][0] in [shi]) and (h[0][1] in chishi)):
                return i
        return -1

    def is_tensen_chichu(self, nisshi, tsuhen, shi):

        if (shi == kd.hitsuchu_rev[nisshi]) and (tsuhen == 6):
            return 1
        return -1

    def is_chu(self, chishi, shi):

        ch = [chishi[0]] + [-1] + [chishi[2]] + [chishi[3]]
        for i, s in enumerate(ch):
            if s == kd.hitsuchu_nodir[shi]:
                return i
        return -1

    def is_kei(self, chishi, shi):

        for i, s in enumerate(chishi):
            if s == kd.kei[shi]:
                return i
        return -1

    def is_gai(self, chishi, shi):

        for i, s in enumerate(chishi):
            if s == kd.gai[shi]:
                return i
        return -1

    def is_kango_y(self, tenkan_zokan, d_kan, kan):

        for i, k in enumerate(tenkan_zokan):
            if k == kd.kango[kan]:
                return i
        if d_kan == kd.kango[kan]:
            return len(tenkan_zokan)
        return -1

    def is_shigo_y(self, chishi, d_shi, shi):

        for i, s in enumerate(chishi):
            if s == kd.shigo[shi]:
                return i
        if d_shi == kd.shigo[shi]:
            return len(chishi)
        return -1

    def is_hogo_y(self, chishi, d_shi, shi, flag1):

        for i, c in enumerate(chishi):
            hogo = [c, d_shi, shi]
            for j, h in enumerate(kd.hogo):
                if (h[0][0] in hogo) and (h[0][1] in hogo) and (h[0][2] in hogo):
                    return j
        if flag1:
            return self.is_hogo(chishi, shi)
        return -1

    def is_sango_y(self, chishi, d_shi, shi, flag2):

        for i, c in enumerate(chishi):
            sango = [c, d_shi, shi]
            for j, s in enumerate(kd.sango):
                if (s[0][0] in sango) and (s[0][1] in sango) and (s[0][2] in sango):
                    return j
        if flag2:
            return self.is_sango(chishi, shi)
        return -1

    def is_hankai_y(self, chishi, d_shi, shi):

        for i, h in enumerate(kd.hankai):
            if ((h[0][0] in chishi) and (h[0][1] in [shi])) or ((h[0][0] in [shi]) and (h[0][1] in chishi)) or ((h[0][0] in [shi]) and (h[0][1] in [d_shi])) or ((h[0][0] in [d_shi]) and (h[0][1] in [shi])):
                return i
        return -1

    def is_chu_y(self, chishi, d_shi, shi):

        ch = chishi + [d_shi]
        for i, s in enumerate(ch):
            if s == kd.hitsuchu_nodir[shi]:
                return i
        return -1

    def is_kei_y(self, chishi, d_shi, shi):

        ch = chishi + [d_shi]
        for i, s in enumerate(ch):
            if s == kd.kei[shi]:
                return i
        return -1

    def is_gai_y(self, chishi, d_shi, shi):

        ch = chishi + [d_shi]
        for i, s in enumerate(ch):
            if s == kd.gai[shi]:
                return i
        return -1

    def is_kansatsu(self, d_tsuhen, n_tsuhen):

        if (d_tsuhen == 6 and n_tsuhen == 7) or (d_tsuhen == 7 and n_tsuhen == 6):
            return 1
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

            if not meishiki["sango"]:
                sango = self.is_sango(meishiki["chishi"], shi)  # 三合
            else:
                sango = -1

            if sango == -1:
                hankai = self.is_hankai(meishiki["chishi"], shi)  # 半会
            else:
                hankai = -1

            tc = self.is_tensen_chichu(
                meishiki["nitchu"][1], tsuhen, shi)  # 天戦地冲
            if tc == -1:
                chu = self.is_chu(meishiki["chishi"], shi)  # 冲
            else:
                chu = -1

            kei = self.is_kei(meishiki["chishi"], shi)  # 刑
            gai = self.is_gai(meishiki["chishi"], shi)  # 害

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
        d_idx = 0

        meishiki = self.meishiki.meishiki

        for n in list(range(0, 120)):
            kan, shi = kd.sixty_kanshi[idx]
            tsuhen = kd.kan_tsuhen[self.meishiki.meishiki["nikkan"]].index(kan)

            if (n != ry) and (n % 10 == ry):
                d_idx += 1

            if n >= ry:

                d_kan = daiun[d_idx][1]
                d_shi = daiun[d_idx][2]

                kango = self.is_kango_y(
                    meishiki["tenkan"] + meishiki["zokan"], d_kan, kan)  # 干合
                shigo = self.is_shigo_y(meishiki["chishi"], d_shi, shi)  # 支合

                if not meishiki["hogo"]:
                    flag1 = True
                else:
                    flag1 = False

                if daiun[d_idx][6] == -1:
                    hogo = self.is_hogo_y(
                        meishiki["chishi"], d_shi, shi, flag1)    # 方号
                else:
                    hogo = -1

                if not meishiki["sango"]:
                    flag2 = True
                else:
                    flag2 = False

                if daiun[d_idx][7] == -1:
                    sango = self.is_sango_y(
                        meishiki["chishi"], d_shi, shi, flag2)  # 三合
                else:
                    sango = -1

                if sango == -1:
                    hankai = self.is_hankai_y(
                        meishiki["chishi"], d_shi, shi)  # 半会
                else:
                    hankai = -1

                tc1 = self.is_tensen_chichu(
                    meishiki["nitchu"][1], tsuhen, shi)  # 天戦地冲（命式）
                tc2 = self.is_tensen_chichu(
                    d_shi, kd.kan_tsuhen[d_kan].index(kan), shi)  # 天戦地冲（大運）
                tc = 1 if tc1 == 1 else 2 if tc2 == 1 else -1

                if tc == -1:
                    chu = self.is_chu_y(meishiki["chishi"], d_shi, shi)  # 冲
                else:
                    chu = -1

                kei = self.is_kei_y(meishiki["chishi"], d_shi, shi)  # 刑
                gai = self.is_gai_y(meishiki["chishi"], d_shi, shi)  # 害

                kansatsu = self.is_kansatsu(daiun[d_idx][3], tsuhen)  # 官殺混雑

                nenun.append([n, kan, shi, tsuhen, kango,
                              shigo, hogo, sango, hankai, tc, chu, kei, gai, kansatsu])

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

    tsuhen_character = [
        ['比肩が重なる比和の組み合わせで、比肩本来の意味が非常に強調され、抜群の出世運を持つ強運の組み合わせとなります。この組み合わせを月柱に持つ人は、例外なく強烈な自我と自負心を持っています。また、天才的なひらめき、センスなどがあり、一般人にはないアクの強さを発揮するので、仲間内でもひときわ目立った存在となります。自己顕示欲も旺盛で、大言壮語する傾向があり、また自分の言葉に酔う傾向もありますが、実力を伴うことが多いので、さして気にする必要もないでしょう。強烈なトップ運ですが、上に立ったとき、往々にしてワンマンになり、たとえ本人は気配りしているつもりでも、他からは強引で押し付けがましく見られます。その点は注意する必要があります。女性は運気が強くなりすぎるため、ときにマイナス傾向が生じます。世の中でバリバリ働いている女性なら問題ありませんが、専業主婦志向の女性は、結婚がスムーズに運ばなかったり、ちょっと頼りない男性と一緒になって苦労する可能性があるので注意してください。自我が強いタイプです。迷いがなく、はっきりと自己主張します。そのため、状況判断を誤ると波紋が広がったり、周囲と衝突したりすることになるので注意が必要です。親切や世話焼きは押し付けにならないようにすることも大切です。',  # 比肩 x 比肩
         '同じ五行に属する比和の関係で、日干の意味が吉凶ともに強調されます。このタイプは、自分の思いを通さないと気の済まない性格です。そのためトラブルメーカー的な色彩が強くなり、さらに口が悪いので、敵を作って孤立しやすくなります。売られたケンカは買うタイプで、闘争心も旺盛。穏やかさ、鷹揚さといったものとは無縁の人が多く、その人生も必然的に浮き沈みが激しくなるのです。比劫星が多いので、この比劫星を生み出す印星があると、人生の浮沈はいっそう大きくなります。印綬があれば、まだ野心の達成に追い風が吹きますが、偏印があると境遇が定まらず、人格的にも難しさが増してきます。一方、比劫星を制する官星があると、比劫星の自立心、独立して一家をなそうとする気概に、官星の制御が働いて立身運になります。他の通変星の影響次第で、運気・気質が大きく変わってくる組み合わせなので、命式をよく分析するようにしてください。全般に運はあまり良いとは言えず、目が出にくい傾向がありますが、原因の多くは強すぎる自我にあります。人格を丸くしていかないと展望は開けません。また、この組み合わせのように劫財が旺じると、劫財は傷官を好むので、女性は男まさりで夫と衝突しがちでしょう。自分の主張を通さないと気が済まないタイプです。闘争心が強いため、言葉にトゲが現れることがあり、作らなくてもいい敵を作ってしまって損をすることがあります。生家から独立し、苦労を重ねた後に成功する可能性があります。',  # 比肩 x 劫財
         '比肩が食神的になります。つまり、本来比肩に見られるような独立性の強い前向き・負けず嫌いの気質が、次第に自己満足を第一に追い求める食神の楽天性や享楽性に取って代わられるという運気なのです。月柱にこの組み合わせを持つタイプは、自分のことで頭がいっぱいになり、人のことまでなかなか頭が回りません。自分が楽しむこと、自分の望むことには貪欲で、ブレーキをかける必要を認めないため、とことん行くところまで行ってしまいます。それがスキャンダラスな事件に結びつくことも少なくないので、多少の自戒は絶対に必要です。反面ことタイプは、優れた文学性を持っています。それも難解な方面のそれではなく、大衆性のある、恋愛や人情物、推理などの分野で、自分の生き様が反映できる分野に適性と才能があるのです。このことは、他の分野にも当てはまります。好きなこと、やりたいことを抑えることのできないタイプですから、それを自覚し、好きなことをやって食べていく道を探るべきでしょう。温厚そうに見えますが、心のベクトルは常に自分を満足させることに向かっていて、周囲への配慮に欠けるきらいがあります。わがままを通せる環境では、特に自制心を働かせることに注意が必要です。表現力に優れ、好きなことを職業に選べば伸びるタイプです。',  # 比肩 x 食神
         '比肩が傷官的になっていきます。比肩の明るく前向きに前進する建設的な気質・運気に、次第に召喚的な影が差し込み、高いプライドを満足させられるような境遇が得られないため、内向性が強まっていくという運気なのです。これは、人生の比較的早い時点で、何らかの挫折を経験することを暗示しています。その挫折を深刻に受け止めず、前向きに受け止めれば、その後の人生にさして尾を引くことはないはずなのですが、傷官の影響から深刻に受け止めがちのため、その思いに引きずられて運気が悪化し、性格も屈折してくることが多いのです。比肩の影響で、見かけは豪胆、あるいは強気に見える人もいますが、内面は繊細で、取り越し苦労をしたり、ちょっとしたことを気にかけ、長く心の中で引きずりがちな人です。ものを考えるとき、悲観的になったり、否定的になる傾向があります。これは傷官の影響ですが、よくありません。傷官に引きずられず、もともと持っている比肩のシンプルな強さに立ち返って、楽観的・肯定的に物事に対処するようにしていけば、運気は改善されていきます。元気があって発言も強気ですが、内面は意外と繊細で傷つきやすいタイプです。結果を出せなかったとき、言い訳や責任転嫁をしていると信用を失うことになるので注意が必要です。失敗や挫折を引きずらないように、ポジティブに物事に対処していけば見通しが明るいでしょう。',  # 比肩 x 傷官
         '地星の比肩が天星の偏財を剋す逆剋です。逆剋は、一般には障害と見ます。では、何のどんな障害に出会う可能性が高いかというと、比肩は自分自身を表し、年柱や月柱の偏財は父親（男女共通）もしくは妻・愛人（男性の場合）なので、自分が父を剋して迷惑をかけるか、父が病弱、ないし女性関係でトラブルが生じる暗示があると推理するわけです。また、自分自身について見れば、偏財は財運ですから、財運に障害が出、金が入っても残らないか、見栄によって財を散じ、事業にトラブルが生じやすいなどと見るのです。ただし、剋すほうの比肩に、自力で開運して財を掴む力がありますから、食いつめるといったことはないでしょう。月柱にこの組み合わせを持つタイプは強い個人主義者で、かつ、相当な自信家です。そのため対人関係はあまりスムーズとは言えませんが、本人はさして気にしません。一芸に秀で、その道のトップに立ちうる素質を持っていますが、それは個人的な才覚・才能・技術・センスを生かした分野に限定され、総合的な指導力、管理能力の要求される分野では目が出にくい傾向があります。音楽（クラシック）のセンスのよいものが多く、自分で演じなければ鑑賞の趣味をもちます。財布の紐が緩いタイプで、散財することがあります。見栄による出費や共同事業による損失には、特に注意が必要です。自信家で個人主義的のため、その特質を生かせる仕事を選ぶと成功の可能性は高まります。例えば、一つの技芸を極める道を進むことが成功のカギになるでしょう。',  # 比肩 x 偏財
         '比肩が正財を剋します。地が天を剋す逆剋の障害運ですが、この場合は比肩を自分と見れば、自分が正財の司る財運を支配する（剋）形ですから、相当な財運があり、また、男性の場合は正財を妻と見るので、支配できる妻、すなわち夫を立て、よく家庭を切り盛りしてくれる良妻に恵まれると見ることができるのです。月柱にこの組み合わせを持つタイプは、現実的・実務的な知性が発達しており、実利を重んじます。自分の置かれたポジションを客観的に把握し、ポジションに見合った役割を演じることができますが、理想は高く、本当の自分は違うんだという意識が、心のどこかに潜んで切ることが多いようです。自己過信、強引、無茶の一面もあります。相当な負けず嫌いで努力家ですが、そうした面はあまり表には出しません。面倒見がよく、下からの信望のあつい人で、かなりの出世運があります。蓄財精神が発達しており、うまくいくいかないは別として、多くは財テクなど、蓄財に熱心なタイプでもあります。金銭の出入りは忙しいですが、最終的には財産を築けるタイプです。負けず嫌いな努力家で、実務能力にも優れているため、社会で活躍する可能性も高いでしょう。ただし、理想を実現するために強引になりやすい点には注意が必要です。',  # 比肩 x 正財
         '偏官が比肩を剋します。自分の中で権威と権威がぶつかり合っているような形のため、進むべき方向にエネルギーが集中できません。横槍、妨害などのせいで思うように手腕が発揮できず、苦しむ傾向があります。特に月柱にこの組み合わせがあると、開運までにかなりの苦労があります。この人は、自分を引き立ててくれていた人から手のひらを返したように冷遇されたり、今までのポジションから追われたりすることがあります。力はあっても、境遇が整わず、常に何かに頭を抑えられている状態になりやすいのです。素直で人の良いところがありますが、比肩が剋されるため、比肩の強烈な自立性が曖昧になり、また我の強さがストレートに表現できないため、内にこもって屈折したり、覇気に欠けた印象が生じます。マイペースで協調性はあみらない人ですから、個人でできる仕事が適しています。そうした仕事を選べば、じわじわと成功を掴むことができます。屈折した自己表現をしやすく、協調性もあまりないタイプです。目上の引き立てや周囲の援助に期待せず、淡々とマイペースで進められる仕事を選ぶと見通しが明るいでしょう。',  # 比肩 x 偏官
         '正官が比肩を剋し、比肩の自立性・独立性をうまくコントロールしてくれます。その結果、この人は自分の職分を守ってコツコツと業績を積み上げていく、マイペース人間になります。周囲の状況がどうであれ、我関せずといったタイプで、それだけに自負心は強く、職人気質です。この組み合わせを月柱に持つ人は、手堅く、着実に成果を積み上げていくので、かなりの立身運が期待できます。ただ、人を押し除けてでも先に出ようとか、上に立とうという意欲は乏しいことが多く、そうしたことに魅力を感じない人も多いため、実力に比して評価が低いきらいがあるようです。また、態度が大きいというのも、評価を下げる一因です。ここにも職人気質が現れています。へそ曲りで口はよくありません。若いときは苦労しがちですが、着実に自分の世界を確立していきます。周囲に惑わされず、コツコツ実績を積み上げていく職人タイプです。周囲に甘えることが下手なため遅咲きですが、そのうち自分の世界を確立できるでしょう。',  # 比肩 x 正官
         '比肩に偏印性が加わります。気質・運気の核は比肩ですから、自立心旺盛、人に命令されることを嫌い、自我を貫きます。そこに偏印性が加わるため、多少ともあまのじゃくな傾向が生じ、人によっては皮肉っぽい気質となるのです。偏印、比肩とも自分は自分というタイプで、スタイルを変えようとしないため、運気的には援助・引き立て運が薄くなり、目が出るまでには苦労を伴います。また、比肩が強まりますから、財星が剋され、金運に障害が出るか、父親縁が薄くなるなどのマイナスも生じやすくなります。ただ、弱音を吐かない芯の強さや、マイペースで生きることができるという強みがあるので、焦らず、じっくりと自分の世界を追及してください。そうすれば、おのずと運気は開けてきます。他人に頼らず、自分の信じた道を進むタイプです。人の意見には耳を貸しませんし、あまのじゃくなところもあるため、周囲の引き立てはあまり期待できないかもしれません。手に職を持ち、自力で生きていく覚悟を決めれば、納得のいく結果を得られるでしょう。',  # 比肩 x 偏印
         '比肩に印綬性が加わります。両星ともに毛並みのよい通変星ですから、たとえ育ちが貧しくても、下積みの境遇にいようとも、人げとしての気品やプライドは失いません。芯に比肩があるため、性格は強く、人の同情を買うことを嫌い、何事も自分の力で解決しようとします。独立独歩の気概が旺盛で、負けん気も相当強いのですが、そこに印綬が加わるため、そうした気質の現れ方はソフトになり、人への気配りも細やかになります。一芸に秀で、頭のいい人ですが（特に月柱にこの組み合わせがある場合）、自分の世界をしっかりと守って、余計な色気は出しません。自分を知っているタイプですから、付き合っていて気持ちがよく、人間に安定感があります。運気も同様で、着実に足場を固め、自分のポジションを確保し、一度手に入れたものは失うことがないので、充実した人生を送れます。ただ、商売的な才覚は乏しいので、その方面は避けた方が無難でしょう。品がよくプライドの高いタイプです。周囲の人に対しては物腰柔らかですが、意に反することで人に頭を下げることはありません。賢く、一芸に秀でているため、努力によって成功する可能性は高いでしょう。',],  # 比肩 x 印綬
        ['同じ五行の陰陽で、比和の関係ですから、その五行の影響が顕著になります。この組み合わせが月柱にあれば、勝負師的な勘のよさ、思い切りのよさが目立ち、実力一方でのしあがっていくタイプです。年柱にあっても基本的には同じですが、ただ、出世運は月柱の場合より多少よくなるようです。時柱にあるときは、晩年の孤独・不如意に注意する必要があります。このタイプは、人の言うことにはあまり耳を貸しません。相当な意地っ張りで負けることを嫌い、努力を惜しまないので、その努力が前向きの方向に働けば、かなりの立身が期待できますが、後ろ向きに働くと、アウトロー的な生き方に直結してしまいます。また、意地を通すためなら、理不尽であれ損であれ、やってしまうという激しい気性を秘めていますから、往々にして妻や夫を剋し、家族を剋します。比肩と劫財では劫財の性格が強く現れやすいので、劫財の脅威には注意が必要です。女性は、太っ腹な部分と投げやりな部分がその時の気分によって現れる、気難しいタイプになりやすいようです。並の男では太刀打ちできない強さや激しさがあるため、婚期は遅れがちです。腕・才覚一本の仕事に就けば相当力を発揮します。平凡なOLは、あまり向いていません。思い切りがよく、実行力があり、世話好きです。負けず嫌いで人の意見には耳を貸さず、自分の実力でのし上がっていくタイプです。目標達成のためには手段を選ばないところがあり、周囲を振り回すことがある点に注意が必要です。',  # 劫財 x 比肩
         '劫財が重ねて現れた比和です。まれに権力を握るものが出ますが、多くは幸運とは言えません。この組み合わせが月柱にあれば、スキャンダラスな事件に巻き込まれたり、職業・境遇が再三変わるなど、なにかと困難に直面しやすくなりますし、年柱にあれば、親に恵まれず、極貧、若い時点での親との生死別など、苦労が多くなります。人格的にも屈折が激しく、極端な場合は非常で反社会的な凶行に及ぶこともあります。特に劫財を生む印星（とりわけ偏印）があると、脅威はいっそう増します。しかし、劫財を制する官星があると、逆に非常に高邁な精神の持ち主になることも少なくないので、この組み合わせはどうしても官星の助けが欲しいのです。凶暗示の強い組み合わせではありますが、大凶は行き着くところまで行くと吉に転じるのが法則です。そのため、この組み合わせで玉の輿に乗ったり、一世を風靡するような成功者が出ることもあるので、捨て鉢になったり、自分で自分の才能を殺すことのないよう注意してください。自分の欲望に忠実に生きるタイプで波乱万丈になりやすく、ともすればスキャンダルに発展することもあるので我を抑える努力が必要です。境遇が変わりやすいので、仕事は共同事業を避ける方がよさそうです。生家から早く独立した方が見通しは明るいでしょう。',  # 劫財 x 劫財
         '劫財の荒々しい気性を、穏やかな食神が吸収・緩和しています。そのため、もともとの気質・運気は暴力的・破壊的で、エゴイスティックな傾向が強いのですが、そこに丸さが加わり、次第に円熟してくるといったプラス方向に向かう運気なのです。この人は人生経験を積むにつれて趣味性を帯び、享楽性を増していきます。ただ、その根っこには、劫財に由来する烈々たる権力欲・支配欲が潜んでいますから、食神の小さな満足でも自足してしまう気宇の小ささは、うまいことセーブされ、人生に対する積極性は失いません。こうした積極性は、社会の中でのしあがっていくためには必要不可欠な要素なので、このタイプの出世運は大きくなるわけです。「ほどほど」ができないところに、この組み合わせの運気の誘導力があります。のめり込む性格は権力を握るのに力を与え、大きな立身運として結実しますが、上に立った時が衰運の訪れる時です。極めて落差の大きな運命ですから、体にだけは注意してください。ソフトな安定感を醸し出すタイプです。アイデアが光り、趣味で才能を開花させ、仕事以外にサイドビジネスでも収入を得られるかもしれません。積極性と物事にのめり込む集中力で成果を手に入れます。ただし、過労には気をつけましょう。',  # 劫財 x 食神
         '',  # 劫財 x 傷官
         '',  # 劫財 x 偏財
         '',  # 劫財 x 正財
         '',  # 劫財 x 偏官
         '',  # 劫財 x 正官
         '',  # 劫財 x 偏印
         '',],  # 劫財 x 印綬

    ]
