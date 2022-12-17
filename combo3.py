import json
import collections
import tkinter as tk
import tkinter.ttk as ttk

LANG_DATA = """
{
    "ひらがな": {
        "あ": ["亜", "阿", "吾", "㋐"],
        "い": [],
        "う": [],
        "え": [],
        "お": []
    },
    "カタカナ": {
        "ア": [],
        "イ": [],
        "ウ": [],
        "エ": [],
        "オ": []
    },
    "alphabet": {
        "a": [],
        "i": [],
        "u": [],
        "e": [],
        "o": []
    }
}
"""

lang = json.loads(LANG_DATA, object_pairs_hook=collections.OrderedDict)
root = tk.Tk()

cb1 = ttk.Combobox(root, state='readonly')
cb1['values'] = list(lang.keys())
cb1.grid(row=1, column=1)

cb2 = ttk.Combobox(root, state='readonly')
cb2.grid(row=1, column=2)

cb3 = ttk.Combobox(root, state='readonly')
cb3.grid(row=1, column=3)

def cb1_selected(event):
    cb2['values'] = list(lang[cb1.get()].keys())
    cb2.set('')

def cb2_selected(event):
    cb3['values'] = lang[cb1.get()][cb2.get()]
    cb3.set('')

cb1.bind('<<ComboboxSelected>>', cb1_selected)
cb2.bind('<<ComboboxSelected>>', cb2_selected)

root.mainloop()
