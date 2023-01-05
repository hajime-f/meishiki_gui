import customtkinter as ctk
from jcc import wareki_converter, time_converter
from meishiki import Meishiki


def main(birthday, t_flag, sex):
    
    meishiki = Meishiki(birthday, t_flag, sex)
    meishiki.build_meishiki()

    

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("895x160")
app.title("命式生成プログラム Ver.1.0")
app.resizable(False, False)

dict = {'西暦': ['1926年', '1927年', '1928年', '1929年', '1930年', '1931年', '1932年', '1933年', '1934年', '1935年', '1936年', '1937年', '1938年', '1939年', '1940年', '1941年', '1942年', '1943年', '1944年', '1945年', '1946年', '1947年', '1948年', '1949年', '1950年', '1951年', '1952年', '1953年', '1954年', '1955年', '1956年', '1957年', '1958年', '1959年', '1960年', '1961年', '1962年', '1963年', '1964年', '1965年', '1966年', '1967年', '1968年', '1969年', '1970年', '1971年', '1972年', '1973年', '1974年', '1975年', '1976年', '1977年', '1978年', '1979年', '1980年', '1981年', '1982年', '1983年', '1984年', '1985年', '1986年', '1987年', '1988年', '1989年', '1990年', '1991年', '1992年', '1993年', '1994年', '1995年', '1996年', '1997年', '1998年', '1999年', '2000年', '2001年', '2002年', '2003年', '2004年', '2005年', '2006年', '2007年', '2008年', '2009年', '2010年', '2011年', '2012年', '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年', '2020年', '2021年', '2022年', '2023年', '2024年', '2025年', '2026年', '2027年', '2028年', '2029年', '2030年', '2031年', '2032年', '2033年', '2034年', '2035年', '2036年', '2037年', '2038年', '2039年', '2040年', ], '昭和': ['元年', '2年', '3年', '4年', '5年', '6年', '7年', '8年', '9年', '10年', '11年', '12年', '13年', '14年', '15年', '16年', '17年', '18年', '19年', '20年', '21年', '22年', '23年', '24年', '25年', '26年', '27年', '28年', '29年', '30年', '31年', '32年', '33年', '34年', '35年', '36年', '37年', '38年', '39年', '40年', '41年', '42年', '43年', '44年', '45年', '46年', '47年', '48年', '49年', '50年', '51年', '52年', '53年', '54年', '55年', '56年', '57年', '58年', '59年', '60年', '61年', '62年', '63年', '64年'], '平成': ['元年', '2年', '3年', '4年', '5年', '6年', '7年', '8年', '9年', '10年', '11年', '12年', '13年', '14年', '15年', '16年', '17年', '18年', '19年', '20年', '20年', '21年', '22年', '23年', '24年', '25年', '26年', '27年', '28年', '29年', '30年', '31年'], '令和': ['元年', '2年', '3年', '4年', '5年', '6年', '7年', '8年', '9年', '10年', '11年', '12年', '13年', '14年', '15年', '16年', '17年', '18年', '19年', '20年', '21年', '22年']}

def cb1_selected(event):
    combobox_6.configure(values=dict[combobox_1.get()])
    combobox_6.set(dict[combobox_1.get()][0])

    
def button_callback():

    date_text = combobox_1.get() + combobox_6.get() + combobox_2.get() + combobox_3.get()
    date = wareki_converter(date_text)
    
    time_text = combobox_4.get() + combobox_5.get()
    birthday, t_flag = time_converter(date, time_text)

    sex = 0 if combobox_7.get() == "男性" else 1
    
    main(birthday, t_flag, sex)

    
combobox_1 = ctk.CTkComboBox(app, values=list(dict.keys()), command=cb1_selected, width=100)
combobox_1.pack(pady=10, padx=10)
combobox_1.set("西暦")
combobox_1.place(x=35, y=35)

combobox_6 = ctk.CTkComboBox(app, values=dict[combobox_1.get()], width=100)
combobox_6.pack(pady=10, padx=10)
combobox_6.place(x=155, y=35)

combobox_2 = ctk.CTkComboBox(app, values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"], width=100)
combobox_2.pack(pady=10, padx=10)
combobox_2.set("1月")
combobox_2.place(x=275, y=35)

combobox_3 = ctk.CTkComboBox(app, values=["1日", "2日", "3日", "4日", "5日", "6日", "7日", "8日", "9日", "10日", "11日", "12日", "13日", "14日", "15日", "16日", "17日", "18日", "19日", "20日", "21日", "22日", "23日", "24日", "25日", "26日", "27日", "28日", "29日", "30日", "31日"], width=100)
combobox_3.pack(pady=10, padx=10)
combobox_3.set("1日")
combobox_3.place(x=395, y=35)

combobox_4 = ctk.CTkComboBox(app, values=["", "0時", "1時", "2時", "3時", "4時", "5時", "6時", "7時", "8時", "9時", "10時", "11時", "12時", "13時", "14時", "15時", "16時", "17時", "18時", "19時", "20時", "21時", "22時", "23時"], width=100)
combobox_4.pack(pady=10, padx=10)
combobox_4.set("")
combobox_4.place(x=515, y=35)

combobox_5 = ctk.CTkComboBox(app, values=["", "00分", "01分", "02分", "03分", "04分", "05分", "06分", "07分", "08分", "09分", "10分", "11分", "12分", "13分", "14分", "15分", "16分", "17分", "18分", "19分", "20分", "21分", "22分", "23分", "24分", "25分", "26分", "27分", "28分", "29分", "30分", "31分", "32分", "33分", "34分", "35分", "36分", "37分", "38分", "39分", "40分", "41分", "42分", "43分", "44分", "45分", "46分", "47分", "48分", "49分", "50分", "51分", "52分", "53分", "54分", "55分", "56分", "57分", "58分", "59分"], width=100)
combobox_5.pack(pady=10, padx=10)
combobox_5.set("")
combobox_5.place(x=635, y=35)

combobox_7 = ctk.CTkComboBox(app, values=["男性", "女性"], width=100)
combobox_7.pack(pady=10, padx=10)
combobox_7.set("男性")
combobox_7.place(x=755, y=35)

button_1 = ctk.CTkButton(master=app, command=button_callback, text="命式生成", width=220)
button_1.pack(pady=10, padx=10)
button_1.place(x=635, y=100)

app.mainloop()


