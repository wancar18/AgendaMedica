from tkcalendar import DateEntry 

import ttkbootstrap as ttk

def formatar_hora(hora_str):
    if len(hora_str) == 4 and ":" not in hora_str:
        return hora_str[:2] + ":" + hora_str[2:]
    return hora_str
