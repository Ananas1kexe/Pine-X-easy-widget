import tkinter.font
import tkinter as tk
import time
import psutil
import platform
from tkinter import *


root = tk.Tk()
root.geometry('520x425')
root.title('Pine X widget')
root['bg'] = '#000000' 
root.attributes("-alpha", 0.5)  # root.attributes("-alpha", 1) чтобы увиджет не было эффекта прозрачности
root.resizable(width=False, height=False)



def get_date():
    current_time = time.localtime()
    days = ['Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье']
    
    mounths = ['января',
            'февраля',
            'марта',
            'апреля',
            'июня',
            'июля',
            'августа',
            'сентября',
            'октября',
            'ноября',
            'декабря']
    return f'{current_time.tm_mday} {mounths[current_time.tm_mon - 1]}, {days[current_time.tm_wday]}'

    

def get_time():
    current_time = time.localtime()
    hour = current_time.tm_hour if current_time.tm_hour >= 10 else '0'+str(current_time.tm_hour)
    minute = current_time.tm_min if current_time.tm_min >= 10 else '0'+str(current_time.tm_min)
    secund = current_time.tm_sec if current_time.tm_sec >= 10 else '0'+str(current_time.tm_sec)
    return f'{hour}:{minute}:{secund}'



def get_system_info():
    # Получаем информацию о системе
    cpu_usage = psutil.cpu_percent(interval=1)  
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    system_info = (
        f"Операционная система: {platform.system()} {platform.release()}\n"
        f"Имя компьютера: {platform.node()}\n"
        f"Архитектура: {platform.architecture()[0]}\n"
        f"Процессор: {platform.processor()}\n"
        f"Загрузка процессора: {cpu_usage}%\n"
        f"Использование оперативной памяти: {memory_info.percent}% из {memory_info.total / (1024 ** 2):.2f} MB\n"
        f"Свободная память: {memory_info.available / (1024 ** 2):.2f} MB\n"
        f"Использование диска: {disk_info.percent}% из {disk_info.total / (1024 ** 3):.2f} GB\n"
        f"Свободное место на диске: {disk_info.free / (1024 ** 3):.2f} GB\n"
    )
    return system_info



date_info_label = tkinter.Label(text=get_date(), font='helvetica 25', bg="black", fg='white')

date_info_label.pack()

time_label =  tkinter.Label(text=get_time(), font='helvetica 100', bg="black", fg='white')
time_label.pack()

system_info_label = tkinter.Label(text=get_system_info(), font='helvetica 10', bg="black", fg='white')
system_info_label.pack()



def update_labels():
    date_info_label.config(text=get_date())
    time_label.config(text=get_time())
    root.after(1000, update_labels)

update_labels()

root.mainloop()