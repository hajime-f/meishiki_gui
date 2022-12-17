import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("780x400")
app.title("命式生成プログラム Ver.1.0")
app.resizable(False, False)

def button_callback():
    print(combobox_1.get())
    print(combobox_6.get())
    print(combobox_2.get())
    print(combobox_3.get())
    print(combobox_4.get())
    print(combobox_5.get())


dict = {'西暦': ['1912年', '1926年', '1989年'], '昭和': ['53年', '54年', '55年']}

def cb1_selected(event):
    combobox_6.configure(values=dict[combobox_1.get()])
    combobox_6.set(dict[combobox_1.get()][0])


combobox_1 = ctk.CTkComboBox(app, values=list(dict.keys()), command=cb1_selected)
combobox_1.pack(pady=10, padx=10)
combobox_1.set("西暦")
combobox_1.place(x=35, y=35)

combobox_6 = ctk.CTkComboBox(app, values=dict[combobox_1.get()])
combobox_6.pack(pady=10, padx=10)

combobox_2 = ctk.CTkComboBox(app, values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"], width=100)
combobox_2.pack(pady=10, padx=10)
combobox_2.set("1月")
combobox_2.place(x=365, y=35)

combobox_3 = ctk.CTkComboBox(app, values=["1日", "2日", "3日", "4日", "5日", "6日", "7日", "8日", "9日", "10日", "11日", "12日", "13日", "14日", "15日", "16日", "17日", "18日", "19日", "20日", "21日", "22日", "23日", "24日", "25日", "26日", "27日", "28日", "29日", "30日", "31日"], width=100)
combobox_3.pack(pady=10, padx=10)
combobox_3.set("1日")

combobox_4 = ctk.CTkComboBox(app, values=["0時", "1時", "2時", "3時", "4時", "5時", "6時", "7時", "8時", "9時", "10時", "11時", "12時", "13時", "14時", "15時", "16時", "17時", "18時", "19時", "20時", "21時", "22時", "23時"], width=100)
combobox_4.pack(pady=10, padx=10)
combobox_4.set("0時")

combobox_5 = ctk.CTkComboBox(app, values=["00分", "01分", "02分", "03分", "04分", "05分", "06分", "07分", "08分", "09分", "10分", "11分", "12分", "13分", "14分", "15分", "16分", "17分", "18分", "19分", "20分", "21分", "22分", "23分", "24分", "25分", "26分", "27分", "28分", "29分", "30分", "31分", "32分", "33分", "34分", "35分", "36分", "37分", "38分", "39分", "40分", "41分", "42分", "43分", "44分", "45分", "46分", "47分", "48分", "49分", "50分", "51分", "52分", "53分", "54分", "55分", "56分", "57分", "58分", "59分"], width=100)
combobox_5.pack(pady=10, padx=10)
combobox_5.set("00分")

button_1 = ctk.CTkButton(master=app, command=button_callback, text="命式生成")
button_1.pack(pady=10, padx=10)



app.mainloop()


