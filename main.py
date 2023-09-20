import tkinter as tk
import scrap as sc
import all_run as al
import os
from datetime import datetime, timedelta

def initial():
    global now, start, path, start_hour, run
    now= datetime.now()
    start = now-(timedelta(days=1))
    path = os.getcwd()
    if start.hour<21:
        start_hour = 20
    else:
        start_hour = start.hour
    run = sc.Scarp(now, datetime(start.year, start.month, start.day, start_hour, 0, 0), path)


root = tk.Tk()
root.title('天氣學實習圖資抓取')
root.geometry('500x700')
root.configure(background="blue")

val = tk.StringVar()  # 建立文字變數
val_start_time = tk.StringVar()
val_end_time = tk.StringVar()

def renew():
    initial()
    val_start_time.set(f"資料抓取起始時間{datetime(start.year, start.month, start.day, start_hour, 0, 0)}")
    val_end_time.set(f"資料抓取終止時間:{now}")

renew()
last_word = '資料已下載完畢'

frame_time = tk.Frame(root, pady=20, padx=90, bg="yellow")
frame_choice = tk.Frame(root, pady=0, padx=60, bg='#0bde40')

start_time_label = tk.Label(frame_time, textvariable=val_start_time, font=40, background="yellow")
start_time_label.pack()
end_time_label = tk.Label(frame_time, textvariable=val_end_time, font=40, background='yellow')
end_time_label.pack()
illustrate_label = tk.Label(frame_choice, text='選擇欲下載之資料', font=30, background="#0bde40")
illustrate_label.pack()

radio_btn0 = tk.Radiobutton(frame_choice, text='全部下載',variable=val, value='所有'+last_word, command=al.main, background="#0bde40")
radio_btn0.pack()

time_delta_10min = tk.Label(frame_choice, text='10分鐘一筆', font = 30, background="#0bde40")
time_delta_10min.pack()

# 放入第一個 Radiobutton
radio_btn1 = tk.Radiobutton(frame_choice, text='雷達',variable=val, value='雷達'+last_word, command=run.scrap_radar, background="#0bde40")
radio_btn1.pack()
#radio_btn1.select()   # 選擇第一個 Radiobutton

radio_btn2 = tk.Radiobutton(frame_choice, text='衛星圖資',variable=val, value='衛星圖資'+last_word, command=run.satellite, background="#0bde40")
radio_btn2.pack()

time_delta_1hr = tk.Label(frame_choice, text='1小時一筆', font = 30, background="#0bde40")
time_delta_1hr.pack()
# 放入第二個 Radiobutton
radio_btn3 = tk.Radiobutton(frame_choice, text='溫度',variable=val, value='溫度'+last_word, command=run.scrap_temperature, background="#0bde40")
radio_btn3.pack()

radio_btn4 = tk.Radiobutton(frame_choice, text='雨量',variable=val, value='雨量'+last_word, command=run.scrap_rainfall, background="#0bde40")
radio_btn4.pack()

radio_btn5 = tk.Radiobutton(frame_choice, text='閃電',variable=val, value='閃電'+last_word, command=run.scrap_lightning, background="#0bde40")
radio_btn5.pack()

radio_btn6 = tk.Radiobutton(frame_choice, text='風',variable=val, value='風'+last_word, command=run.scrap_wind, background="#0bde40")
radio_btn6.pack()

radio_btn7 = tk.Radiobutton(frame_choice, text='剖風儀',variable=val, value='剖風儀'+last_word, command=run.scrap_wind_profile, background="#0bde40")
radio_btn7.pack()

radio_btn8 = tk.Radiobutton(frame_choice, text='wissdom圖資',variable=val, value='wissdom圖資'+last_word, command=run.scrap_wissdom, background="#0bde40")
radio_btn8.pack()

time_delta_12hrs = tk.Label(frame_choice, text='每日00、12z各一筆', font = 30, background="#0bde40")
time_delta_12hrs.pack()

radio_btn9 = tk.Radiobutton(frame_choice, text='探空圖',variable=val, value='探空圖'+last_word, command=run.scrap_skew_T, background="#0bde40")
radio_btn9.pack()

radio_btn10 = tk.Radiobutton(frame_choice, text='天氣圖',variable=val, value='天氣圖'+last_word, command=run.scrap_analysis, background="#0bde40")
radio_btn10.pack()

# 放入 Label 標籤，設定 textvariable=val
finish_information = tk.Label(frame_choice, textvariable=val, font=('Arial',30), fg='#f00', background="#0bde40")
finish_information.pack()

button = tk.Button(frame_choice, text="更新時間", command=renew)


frame_time.pack()
frame_choice.pack()
button.pack()

root.mainloop()

